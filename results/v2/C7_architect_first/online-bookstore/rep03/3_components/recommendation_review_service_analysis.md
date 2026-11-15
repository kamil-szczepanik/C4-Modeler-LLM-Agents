## Overview
The Recommendation & Review Service is a Python-based FastAPI microservice running on AWS ECS Fargate that manages product recommendations and 5-star customer reviews for the Online Bookstore. It ensures high performance, regional scalability, and strict GDPR/CCPA compliance for 1 million monthly active users.

## Key Elements
- API Controller Component (FastAPI)
- Review Management Component
- Recommendation Aggregator Component
- Data Access Repository Component (async SQLAlchemy)
- Caching / Fallback Store Component (Amazon ElastiCache Redis)
- Review Event Consumer Component (Amazon SQS / SNS)
- Third-Party Recommendation Engine (External System)
- Amazon Aurora (PostgreSQL) Global Database

## Relationships
- Core E-Commerce API -> API Controller: Invokes endpoints [gRPC over mTLS]
- API Controller -> Review Management & Recommendation Aggregator: Delegates operations [In-process]
- Recommendation Aggregator -> Third-Party Recommendation Engine: Fetches product suggestions [HTTPS/REST with circuit breaker]
- Recommendation Aggregator -> Caching / Fallback Store: Reads/writes cached recommendations [Redis TLS]
- Review Management & Recommendation Aggregator -> Data Access Repository: Persists and queries data [Async SQLAlchemy via TLS 1.3]
- Review Management -> Review Event Consumer: Publishes review events [Amazon SQS / SNS]

## Technology Stack
- Python / FastAPI: Lightweight, high-performance framework ideal for asynchronous microservices.
- AWS ECS (Fargate): Serverless container orchestration for multi-region scaling (`us-east-1`, `eu-west-1`, `ap-southeast-1`).
- Amazon Aurora (PostgreSQL) Global Database: Distributed relational storage with multi-region replication.
- Amazon ElastiCache Redis: Low-latency caching for pre-computed recommendations and heuristics fallback.
- Amazon SQS / SNS: Asynchronous event messaging with Dead-Letter Queues (DLQs) for review processing.
- Pydantic: Strict input validation and sanitization for OWASP Top-10 and GDPR/CCPA compliance.

## Rationale
This architecture guarantees 99.95% availability and sub-second performance by decoupling review ingestion via SQS queues and protecting against third-party outages using Redis fallbacks. Strict input validation, encryption, and regional containerization secure user data while supporting 1M MAU globally.