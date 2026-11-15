## Overview
The Customer Service system manages customer profiles, preferences, and support tickets for the Online Bookstore. It ensures secure, GDPR-compliant handling of PII while delivering scalable, low-latency support operations.

## Key Elements
- **Profile Handler**: Go component managing user account details and communication preferences.
- **Support Ticket Manager**: Go component handling inquiry lifecycles and agent interactions.
- **Data Access Repository**: Go component utilizing `pgx` for database persistence.
- **Cache Manager**: Go component interfacing with Amazon ElastiCache (Redis).
- **Event Publisher**: Go component emitting domain events to Amazon EventBridge.
- **Amazon Aurora PostgreSQL**: Primary relational database with AWS KMS encryption.
- **Envoy Service Mesh**: Ingress and mesh proxy enforcing mTLS (SPIFFE/SPIRE).

## Relationships
- **Envoy Service Mesh -> Profile Handler**: Routes validated external/internal requests [gRPC/REST over mTLS].
- **Support Ticket Manager -> Notification Service**: Triggers ticket updates and emails [REST over HTTPS].
- **Data Access Repository -> Amazon Aurora PostgreSQL**: Persists and queries customer data [PostgreSQL wire protocol over TLS 1.3 with IAM authentication].
- **Event Publisher -> Amazon EventBridge**: Emits asynchronous domain events [JSON over HTTPS].
- **Cache Manager -> Amazon ElastiCache (Redis)**: Caches read-heavy customer profile metadata [Redis wire protocol over TLS].

## Technology Stack
- **Go**: High-performance compiled language for rapid request execution.
- **`pgx`**: PostgreSQL driver supporting connection pooling and parameterized queries.
- **`go-playground/validator`**: Schema validation library for strict input sanitization.
- **Amazon ECS on Fargate**: Container orchestration platform for autoscaling.
- **Amazon Aurora PostgreSQL**: Managed relational database with IAM authentication and read replicas.
- **Amazon ElastiCache (Redis)**: In-memory cache for sub-second profile metadata reads.

## Rationale
This architecture uses Go microservices deployed on AWS ECS Fargate with Redis caching to meet 1M MAU scalability and sub-second performance goals. Zero-trust networking (mTLS), IAM database authentication, and strict input validation ensure OWASP Top-10 mitigation and GDPR/CCPA compliance.