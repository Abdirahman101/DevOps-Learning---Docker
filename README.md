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

## Docker Multi-Container Flask Application

This project demonstrates how to build a scalable multi-container application using Docker Compose, featuring a Flask web application, Redis database, and nginx load balancer.

---

## Project Structure
.
├── app.py                 # Flask application
├── Dockerfile            # Container definition for Flask app
├── docker-compose.yaml   # Multi-container orchestration
└── nginx.conf            # nginx load balancing configuration

1. Environment Variables in Flask
Challenge: Making Flask app configurable through environment variables instead of hardcoded values.
Solution: Using os.getenv() with fallback defaults
pythonimport os

r = redis.Redis(
    host=os.getenv('REDIS_HOST', 'redis'), 
    port=int(os.getenv('REDIS_PORT', '6379'))
)
Key Concepts:

Environment variables are always strings - convert with int() when needed
Always provide sensible defaults
Use descriptive variable names (e.g., REDIS_HOST not just host)

2. Docker Compose Service Communication
Challenge: Containers need to communicate with each other by name, not localhost.
Solution: Use service names as hostnames
yamlservices:
  web:
    environment:
      - REDIS_HOST=redis  # Service name, not localhost
      - REDIS_PORT=6379
  redis:
    image: "redis:latest"
Key Concepts:

Docker Compose creates an internal network where services can reach each other by name
Default Redis host should be the service name (redis), not localhost

3. Load Balancing and Scaling
Challenge: Running multiple instances of the same service behind a load balancer.
Solution: Use nginx as reverse proxy with Docker Compose scaling
yamlweb:
  expose:        # Internal port only
    - "5003"
  
nginx:
  ports:         # External access point
    - "5003:5003"
  volumes:
    - ./nginx.conf:/etc/nginx/nginx.conf
Useful Commands
Development
bash# Build and run all services
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs
docker-compose logs web

# Stop all services
docker-compose down
Scaling
bash# Scale web service to 3 instances
docker-compose up --scale web=3

# Scale with build
docker-compose up --scale web=3 --build

# Check running containers
docker-compose ps
Debugging
bash# Execute command in running container
docker-compose exec web bash

# View service logs
docker-compose logs -f web

# Restart specific service
docker-compose restart web
Key Configuration Patterns
Docker Compose Environment Variables
yamlservices:
  web:
    environment:
      - REDIS_HOST=redis
      - REDIS_PORT=6379
      # Alternative object syntax:
      # environment:
      #   REDIS_HOST: redis
      #   REDIS_PORT: 6379
Service Dependencies
yamlservices:
  web:
    depends_on:
      - redis    # Ensures redis starts before web
  nginx:
    depends_on:
      - web      # Ensures web starts before nginx
Port Exposure vs Publishing
yamlservices:
  web:
    expose:      # Internal network only
      - "5003"
  
  nginx:
    ports:       # External access
      - "5003:5003"
Volume Mounting
yamlservices:
  nginx:
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf  # Mount local file
  redis:
    volumes:
      - redis-data:/data                    # Named volume

volumes:
  redis-data:    # Persistent storage
nginx Load Balancing Configuration
nginxevents {}

http {
    upstream flask_app {
        server web:5003;  # Docker Compose handles multiple instances
    }

    server {
        listen 5003;
        location / {
            proxy_pass http://flask_app;
        }
    }
}
Best Practices Learned

Use environment variables for configuration instead of hardcoding values
Use expose vs ports - only expose external ports where needed
Service naming - use descriptive names that reflect their purpose
Dependencies - define service startup order with depends_on
Volume persistence - use named volumes for data that should survive container restarts
Health checks - consider adding health checks for production readiness

Common Pitfalls to Avoid

localhost confusion: Use service names, not localhost for inter-container communication
Port conflicts: When scaling, don't publish the same port multiple times
Environment variable types: Remember to convert strings to integers when needed
Volume paths: Ensure local paths exist and are accessible to Docker
Build context: Make sure Dockerfile and required files are in the build context

Testing the Application

Basic functionality: Visit http://localhost:5003 and http://localhost:5003/count
Redis persistence: Restart containers and verify count persists
Load balancing: Check logs to see requests hitting different instances (web-1, web-2, web-3)
Scaling: Try different scale numbers and verify all instances receive traffic

This project demonstrates fundamental Docker Compose concepts essential for building scalable containerized applications.


