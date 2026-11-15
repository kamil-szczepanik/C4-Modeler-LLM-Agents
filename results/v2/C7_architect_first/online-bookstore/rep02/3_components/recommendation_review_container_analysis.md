## Overview
The Recommendation & Review Container provides secure book recommendations and user reviews for the Online Bookstore. It runs on Python and FastAPI within AWS ECS Fargate, ensuring scalability and 99.95% uptime.

## Key Elements
- **Review API Component**: FastAPI application handling review CRUD operations, moderation flags, and verified purchase badging.
- **Recommendation Query Component**: FastAPI application serving low-latency "Customers also bought" suggestions.
- **Recommendation Worker Component**: Decoupled Python background worker processing purchase events.
- **Amazon Aurora PostgreSQL**: Relational database for persistent storage of reviews and purchase histories.
- **Amazon ElastiCache Redis**: In-memory cache for fast recommendation lookups with Multi-AZ replication.
- **Amazon SQS / SNS**: Event bus used for triggering background workers and publishing analytics.

## Relationships
- **API Gateway -> Review API / Recommendation Query**: Routes HTTP/REST requests [HTTPS]
- **Review API / Recommendation Query -> Amazon Aurora PostgreSQL**: Reads and writes transactional data [TCP / PostgreSQL Wire Protocol with TLS]
- **Recommendation Query -> Amazon ElastiCache Redis**: Fetches cached recommendations [Redis TCP with TLS and AUTH]
- **Amazon SQS -> Recommendation Worker**: Triggers asynchronous background model updates [AWS SDK / SQS API]
- **Recommendation Query -> Event Bus (SNS)**: Logs impression and click-through metrics [AWS SDK]

## Technology Stack
- **Python with FastAPI**: High-performance asynchronous framework chosen for rapid API development and Pydantic validation.
- **Amazon ECS with AWS Fargate**: Serverless container orchestration to maintain scalability and simplify infrastructure management.
- **Amazon ElastiCache Redis**: Distributed caching layer to achieve sub-second page loads and recommendation delivery.
- **Pydantic**: Data validation library used to sanitize inputs and prevent XSS or SQL injection.
- **AWS Secrets Manager**: Secure storage for database credentials and Redis auth tokens.

## Rationale
Decoupling the recommendation worker via SQS isolates heavy data processing from public APIs to meet scalability requirements for 1M MAU. Multi-AZ Redis caching with graceful database fallbacks ensures high availability, strict security compliance, and sub-second performance.