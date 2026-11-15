## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing securely. It provides high availability (99.99%) and strict adherence to HIPAA and GDPR compliance regulations.

## Key Elements
- Patients & Family Caregivers
- Kong/Envoy API Gateway
- Patient Portal BFF (Node.js/TypeScript)
- Core Services (Java, Spring Boot)
- Apache Kafka Event Stream
- Redis Enterprise Caching Layer
- External Identity Provider (IdP)

## Relationships
- Patient Portal BFF -> Core Services: Queries business logic [gRPC over mTLS]
- API Router -> Apache Kafka: Publishes compliance audit logs [Async TCP]
- Kong/Envoy API Gateway -> Patient Portal BFF: Routes patient requests [HTTPS/TLS 1.3]
- Patient Portal BFF -> Redis Enterprise: Caches session state and rate limits [TLS 1.3]

## Technology Stack
- Node.js with TypeScript & Fastify/Express: Chosen for non-blocking I/O efficiency in high-concurrency BFF workloads.
- gRPC over mTLS: Ensures secure, low-latency inter-service communication.
- Apache Kafka: Handles asynchronous event publishing for notifications and audit logging.
- Redis Enterprise: Provides distributed rate limiting, caching, and session revocation tracking.

## Rationale
This architecture decouples synchronous aggregation from asynchronous event processing to guarantee sub-second P95 response times and active-active high availability. It enforces strict token exchange, consent management, and data masking to satisfy rigorous HIPAA and GDPR security constraints.