# Docker Learning Journey 🚢🐳

Welcome to my **Docker Learning Journey** repository!  
This repo is used for:

- **Learning the basics of Docker**
- **Hands-on examples to practice**
- **A mini project to apply what I’ve learned**

---

## Why this repo?

I created this repository to **track and structure my Docker learning**, ensuring I build a solid foundation before using Docker in real projects. This will help me:

✅ Build muscle memory with Docker CLI and concepts  
✅ Practice by containerizing simple applications  
✅ Apply concepts through a mini project/challenge (Docker Multi-Container Flask Application)

---

## Challenge/Mini-project 1:

# Docker Multi-Container Flask Application

A scalable Flask web app with Redis and nginx load balancing using Docker Compose.

## What This Project Does

- Flask web app that counts page visits
- Redis database stores the visit counter
- nginx load balancer distributes traffic across multiple Flask instances
- Everything runs in Docker containers

## Files

- `app.py` - Flask application
- `Dockerfile` - Flask container setup
- `docker-compose.yaml` - Container orchestration
- `nginx.conf` - Load balancer configuration

## Key Learning Points

### 1. Environment Variables in Flask

Instead of hardcoding Redis connection details:

```python
import os

r = redis.Redis(
    host=os.getenv('REDIS_HOST', 'redis'), 
    port=int(os.getenv('REDIS_PORT', '6379'))
)
```

Set them in docker-compose.yaml:
```yaml
environment:
  - REDIS_HOST=redis
  - REDIS_PORT=6379
```

### 2. Container Communication

Containers talk to each other using service names, not localhost:
- Redis service name: `redis`
- Flask connects to: `redis:6379`

### 3. Load Balancing

nginx configuration:
```nginx
events {}
http {
    upstream flask_app {
        server web:5003;
    }
    server {
        listen 5003;
        location / {
            proxy_pass http://flask_app;
        }
    }
}
```

## Useful Commands

### Basic Usage
```bash
# Start everything
docker-compose up --build

# Stop everything
docker-compose down

# View logs
docker-compose logs web
```

### Scaling
```bash
# Run 3 Flask instances
docker-compose up --scale web=3

# Check running containers
docker-compose ps
```

## Important Docker Compose Patterns

### Port Configuration
```yaml
web:
  expose:        # Internal only
    - "5003"

nginx:
  ports:         # External access
    - "5003:5003"
```

### Service Dependencies
```yaml
web:
  depends_on:
    - redis

nginx:
  depends_on:
    - web
```

### Volumes
```yaml
nginx:
  volumes:
    - ./nginx.conf:/etc/nginx/nginx.conf

redis:
  volumes:
    - redis-data:/data
```

## Testing

1. Visit `http://localhost:5003` - should show welcome message
2. Visit `http://localhost:5003/count` - should increment counter
3. Check logs to see requests hitting different instances (web-1, web-2, web-3)

## Common Mistakes to Avoid

- Don't use `localhost` for container communication - use service names
- Environment variables are strings - use `int()` when needed
- Only expose ports externally when necessary
- Use `expose` for internal communication, `ports` for external access
