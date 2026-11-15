## Overview
The EMR Engine is a core microservice within the Clinic Management System responsible for managing electronic medical records, clinical data caching, and HL7 FHIR interoperability. It ensures high-performance, secure clinical data access while satisfying strict HIPAA, GDPR, and 10-year data retention mandates.

## Key Elements
- **EMR Controller**: Spring REST/gRPC facade handling ingress.
- **Clinical Record Service**: Domain logic, validation, ABAC, and Resilience4j circuit breakers.
- **HL7 FHIR Transformer**: HAPI FHIR library and Spring WebFlux for reactive payload serialization.
- **Audit Interceptor**: Chronicle Queue-backed event publisher for cryptographic non-repudiation.
- **PostgreSQL Cluster**: Primary data store with AES-256 and LUKS.
- **Redis**: Hot patient data cache with in-memory encryption and TTL.
- **Audit Logging Sidecar**: Sidecar proxy for immutable logging.

## Relationships
- **Core API Service -> EMR Controller**: Transmits requests via gRPC over TLS with mutual TLS (mTLS).
- **Clinical Record Service -> PostgreSQL Cluster**: Persists patient records via TCP.
- **Clinical Record Service -> Redis**: Caches EMR data via TCP.
- **Audit Interceptor -> Audit Logging Sidecar**: Dispatches signed audit events.
- **HL7 FHIR Transformer -> External Systems**: Exchanges lab and imaging payloads via HL7 FHIR REST APIs.

## Technology Stack
- **Java / Spring Boot**: Chosen for enterprise maturity, high concurrency handling, and robust ecosystem integration.
- **Spring Data JPA / Hibernate**: Provides robust ORM capabilities for relational mapping to PostgreSQL.
- **HAPI FHIR**: Industry standard library for serializing and parsing HL7 FHIR R4 medical resources.
- **Project Reactor (Spring WebFlux)**: Enables reactive, non-blocking data ingestion to prevent thread-pool exhaustion.
- **Resilience4j**: Implements circuit breaker patterns to gracefully handle database failovers.
- **Chronicle Queue**: Provides a bounded, disk-backed queue ensuring zero audit log loss.
- **G1GC (JVM)**: Tuned garbage collection to strictly prevent latency spikes exceeding sub-second P95.

## Rationale
This architecture uses a stateless, containerized Spring Boot design deployed across hybrid Kubernetes clusters to guarantee 99.99% active-active availability and sub-second P95 response times. Strict security controls, including mTLS, application-layer envelope encryption, and immutable audit logging, fulfill rigorous HIPAA and GDPR compliance requirements.