## Overview
[The Billing & Claims Service manages financial transactions, insurance claims, and billing for the Clinic Management System. It ensures HIPAA/GDPR compliance, high availability, and secure external clearinghouse integrations.]

## Key Elements
- Claim Processing Engine (Java / Spring State Machine)
- Invoice & Ledger Manager (Java / Spring Data JPA)
- Clearinghouse Adapter (Java / Spring Integration)
- Outbox Publisher Component (Spring Integration / JDBC)
- CockroachDB
- RabbitMQ
- HashiCorp Vault
- Insurance Clearinghouse

## Relationships
- Claim Processing Engine -> Clearinghouse Adapter: Direct Java method calls
- Clearinghouse Adapter -> Insurance Clearinghouse: SFTP / AS2 with TLS 1.3 / AES-256
- Invoice & Ledger Manager -> CockroachDB: JDBC over TLS with ACID guarantees
- Claim Processing Engine -> Outbox Publisher: Internal transactional method call
- Outbox Publisher -> RabbitMQ: AMQP with cryptographically signed domain events
- Invoice & Ledger Manager -> HashiCorp Vault: HTTPS/REST via Spring Cloud Vault

## Technology Stack
- Java / Spring Boot: Core framework for business logic and domain processing
- CockroachDB: Distributed SQL database for multi-region ACID guarantees
- RabbitMQ: Asynchronous message broker providing outbox durability and DLQs
- HashiCorp Vault: Secret management for encryption keys and external credentials
- OpenTelemetry: Distributed tracing and telemetry collection with PHI/financial data masking

## Rationale
[This architecture uses an outbox pattern with RabbitMQ to prevent thread starvation and guarantee message delivery during external clearinghouse outages. CockroachDB and Spring Boot ensure strict distributed ACID compliance for financial ledgers and adherence to 99.99% availability requirements.]