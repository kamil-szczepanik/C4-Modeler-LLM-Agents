## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce site designed to buy physical and electronic books with recommendations and reviews. It utilizes a resilient, multi-region AWS cloud architecture with a dedicated Redis caching tier to support high-throughput cart and currency session operations.

## Key Elements
- Customers and Administrators/Content Moderators
- Single Page Application / Server-Side Rendered Frontend (AWS S3 / CloudFront)
- API Gateway (AWS API Gateway)
- Checkout & Order Container (Docker / AWS ECS/EKS, PostgreSQL)
- Redis Cache Tier (AWS ElastiCache Redis)
- Catalog & Search, Recommendations, and User & Reviews Containers (AWS ECS/EKS, OpenSearch)
- External Systems: Payment Gateway, Shipping APIs, Identity/Consent Management, Notification Services, Currency Exchange, Monitoring

## Relationships
- Customers -> Frontend: HTTPS via TLS 1.3
- Frontend -> API Gateway: HTTPS / REST / gRPC
- API Gateway -> Checkout & Order Container: Internal routing / gRPC
- Checkout & Order Container -> Redis Cache: Session caching, cart reads/writes [Redis drivers with connection pooling]
- Checkout & Order Container -> PostgreSQL: Persistent transactional data [PostgreSQL protocol]

## Technology Stack
- AWS ElastiCache Redis: Multi-AZ replication, automatic failover, and AWS KMS encryption at rest for high availability and security.
- PostgreSQL: Primary transactional data store for orders and catalog data.
- OpenTelemetry: Sidecar-based telemetry for monitoring cache hit/miss ratios, latency, and health.
- Redis Drivers: Configured with connection pooling, exponential backoff with jitter, and circuit breakers.

## Rationale
This architecture ensures 99.95% uptime and supports 1 million monthly active users by decoupling transient session data into a highly available Redis cache. Circuit breakers, fallback patterns to PostgreSQL, and strict payload limits guarantee fault tolerance and performance under heavy traffic loads.