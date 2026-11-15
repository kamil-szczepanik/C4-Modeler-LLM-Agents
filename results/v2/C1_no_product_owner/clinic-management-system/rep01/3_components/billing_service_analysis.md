## Overview
The Billing Service is a core container within the Clinic Management System designed to handle billing operations and insurance claim submissions. It ensures secure, compliant, and highly available financial processing across hybrid cloud environments.

## Key Elements
- Billing API Controller (Spring MVC)
- Claim Management Engine (Spring Service)
- Insurance Integration Adapter (Apache Camel / Spring Integration)
- Billing Data Repository (Spring Data JPA / PostgreSQL)
- External Insurance Clearinghouses
- Message Broker Container (Apache Kafka)

## Relationships
- Billing API Controller -> Claim Management Engine: Local Java method invocations
- Claim Management Engine -> Billing Data Repository: TLS-secured JDBC for atomic outbox writes
- Claim Management Engine -> Message Broker Container: TLS/mTLS and SCRAM-SHA-512 event publishing
- Insurance Integration Adapter -> External Insurance Clearinghouses: HTTPS with mTLS, OAuth2, and egress proxy filtering

## Technology Stack
- Spring Boot: Core framework for microservices and API controllers
- Apache Camel: Enterprise integration patterns for clearinghouse retries and dead-letter queues
- PostgreSQL & Hibernate/JPA: Relational persistence with automated table partitioning for 10-year retention
- Apache Kafka: Event streaming implementing the transactional outbox pattern
- HashiCorp Vault / AWS KMS: HSM-backed key management for field-level encryption

## Rationale
This architecture guarantees 99.99% availability and strict data compliance via active-read/write replication, transactional outboxing, and rigorous hybrid boundary security controls. It isolates third-party integrations and ensures encrypted, auditable financial transactions.