##FROM python:3.8-slim

#WORKDIR /app

#COPY . .

#RUN apt-get update && apt-get install -y \
    #gcc \
    #python3-dev \
    #libmariadb-dev \
    #pkg-config

#RUN pip install flask mysqlclient

#EXPOSE 5002

#CMD ["python", "app.py"]
# This Dockerfile sets up a simple Flask application that listens on port 5002.
# It uses a slim version of Python 3.8, copies the application code into the
# container, installs Flask and MySQL client, and runs the application.



#Stage 1: Build Stage
FROM python:3.8-slim AS build

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config

COPY . .

RUN pip install flask mysqlclient

#Stage 2: prodiction stage
FROM python:3.8-slim

WORKDIR /app

COPY --from=build /app /app

EXPOSE 5002

CMD ["python", "app.py"]