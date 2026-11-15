## Overview
The Recommendation Service provides personalized "Customers also bought" recommendations and tracking for the Online Bookstore. It ensures high performance, compliance, and resilience across global AWS regions.

## Key Elements
- **RecommendationEngine**: FastAPI core component handling collaborative filtering and input validation.
- **CacheManager**: Manages low-latency retrieval using Amazon ElastiCache (Redis).
- **FallbackManager**: Implements circuit breakers to query Amazon Aurora PostgreSQL for genre-specific best-sellers during cache failures.
- **ABTestRouter**: Evaluates request headers to assign algorithm variants and campaign IDs.
- **EventPublisher**: Asynchronously logs pseudonymized impression and click events to Amazon SQS via AWS SDK (Boto3).

## Relationships
- **API Gateway** -> **RecommendationEngine**: Routes recommendation requests via REST/gRPC using mTLS.
- **RecommendationEngine** -> **CacheManager**: Reads and writes recommendation data using the Redis Protocol with TLS.
- **FallbackManager** -> **Amazon Aurora PostgreSQL**: Queries fallback best-sellers using PostgreSQL Protocol over TLS 1.3.
- **EventPublisher** -> **Amazon SQS**: Publishes pseudonymized events using HTTPS and AWS KMS encryption with IAM least privilege.

## Technology Stack
- **FastAPI / Python**: Chosen for high-performance async request handling and Pydantic input validation.
- **Amazon ElastiCache (Redis)**: Global Datastores utilized for low-latency caching (<2s page load).
- **Amazon SQS**: Enables asynchronous, non-blocking telemetry and metric publishing.
- **AWS ECS Fargate**: Serverless container orchestration with auto-scaling to handle 1M MAU.
- **AWS KMS**: Provides encryption-at-rest for Redis and SQS to meet OWASP Top-10 security standards.

## Rationale
This architecture decouples telemetry and caching to protect the 99.95% uptime SLA while meeting stringent GDPR/CCPA privacy requirements. Multi-region Redis replication and fallback mechanisms guarantee sub-2-second page loads globally.