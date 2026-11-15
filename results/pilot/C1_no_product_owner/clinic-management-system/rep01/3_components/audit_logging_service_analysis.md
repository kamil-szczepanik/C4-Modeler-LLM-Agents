## Overview
The Audit Logging Service captures, normalizes, cryptographically secures, and permanently archives security and compliance events for the Clinic Management System. It guarantees regulatory adherence, tamper-resistance, and high availability across hybrid cloud infrastructures.

## Key Elements
- Audit Log Ingestor (Spring WebFlux reactive endpoint)
- Event Normalization Engine (Jackson-based payload sanitizer and PII masker)
- Immutable Writer Component (Spring Data JDBC append-only writer with cryptographic hash chaining)
- Retention Policy Manager (Quartz scheduler for cold S3-compatible WORM storage tiering)
- Compliance Export Facade (REST API service for external regulatory auditors)
- Apache Kafka (Event broker for asynchronous log streams)
- PostgreSQL & S3-compatible WORM Storage (Primary and cold tier storage backend)

## Relationships
- Apache Kafka streams events to Audit Log Ingestor via TCP using consumer groups with mutual TLS (mTLS).
- Audit Log Ingestor invokes Event Normalization Engine via internal function calls.
- Immutable Writer Component persists records to PostgreSQL via TLS with driver-level AES-256 encryption.
- Retention Policy Manager moves aged logs to S3-compatible WORM storage utilizing Object Lock in compliance mode.
- Compliance Export Facade serves external auditors via authenticated, rate-limited HTTPS REST endpoints.

## Technology Stack
- Java / Spring Boot: Core runtime for microservice and reactive components.
- Spring WebFlux: Reactive endpoint framework for high-throughput event ingestion.
- Jackson: JSON processing library utilized for payload sanitization and PII masking.
- Spring Data JDBC: Lightweight data access framework for append-only transactional database operations.
- Quartz Scheduler: Job scheduling library for managing 10-year retention and tiering policies.
- Apache Kafka: Distributed message broker for decoupled, asynchronous log transmission and dead-letter queue handling.
- PostgreSQL & S3: Relational database and object storage utilizing WORM compliance mode for secure, long-term data retention.
- Hardware Security Module (HSM) & OAuth2: Security infrastructure for cryptographic key management, digital signing, and token-based RBAC/ABAC authorization.

## Rationale
This decoupled reactive architecture ensures high-throughput log ingestion without impacting primary clinical workflows while strictly enforcing HIPAA and GDPR mandates. Cryptographic chaining and S3 WORM storage guarantee immutable 10-year data retention and tamper-resistance.