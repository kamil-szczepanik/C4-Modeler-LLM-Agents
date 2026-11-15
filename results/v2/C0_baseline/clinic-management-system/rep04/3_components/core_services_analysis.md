## Overview
- **System**: Clinic Management System (Core Services Container).
- **Purpose**: Manages patient admissions, EMRs, scheduling, and billing for medium-sized hospitals and clinics.

## Key Elements
- **Patient Registry Component**: Manages demographic capture using Spring Data JPA.
- **Scheduling Engine Component**: Handles resource clash checks leveraging Redis Enterprise for real-time slot locking.
- **EMR Manager Component**: Manages clinical records with an immutable audit trail using PostgreSQL clusters and WORM object storage.
- **Event Publisher Component**: Emits domain and audit events asynchronously via Apache Kafka.
- **Resilience4j Circuit Breaker**: Protects system availability and performance.
- **Encrypted Local Disk Buffer**: Stores audit logs locally prior to Kafka dispatch.

## Relationships
- **API Gateway (Kong/Envoy) -> Core Services**: Invokes business logic via gRPC over mTLS (Istio).
- **Core Services -> PostgreSQL**: Reads/writes relational data using encrypted JDBC.
- **Core Services -> Redis Enterprise**: Caches sessions, authorization scopes, and scheduling locks using encrypted cache protocols.
- **Core Services -> Apache Kafka**: Publishes domain and audit events using Kafka Protocol with SASL/SCRAM.
- **Core Services -> WORM Object Storage**: Persists long-term data for 10-year retention via Secure Object Storage API.

## Technology Stack
- **Java & Spring Boot**: Core application runtime providing modular component architecture and dependency injection.
- **Spring Security**: Enforces fine-grained RBAC/ABAC and JWT validation.
- **Resilience4j**: Implements circuit breaking and fallbacks to protect R-07 performance.
- **OpenTelemetry**: Provides distributed tracing across all gRPC and Kafka boundaries.
- **AES-256 & mTLS**: Secures data at rest across databases, local buffers, and object storage, and data in transit via Istio.

## Rationale
- Decomposing Core Services into modular Spring components guarantees sub-second EMR load times (<1s P95) while maintaining high availability (99.99%).
- Integrating durable local disk buffering, asynchronous Kafka audit logging, and strict cryptographic controls ensures full HIPAA and GDPR compliance without sacrificing performance.