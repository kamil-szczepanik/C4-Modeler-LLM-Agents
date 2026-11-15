## Overview
The Online Bookstore Recommendation Engine provides personalized book recommendations and "customers also bought" suggestions for users. It is a Python-based container running on Amazon ECS Fargate designed for high scalability and low latency.

## Key Elements
- API Router / Controller (FastAPI)
- Recommendation Service (Python)
- Model Scoring Agent (Python / scikit-learn / PyTorch)
- Data Access Repository (SQLAlchemy / Boto3)
- Event Ingestion Listener (Python / Celery or asyncio worker)
- Model Training Pipeline / Job Scheduler (Python / AWS SageMaker / ECS Scheduled Tasks)
- Recommendation Cache Manager (Python / Redis Client)

## Relationships
- AWS API Gateway -> API Router / Controller via HTTPS/JSON
- Event Ingestion Listener -> Amazon SQS / SNS via AMQP/HTTPS
- Data Access Repository -> Amazon DynamoDB & Amazon OpenSearch Service via TCP/HTTPS
- Model Training Pipeline -> Amazon Aurora PostgreSQL via TCP/SQL
- Model Training Pipeline & Model Scoring Agent -> Amazon S3 via HTTPS
- Recommendation Cache Manager -> Amazon ElastiCache (Redis) via TCP/Redis protocol

## Technology Stack
- FastAPI: High-performance Python framework for building REST APIs with automatic OpenAPI generation.
- Amazon ECS Fargate: Serverless container compute for running Python application components.
- Amazon ElastiCache (Redis): In-memory caching to serve instant recommendations and protect the scoring engine.
- Amazon DynamoDB & Amazon OpenSearch Service: Fast profile retrieval and vector similarity search.
- Amazon Aurora PostgreSQL & Amazon S3: Historical transaction storage and machine learning model artifact persistence.

## Rationale
The micro-components separate real-time event ingestion, cached serving, and offline model training to meet the strict 2-second page load requirement. This decoupled, asynchronous design effortlessly handles 1 million monthly active users on AWS.