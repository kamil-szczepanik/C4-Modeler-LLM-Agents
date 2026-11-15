## Overview
The Recommendation Service is a microservice within the Online Bookstore platform that generates personalized "Customers also bought" suggestions. It processes asynchronous order events and serves real-time recommendations to maintain high performance under scale.

## Key Elements
- Recommendation Controller (NestJS REST Controller)
- Event Consumer Worker (NestJS Background Service)
- Recommendation Engine Core (TypeScript Domain Service)
- Model Cache Manager (NestJS Provider)
- Data Access Repository (NestJS Provider)
- Amazon OpenSearch & Amazon ElastiCache (Redis)

## Relationships
- API Gateway -> Recommendation Controller: Routes inbound requests [HTTP/REST]
- SQS -> Event Consumer Worker: Consumes asynchronous domain events [SQS/Polling]
- Recommendation Engine Core -> Model Cache Manager: Checks precomputed cache [Function Call]
- Model Cache Manager -> Amazon ElastiCache (Redis): Reads/writes cached payloads [Redis Protocol]
- Recommendation Engine Core -> Amazon OpenSearch: Queries product metadata and vectors [HTTPS/REST]

## Technology Stack
- Node.js & NestJS: Chosen for scalable asynchronous I/O and modular component architecture
- TypeScript: Ensures type safety and maintainability across domain services
- Amazon ECS/Fargate: Provides serverless container orchestration for auto-scaling
- Amazon ElastiCache (Redis): Enables low-latency caching to meet sub-2s page load constraints
- Amazon OpenSearch: Powers fast vector and catalog lookups for recommendations

## Rationale
This component architecture uses specialized workers, caching layers, and decoupled engines to handle 1M MAU with low latency. It strictly adheres to the system's performance and scalability non-functional requirements.