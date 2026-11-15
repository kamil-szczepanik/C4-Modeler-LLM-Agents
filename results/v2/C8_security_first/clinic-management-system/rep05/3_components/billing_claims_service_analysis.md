## Overview
- Manages patient admissions, EMR, scheduling, and billing for clinics.
- Ensures HIPAA/GDPR compliance, 99.99% availability, and 10-year data retention.

## Key Elements
- Billing Specialist & Finance Auditor (Users)
- Billing & Claims Service (Java Spring Boot Container)
- EMR & Patient Service (Node.js / Fastify Container)
- Apache Kafka & PostgreSQL (CloudNativePG)
- Insurance Claim Clearinghouse (External System)

## Relationships
- EMR & Patient Service -> Billing & Claims Service: gRPC over mTLS
- Billing & Claims Service -> Insurance Claim Clearinghouse: Asynchronous queue via Apache Kafka
- Billing & Claims Service -> PostgreSQL: Encrypted database connection with field-level tokenization

## Technology Stack
- Java Spring Boot: Core runtime for business logic and microservices
- Apache Kafka: Event-driven asynchronous messaging and transactional outbox pattern
- PostgreSQL: Relational persistence with AES-256 encryption at rest
- Resilience4j: Circuit breaking for outbound HTTP/gRPC calls
- OpenTelemetry: Distributed tracing across services

## Rationale
- Active-active multi-region hybrid setup meets 99.99% availability.
- Tokenization and RBAC satisfy HIPAA/GDPR security mandates.