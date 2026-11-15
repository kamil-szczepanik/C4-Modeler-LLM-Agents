## Overview
The Recommendation Service provides real-time personalized book recommendations for the Online Bookstore platform. It is designed to handle high scalability, low latency, and strict GDPR/CCPA compliance.

## Key Elements
- **Recommendation API Controller**: Go service handling incoming gRPC requests, input validation, and fallback logic.
- **Recommendation Engine**: Python FastAPI service running collaborative filtering and ML scoring models.
- **Fallback & Resiliency Manager**: Component handling circuit breaking and static top-seller fallbacks.
- **Data Access Repository**: Go module interfacing with databases and caches.
- **Amazon ElastiCache Redis**: High-performance cache storing pre-computed recommendation vectors and fallbacks.
- **Amazon Aurora PostgreSQL**: Relational database storing anonymized historical purchase data.
- **AWS App Mesh**: Service mesh managing secure internal communications and telemetry.

## Relationships
- Amazon API Gateway -> Recommendation API Controller: Routes gRPC requests [gRPC over HTTP/2 via AWS App Mesh]
- Recommendation API Controller -> Recommendation Engine: Forwards scoring requests [gRPC over mTLS via AWS App Mesh]
- Recommendation API Controller -> Amazon ElastiCache Redis: Queries fallback top-sellers [Redis Protocol over TLS]
- Recommendation Engine -> Amazon ElastiCache Redis: Fetches pre-computed vectors [Redis Protocol over TLS]
- Recommendation Engine -> Amazon Aurora PostgreSQL: Queries order history [SQL/TCP with IAM Auth]

## Technology Stack
- **Go**: Chosen for the API Controller to ensure high concurrency and low latency.
- **Python (FastAPI)**: Chosen for the Recommendation Engine to leverage data science libraries.
- **gRPC / AWS App Mesh**: Used for high-performance internal IPC and strict mTLS security.
- **Amazon ECS Fargate**: Deploys containerized workloads with independent autoscaling profiles.
- **Amazon ElastiCache Redis**: Provides sub-millisecond caching and fallback data storage.
- **Amazon Aurora PostgreSQL**: Stores structured, pseudonymized purchase data.
- **OpenTelemetry**: Provides distributed tracing across microservices.

## Rationale
Separating the I/O-bound Go API Controller from the CPU-bound Python ML Engine across ECS Fargate tasks enables independent autoscaling and isolates workloads. Incorporating circuit breakers, Redis fallbacks, and strict mTLS encryption guarantees 99.95% uptime, <2s page load performance, and GDPR/CCPA compliance.