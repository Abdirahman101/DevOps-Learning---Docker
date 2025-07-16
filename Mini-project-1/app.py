from flask import Flask
import redis
import os

app = Flask(__name__)

#r = redis.Redis(host='redis', port=6379)
#Created redis connection

r = redis.Redis(host=os.getenv('REDIS_HOST', 'redis'), port=int(os.getenv('REDIS_PORT', '6379')))
#creating environment variables for redis connection

@app.route('/')
def hello_world():
    return 'Welcome to the CoderCo Challenge'

@app.route('/count')
def count():
    count = r.incr('visit_count')
    return f'This page has been visited {count} times!'
    # Increment the visit count in Redis

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)