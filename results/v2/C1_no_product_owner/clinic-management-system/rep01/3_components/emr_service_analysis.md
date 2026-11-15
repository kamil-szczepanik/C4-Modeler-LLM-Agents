## Overview
The EMR Service is a Spring Boot container within the Clinic Management System that manages electronic medical records with strict HIPAA compliance, cryptographic audit trails, and high availability. It operates across a hybrid Kubernetes and AWS (`eu-central-1`) infrastructure.

## Key Elements
- **EMR API Controller (Spring MVC):** Exposes RESTful endpoints for clinical documentation and payload validation.
- **Clinical Record Manager (Spring Service):** Contains domain logic, ABAC authorization, and an encrypted local Caffeine cache using AES-256 envelope encryption with memory-locking (`mlock`).
- **FHIR Transformer (HAPI FHIR Library):** Maps internal clinical models to HL7 FHIR standards.
- **Audit Trail Publisher:** Publishes cryptographically signed, non-repudiation audit events backed by a local durable write-ahead log (WAL).
- **Data Persistence Layer:** PostgreSQL database with TLS-secured JDBC and HSM-managed column encryption.
- **Message Broker Container:** Geo-local Apache Kafka clusters using MirrorMaker, secured via TLS/mTLS and SCRAM-SHA-512.

## Relationships
- EMR API Controller -> Clinical Record Manager: In-process method calls
- Clinical Record Manager -> FHIR Transformer: In-process domain-to-FHIR mapping [Java objects]
- Clinical Record Manager -> Data Persistence Layer: Queries and persists clinical records [TLS-secured JDBC]
- Audit Trail Publisher -> Message Broker Container: Publishes signed audit events [TLS/mTLS and SCRAM-SHA-512]

## Technology Stack
- **Spring Boot & Spring MVC:** Core application framework for rapid service development and REST API exposure.
- **HAPI FHIR Library:** Standardized mapping tool ensuring HL7 FHIR interoperability for lab and imaging systems.
- **Caffeine Cache:** Local in-memory cache with AES-256 and `mlock` memory protection to meet sub-second P95 performance without cross-region latency.
- **PostgreSQL & JDBC:** Relational data storage utilizing TLS-secured connections and HSM column encryption for 10-year data retention.
- **Apache Kafka & MirrorMaker:** Distributed event streaming platform ensuring active-active geo-local message replication.
- **OpenTelemetry & Resilience4j:** Observability and circuit-breaking frameworks maintaining 99.99% availability and latency tracking.

## Rationale
This architecture uses internal component decomposition, local memory caching, and durable WAL buffers to achieve sub-second P95 latencies and high availability across hybrid cloud boundaries. It enforces strict HIPAA compliance and non-repudiation through fine-grained ABAC, asymmetric audit logging, and encrypted data protection at rest and in transit.