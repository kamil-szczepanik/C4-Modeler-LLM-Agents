## Overview
The Engagement Service subsystem provides customer reviews, 5-star ratings, and "Customers also bought" recommendations for the online bookstore. It uses a decoupled microservices architecture to process user interactions while maintaining compliance with GDPR and CCPA.

## Key Elements
- **Review Service:** Spring Boot (Java) container managing customer reviews and ratings (ECS Fargate).
- **Recommendation Service:** Python/FastAPI container generating book recommendations (ECS Fargate).
- **Review Component:** Handles CRUD operations and OWASP input sanitization for user reviews.
- **Recommendation Component:** Executes collaborative filtering models for product suggestions.
- **Data Layers:** Amazon Aurora PostgreSQL, Amazon DynamoDB, and Amazon ElastiCache (Redis).
- **Integration Layer:** Amazon SNS/SQS Message Bus for asynchronous event publishing.

## Relationships
- **API Gateway / ALB -> Review Service:** Routes incoming HTTP REST requests for review submissions [HTTPS / TLS 1.3].
- **API Gateway / ALB -> Recommendation Service:** Serves recommendation queries [HTTPS / TLS 1.3].
- **Review Service -> Amazon Aurora PostgreSQL:** Persists review data and ratings [TCP / PostgreSQL via TLS 1.3].
- **Recommendation Service -> Amazon DynamoDB / ElastiCache:** Fetches pre-computed models and caches recommendation outputs [HTTPS / Redis Protocol].
- **Review Service -> Message Bus:** Publishes `ReviewSubmitted` events to trigger recommendation updates [Amazon SNS/SQS via HTTPS].

## Technology Stack
- **Spring Boot / Java:** Selected for the Review Service to handle enterprise-grade CRUD operations securely.
- **Python / FastAPI:** Selected for the Recommendation Service for native compatibility with machine learning libraries.
- **Amazon ECS Fargate:** Provides serverless container orchestration with isolated runtime scaling.
- **Amazon Aurora PostgreSQL & DynamoDB:** Store relational review data and high-speed recommendation models respectively.
- **Amazon ElastiCache (Redis):** Caches recommendation payloads to guarantee low latency.

## Rationale
Separating the JVM-based Review Service from the Python-based Recommendation Service optimizes resource allocation and security boundaries for distinct workloads. Utilizing caching and event-driven updates ensures high performance, availability, and scalability for 1 million MAU.