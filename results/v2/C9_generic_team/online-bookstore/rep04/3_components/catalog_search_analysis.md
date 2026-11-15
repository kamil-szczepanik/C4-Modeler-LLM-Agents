## Overview
The Online Bookstore system is a scalable e-commerce platform designed for browsing, searching, and purchasing physical and electronic books with integrated recommendations and reviews. It delivers high-availability retail services globally while ensuring strict performance and security compliance.

## Key Elements
- Customers and Administrators/Content Moderators
- Single Page Application / Server-Side Rendered Frontend (AWS S3 / CloudFront)
- API Gateway (AWS API Gateway)
- Catalog & Search (AWS ECS/EKS container using Hexagonal Architecture)
- Checkout & Order, Recommendations, and User & Reviews containers
- OpenSearch Database and PostgreSQL Database
- Redis Cache
- Async Event Bus (AWS EventBridge / Kafka)

## Relationships
- API Gateway -> Catalog & Search: Routes catalog requests [Internal TLS / REST / gRPC]
- Catalog & Search -> Redis Cache: Performs read-through caching [Redis TCP Protocol]
- Catalog & Search -> OpenSearch Database: Indexes and searches catalog data [Native database protocols (NoSQL drivers)]
- Catalog & Search -> Async Event Bus: Publishes and consumes state changes [Asynchronous pub/sub messaging]

## Technology Stack
- AWS ECS/EKS & Docker: Containerized deployment ensuring scalability for 1M MAU.
- OpenSearch: High-performance search engine powering fast catalogue queries.
- Redis: Read-through caching to meet sub-2-second page load requirements.
- PostgreSQL: Primary relational datastore for transactional consistency.
- OpenTelemetry: Distributed tracing and structured logging for observability.

## Rationale
This architecture uses CQRS, Hexagonal Architecture, and Redis caching to ensure rapid sub-2-second response times under heavy traffic. Outbox patterns, index aliasing, and circuit breakers guarantee high availability and zero-downtime deployments.