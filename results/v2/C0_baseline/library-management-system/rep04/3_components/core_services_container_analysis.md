## Overview
Core Services Container provides modular backend logic, RBAC enforcement, and data management for the Library Management System. It handles circulation transactions and EU-compliant data processing for patrons and librarians.

## Key Elements
- **Core Services Container**: Java/Spring Boot modular monolith deployed on Kubernetes.
- **Security & RBAC Module**: Spring Security component handling local JWT validation and least-privilege checks.
- **Catalog & Circulation Module**: Spring Data JPA component managing items, loans, and HikariCP connection pools.
- **Audit & Event Dispatcher**: Spring Events and Kafka client emitting signed audit/domain events.
- **Database**: PostgreSQL storing transactional data with column-level PII encryption.
- **External Dependencies**: API Gateway, External IdP, Search Container, Message Broker, Payment Gateway, Notification Service, Audit Container, HashiCorp Vault.

## Relationships
- **API Gateway -> Core Services Container**: Routes API traffic [gRPC/REST over mTLS]
- **Security & RBAC Module -> External IdP**: Fetches cached public keys for local JWT validation [HTTPS]
- **Catalog & Circulation Module -> Database**: Executes transactional reads/writes [JDBC over mTLS with `sslmode=verify-full`]
- **Core Services Container -> Search Container**: Queries catalog index [mTLS]
- **Audit & Event Dispatcher -> Message Broker**: Publishes signed audit and domain events [TCP/mTLS]
- **Core Services Container -> Payment Gateway**: Processes financial transactions [HTTPS/REST with certificate pinning]
- **Core Services Container -> Notification Service**: Dispatches alerts [HTTPS/SMTP]

## Technology Stack
- **Java 17 / Spring Boot**: Foundation for the modular monolith, ensuring rapid feature delivery.
- **Spring Security**: Implements method-level RBAC (`@PreAuthorize`) and cryptographic JWT validation.
- **Spring Data JPA / HikariCP**: Manages relational persistence with partitioned connection pools to prevent resource starvation.
- **Kubernetes & Resilience4j**: Orchestrates container deployment with liveness/readiness probes and circuit breakers for external third-party calls.
- **HashiCorp Vault**: Secures ephemeral secrets via CSI volume mounts, avoiding plaintext environment variables.

## Rationale
The modular monolith architecture balances rapid delivery for circulation features with strict EU data residency constraints. Internal module boundaries and connection partitioning ensure performance meets the <800ms P99 search requirement under concurrent self-checkout spikes.