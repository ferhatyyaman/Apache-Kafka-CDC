# Simple CDC Application with Apache Kafka

This project is a simple Change Data Capture (CDC) application that queries new documents in a specific collection in MongoDB and produces them as JSON messages to Apache Kafka, which are then consumed by another application.

## Project Description

The project consists of two applications developed in the programming language of your choice:

1. Message Producer Application (App A): This application queries a specific collection in MongoDB every 10 seconds and detects newly added documents since its last run. It then sends the new document as a JSON message to Apache Kafka.

2. Message Consumer Application (App B): This application consumes messages from Apache Kafka and prints them to the console. The application runs in three copies and consumes messages concurrently.

The project also involves setting up an environment using Docker, which includes both applications and Apache Kafka. Docker images will be created using a Dockerfile and run using Docker Compose.

## Project Diagram

A diagram representing the project structure is shown below:

```

```

## Requirements

The following requirements are needed to run the project:

- Specification of the programming language and its version.
- MongoDB connection details.
- Apache Kafka connection details.

## Installation and Execution

You can follow the steps below to build and run the applications:

**1. Clone the Project:**

First, you need to clone the project from GitHub. You can clone the project to your local machine using the following command:

```shell
git clone https://github.com/ferhatyyaman/Apache-Kafka-CDC
```

**2. Navigate to the Project Directory:**

Once the cloning is complete, navigate to the project directory:

```
cd Apache-Kafka-CDC
```

**3. Build Docker Images and Run the Services:**

You can use Docker Compose to build the Docker images and run the application services. Run the following command to start Docker Compose:

```
docker-compose up --build
```

This command will build the services defined in the project and start them. Building the images may take some time. Once completed, the applications will be up and running, and data flow will begin.

**4. Start the Data Flow:**

To initiate the data flow, open a terminal and make sure you are in the project directory. Then, enter the following command to start the data producer:

```
python kafka-producer.py
```

This command will query new documents from a specific collection in MongoDB and send them as JSON messages to Apache Kafka.

After following these steps, you can observe the data flow in the terminal and monitor the changes in Apache Kafka and MongoDB.
