## Overview
The Recommendation Engine is a Python/FastAPI microservice within the Online Bookstore that delivers personalized "Customers also bought" suggestions while strictly enforcing GDPR/CCPA privacy constraints. It provides low-latency, scalable recommendations to handle 1 million monthly active users globally across AWS regions.

## Key Elements
- **API Controller**: FastAPI Router validating inputs via Pydantic.
- **Privacy Filter Middleware**: Scrubs PII and verifies GDPR/CCPA consent flags.
- **Experimentation Router**: Evaluates A/B testing variant weights.
- **Recommendation Logic Service**: Executes collaborative filtering using scikit-learn and pandas.
- **Model & Feature Store Client**: Fetches cached features with a fallback circuit breaker.
- **Amazon ElastiCache**: Redis cache providing low-latency feature storage.

## Relationships
- **API Gateway** -> **API Controller**: HTTPS/gRPC with mTLS via AWS Service Connect.
- **API Controller** -> **Privacy Filter Middleware**: In-process call.
- **Privacy Filter Middleware** -> **Experimentation Router**: In-process call.
- **Experimentation Router** -> **Recommendation Logic Service**: In-process call.
- **Recommendation Logic Service** -> **Model & Feature Store Client**: In-process call.
- **Model & Feature Store Client** -> **Amazon ElastiCache**: TCP/Redis with TLS and RedisAUTH.

## Technology Stack
- **Python / FastAPI**: High-performance asynchronous API framework for rapid request handling.
- **scikit-learn & pandas**: Machine learning and data manipulation libraries for recommendation algorithms.
- **Amazon ElastiCache for Redis**: In-memory cache ensuring sub-second response times for feature retrieval.
- **AWS ECS (Fargate)**: Serverless container platform enabling isolated, multi-region deployments with IAM least-privilege roles.

## Rationale
This architecture uses serverless containerization and in-memory caching to achieve sub-second latency and high availability across multiple global regions. Privacy filters and robust input sanitization ensure compliance with GDPR/CCPA and OWASP Top-10 security requirements.