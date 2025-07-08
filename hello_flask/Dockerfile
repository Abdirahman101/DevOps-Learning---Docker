FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 5004
CMD ["python", "app.py"]
# This Dockerfile sets up a simple Flask application that listens on port 5004.
# It uses a slim version of Python 3.8, copies the application code into the
# container, installs Flask, and runs the application.