## Overview
The Circulation & Core Service handles transactional loan states, fine management, and patron account workflows for the Library Management System. It guarantees ACID compliance, GDPR data residency, and high availability during peak traffic periods.

## Key Elements
- **Circulation & Core Service**: Java, Spring Boot container for core logic.
- **Circulation Engine Component**: Manages checkouts, renewals, and holds.
- **Fine & Fee Manager Component**: Handles financial ledgers and payment integrations.
- **Patron Account Coordinator Component**: Manages circulation blocks and account states.
- **PostgreSQL (EU Instance)**: EU-hosted relational database with primary-replica streaming.
- **Payment Gateway**: External system for processing fines and fees.
- **Notification Dispatcher**: Python, FastAPI service via RabbitMQ/Kafka.
- **Audit Logging Container**: Node.js container for immutable audit trails.

## Relationships
- **Circulation Engine Component** -> **PostgreSQL**: Persists transactional loan states via JDBC over TLS 1.3 (strict ACID).
- **Fine & Fee Manager Component** -> **Payment Gateway**: Processes financial settlements via REST over mTLS (TLS 1.3).
- **Fine & Fee Manager Component** -> **Notification Dispatcher**: Publishes asynchronous outbox events via AMQP/Kafka over TLS.
- **Patron Account Coordinator Component** -> **Audit Logging Container**: Dispatches immutable audit trails via gRPC over mTLS.
- **Internal Components** -> **Internal Components**: Communicates via in-memory Spring Application Events.

## Technology Stack
- **Java & Spring Boot**: Core framework for robust enterprise transaction management.
- **Spring `@Transactional`**: Enforces strict serializable/repeatable read isolation levels in PostgreSQL.
- **PostgreSQL**: Stores transactional data with primary-replica streaming replication and column-level PII encryption.
- **Resilience4j**: Implements circuit breakers on the Payment Gateway REST client to prevent thread-pool exhaustion.
- **Spring Security**: Enforces RBAC and cryptographic JWT validation.

## Rationale
This architecture ensures strict ACID compliance and high throughput for critical library workflows while strictly enforcing EU data residency. Decoupling external payment calls via the Outbox Pattern protects system availability during peak traffic.