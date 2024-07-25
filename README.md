
# Banking API

## Description

This project is a showcase of a Mini Banking API, designed as a microservice architecture. The API allows for basic banking operations such as account management and transaction handling, utilizing modern technologies for efficient and scalable solutions.

## Tech Stack

- **Python 3.10-slim**: A lightweight and efficient version of Python, perfect for microservices.
- **Docker**: A containerization platform that allows for the deployment and management of microservices in isolated environments.
- **Docker Compose**: A tool for defining and running multi-container Docker applications, ensuring seamless integration and orchestration of the services.
- **Redis**: An in-memory data structure store, used as a cache to enhance performance and as a message broker for inter-service communication.

## Project Structure

```
banking-api
│
├── apis/
│   ├── auth_service/
│   │   ├── auth_service/
│   │   │   ├── __init__.py
│   │   │   ├── settings.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── tests.py
│   │   ├── Dockerfile
│   │   └── manage.py
│   │
│   ├── account_service/
│   │   ├── account_service/
│   │   │   ├── __init__.py
│   │   │   ├── settings.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── tests.py
│   │   ├── Dockerfile
│   │   └── manage.py
│   │
│   ├── transaction_service/
│   │   ├── transaction_service/
│   │   │   ├── __init__.py
│   │   │   ├── settings.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── tests.py
│   │   ├── Dockerfile
│   │   └── manage.py
│   │
├── share/
│   ├── utilities/
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   ├── response_controller.py
│   │   ├── permissions.py
│   ├── requirements.txt
│
├── .envexample
├── .gitignore
├── docker-compose.yml
├── run_tests.sh
├── README.md
├── venv/
```

## How to Start

### Prerequisites

- **Docker**: Ensure Docker is installed on your system. [Get Docker](https://www.docker.com/get-started)
- **Docker Compose**: Make sure Docker Compose is installed. [Install Docker Compose](https://docs.docker.com/compose/install/)

### Steps

1. **Clone the Repository**
   ```sh
   git clone https://github.com/tanakon8529/micro-banking-services.git
   cd banking-api
   ```

2. **Copy Environment Variables File**
   ```sh
   cp .envexample .env
   ```

3. **Edit the `.env` File**
   - Open the `.env` file and update the necessary environment variables such as `CLIENT_ID`, `CLIENT_SECRET`, `REDIS_HOST`, `REDIS_PORT`, and `REDIS_PASSWORD`.

4. **Build and Start the Docker Containers**
   ```sh
   docker-compose up --build
   ```

## How to Test

1. **Ensure Docker Containers are Running**
   ```sh
   docker-compose up
   ```

2. **Run Tests**
   ```sh
   ./run_tests.sh
   ```

## How to Edit Configuration

### Edit Environment Variables

1. **Copy the `.envexample` File**
   ```sh
   cp .envexample .env
   ```

2. **Update Environment Variables**
   - Open the `.env` file in a text editor.
   - Update the variables such as `CLIENT_ID`, `CLIENT_SECRET`, `REDIS_HOST`, `REDIS_PORT`, and `REDIS_PASSWORD` as needed.

### Rebuild Docker Containers to Apply Changes

```sh
docker-compose up --build
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
