## Overview
The Clinic Management System is a hybrid cloud clinical IT platform designed to manage patient admissions, electronic medical records, appointments, and billing with 99.99% availability. It ensures strict HIPAA and GDPR compliance while maintaining sub-second performance for clinical operations.

## Key Elements
- **EMR Facade / Controller**: Handles incoming gRPC requests and schema validation.
- **Policy Enforcement Component**: Evaluates Attribute-Based Access Control (ABAC) rules.
- **Clinical Record Manager**: Manages core business logic and ACID transactions.
- **Audit Trail Interceptor**: Signs and logs PHI access for compliance.
- **KMS Client Adapter**: Handles envelope encryption and key management with resilience fallbacks.
- **PostgreSQL Database**: Persistent storage utilizing PgBouncer connection pooling and column-level encryption.

## Relationships
- API Gateway -> EMR Facade: Routes electronic medical records requests [gRPC with Istio mTLS and propagated JWTs]
- EMR Facade -> Policy Enforcement Component -> Clinical Record Manager: Processes and authorizes requests [In-process Spring Security filter/aspect and method calls]
- Clinical Record Manager -> KMS Client Adapter: Encrypts sensitive PHI fields [gRPC/HTTPS]
- Clinical Record Manager -> PostgreSQL Database: Persists clinical records [JDBC over TLS with AES-256]
- Clinical Record Manager -> Audit Trail Interceptor -> Apache Kafka: Publishes cryptographically signed compliance audit events [In-process eventing and Kafka producer]

## Technology Stack
- **Java Spring Boot**: Core framework for robust enterprise service development and sub-second P95 performance.
- **Spring gRPC / Protobuf**: High-performance internal communication protocol with strict schema validation.
- **HashiCorp Vault & AWS KMS**: Centralized cloud and on-prem key management for envelope encryption and dynamic database credentials.
- **Resilience4j**: Circuit breaking and fallback caching for data-encryption-keys (DEKs) to maintain availability.
- **OpenTelemetry**: Distributed tracing across all internal components.
- **Apache Kafka**: Asynchronous, decoupled compliance audit logging.

## Rationale
This architecture uses an active-active hybrid setup across `on-prem-k8s` and `eu-central-1` to guarantee 99.99% availability and meet strict 10-year data retention rules. Centralized KMS integration, ABAC authorization, and cryptographically signed audit trails satisfy HIPAA and GDPR security mandates without compromising sub-second EMR performance.