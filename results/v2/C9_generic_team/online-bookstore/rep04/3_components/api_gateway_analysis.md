## Overview
The Online Bookstore is a scaled-down e-commerce platform providing catalog browsing, secure checkout, reviews, and personalized recommendations for 1M MAU. It features a microservices architecture hosted on AWS across multiple global regions.

## Key Elements
- Frontend: Single Page Application / Server-Side Rendered Frontend (AWS S3 / CloudFront)
- Entry Point: API Gateway (AWS API Gateway)
- Backend Services: Catalog & Search, Checkout & Order, Recommendations, User & Reviews (AWS ECS/EKS)
- Data Stores: PostgreSQL Database, OpenSearch Database, Redis Cache
- Infrastructure Services: AWS EventBridge / Kafka, AWS Secrets Manager, OpenTelemetry sidecars

## Relationships
- Single Page Application / Server-Side Rendered Frontend -> API Gateway: Sends API requests via [HTTPS / TLS]
- API Gateway -> Catalog & Search: Routes catalog requests via [Internal TLS / REST / gRPC]
- API Gateway -> Checkout & Order: Routes checkout requests via [Internal TLS / REST / gRPC]
- API Gateway -> Recommendations: Routes recommendation requests via [Internal TLS / REST / gRPC]
- API Gateway -> User & Reviews: Routes user and review requests via [Internal TLS / REST / gRPC]

## Technology Stack
- AWS API Gateway: Entry point for multi-region routing, rate limiting, JWT validation, and circuit breaking
- AWS ECS/EKS & Docker: Container orchestration for scalable backend microservices
- PostgreSQL: ACID-compliant transactional database for orders and checkout
- OpenSearch: Full-text search engine for catalogue keyword search and browsing
- Redis: Low-latency caching for read-heavy endpoints and session data
- OpenTelemetry: Distributed tracing and telemetry sidecars for end-to-end observability

## Rationale
This architecture uses multi-region AWS services and containerization to guarantee 99.95% uptime and scale seamlessly for 1 million MAU. Decoupled microservices with gateway-level caching, rate-limiting, and circuit breakers ensure sub-2-second page loads and robust security.