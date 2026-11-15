## Overview
The Reviews Container manages customer ratings, 5-star reviews, and asynchronous compliance workflows for the Online Bookstore. It is architected for high availability, fault tolerance, and sub-second performance under peak e-commerce loads.

## Key Elements
- Reviews Container (Docker, Amazon ECS/EKS)
- Amazon Aurora/RDS
- Amazon ElastiCache (Redis)
- AWS SNS & AWS SQS (with DLQ)
- Compliance Workers (Docker, Amazon ECS/EKS)
- API Gateway & BFF (AWS API Gateway)

## Relationships
- API Gateway & BFF -> Reviews Container: Routes review and rating queries [HTTPS/REST]
- Reviews Container <-> Amazon Aurora/RDS: Persists and retrieves reviews and aggregates [PostgreSQL/TCP]
- Reviews Container <-> Amazon ElastiCache (Redis): Caches aggregated ratings and serves fallbacks [Redis Protocol/TCP]
- Reviews Container -> AWS SNS: Publishes new review events for asynchronous processing [AWS SDK/HTTPS]
- AWS SNS -> AWS SQS: Distributes review and compliance events [AWS Protocol]
- AWS SQS -> Compliance Workers: Triggers GDPR/CCPA data redaction workflows [AWS Protocol]

## Technology Stack
- Docker & Amazon ECS/EKS: Containerization and orchestration for scalability and health monitoring.
- Amazon ElastiCache (Redis): In-memory caching for aggregated ratings to maintain <2s page loads and enable circuit-breaker fallbacks.
- AWS SNS / SQS / DLQ: Event-driven decoupling, asynchronous processing, and dead-letter queue error handling.
- AWS X-Ray: Distributed tracing and structured JSON logging for low MTTR.
- Repository Pattern & Bulkhead Pattern: Code architecture and resource isolation separating reads from writes.

## Rationale
This architecture uses caching, circuit breakers, and bulkhead isolation to guarantee 99.95% uptime and fast page loads under high concurrency. Asynchronous eventing and robust compliance tooling ensure seamless GDPR/CCPA adherence without impacting core e-commerce performance.