from flask import Flask
# This is a simple Flask application that returns "Hello, world!" when accessed at the root URL.
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

if  __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
# To run this application, use the command: python app.py
# You can then access it in your web browser at http://localhost:5004/
