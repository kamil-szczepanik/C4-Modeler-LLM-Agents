## Overview
The Staff Management API is a core container within the Library Management System that handles cataloging, circulation, and administrative operations for staff. It processes internal requests and coordinates with external services while adhering to strict EU data residency mandates.

## Key Elements
* **Staff Management API (Java/Spring Boot)**: Main container housing circulation and cataloging logic.
* **Circulation Controller & Service**: Handles loans, fines, and fast-path check-outs.
* **Catalog Management Service**: Manages physical and digital item cataloging and bulk imports.
* **Payment & ILL Client Adapters**: Encapsulates outbound traffic to external systems.
* **Data Masking Component**: Strips or pseudonymizes patron PII for cross-border transit.
* **Bulk Processing & Asynchronous Worker Component**: Offloads heavy tasks to messaging brokers.
* **External Systems**: Managed PostgreSQL, Managed Apache Kafka, External Payment Gateway, Interlibrary Loan (ILL) Network, External Identity Provider (IdP), and Observability Platform & SIEM.

## Relationships
* **API Gateway -> Staff Management API**: Routes staff traffic via gRPC over mTLS.
* **Staff Management API -> Managed PostgreSQL**: Reads and writes transactional data using PostgreSQL Protocol and Spring Data JPA.
* **Staff Management API -> Managed Apache Kafka**: Publishes asynchronous events using AMQP/Kafka protocols.
* **Staff Management API -> External Payment Gateway**: Processes library payments via REST/JSON over TLS 1.3.
* **Staff Management API -> External Identity Provider (IdP)**: Authenticates staff using OpenID Connect (OIDC) / OAuth 2.0.
* **Staff Management API -> Interlibrary Loan (ILL) Network**: Performs cross-border searches via HTTPS/REST.
* **Staff Management API -> Observability Platform & SIEM**: Streams metrics and traces using OpenTelemetry / Prometheus over TLS.

## Technology Stack
* **Java / Spring Boot**: Chosen for enterprise maturity, robust ecosystem, and concurrency management.
* **Spring Data JPA**: Provides secure, parameterized database interactions.
* **Resilience4j**: Implements circuit breakers within adapters to prevent cascading failures.
* **Managed OpenSearch/Elasticsearch & PostgreSQL**: Hosted exclusively in the EU to meet strict data residency and encryption (AES-256) requirements.
* **Managed Apache Kafka**: Enables asynchronous decoupling for high-throughput bulk catalog operations.

## Rationale
This architecture combines Spring Boot services with asynchronous Kafka messaging to meet high-performance search and bulk-processing needs. Built-in data masking components and strict EU hosting ensure full compliance with GDPR and data residency constraints.