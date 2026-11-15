## Overview
The Clinic Management System is a clinical IT platform managing patient records, scheduling, and billing for healthcare providers. It features a distributed hybrid architecture ensuring high availability, strict HIPAA/GDPR compliance, and sub-second EMR performance.

## Key Elements
- **EMR Rest Controller Layer**: Spring MVC component handling REST/gRPC endpoints, input validation, and OAuth2/JWT security context.
- **Clinical Record Manager**: Spring Service containing core domain logic, utilizing resilience4j circuit breakers and HashiCorp Vault.
- **Audit Trail Engine**: Spring AOP/Spring WebFlux component with a reactive outbox processor and cryptographic signing pipeline.
- **Data Access Repository**: Spring Data JPA / Hibernate interface utilizing PostgreSQL read-replicas.
- **Infrastructure Services**: Istio service mesh, HashiCorp Vault, Kafka/RabbitMQ, WORM-compliant S3/MinIO, and Jaeger/OpenTelemetry.

## Relationships
- EMR Rest Controller Layer -> Clinical Record Manager: In-process method calls [Java/Spring Beans]
- Clinical Record Manager -> Data Access Repository: Encrypted SQL queries [Encrypted SQL]
- Clinical Record Manager -> HashiCorp Vault: Dynamic secret retrieval [HTTPS/TLS 1.3 with Istio/SPIFFE workload identity]
- Audit Trail Engine -> Kafka/RabbitMQ: Asynchronous event publishing [TLS 1.3]
- Audit Trail Engine -> WORM-compliant S3 / MinIO: Immutable audit log archival [HTTPS/TLS 1.3]

## Technology Stack
- **Java / Spring Boot**: Core container runtime for enterprise reliability and high performance.
- **Spring WebFlux / Project Reactor**: Powers the reactive outbox processor for high-throughput asynchronous operations.
- **PostgreSQL with Patroni**: Relational persistence layer ensuring high availability and ACID compliance.
- **HashiCorp Vault**: Manages encryption keys and dynamic secrets for field-level PHI protection.
- **Kafka / RabbitMQ**: Decouples services to guarantee non-blocking audit logging and high availability.
- **WORM-compliant S3 / MinIO**: Provides immutable object storage meeting the 10-year data retention mandate.

## Rationale
This architecture uses an asynchronous outbox pattern and reactive processing to decouple audit logging, protecting 99.99% availability and <1s P95 latency targets. Field-level encryption, SPIFFE/Istio workload identity, and WORM storage ensure strict HIPAA and GDPR compliance across the hybrid cloud deployment.