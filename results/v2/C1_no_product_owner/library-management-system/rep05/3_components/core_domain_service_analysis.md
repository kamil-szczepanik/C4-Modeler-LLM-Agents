## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals, adhering strictly to EU-only data residency.

## Key Elements
- Users: Patron, Librarian / Staff
- External Systems: Authentication Provider, External Payment Gateway, National Library Registry, Notification Service
- Containers: Web App (React/TypeScript, Nginx), API Gateway (Kong/Spring Cloud Gateway), Core Domain Service (Java/Spring Boot), Search Service (Elasticsearch), Database (PostgreSQL), Async Event Broker (Apache Kafka), Background Worker
- Components: Catalog Management Component, Circulation Component, Fine & Fee Component, Patron Management Component

## Relationships
- API Gateway -> Core Domain Service: Routes domain API requests [gRPC/Internal REST over mTLS]
- Catalog Management Component -> Search Service: Publishes change-data-capture (CDC) events [Apache Kafka (AMQP/TLS 1.3)]
- Core Domain Service -> Database: Reads and writes relational data [JDBC/TLS 1.3 with mTLS]
- Core Domain Service -> External Payment Gateway: Processes fines and fees [REST/HTTPS with mTLS and TLS 1.3]
- Core Domain Service -> Authentication Provider: Validates tokens [OIDC/HTTPS]

## Technology Stack
- Java/Spring Boot: Implements the Core Domain Service as a modular monolith for domain separation.
- PostgreSQL: Stores relational data, enforcing EU-only data residency and application-level PII encryption.
- Apache Kafka: Handles asynchronous integration events and CDC to maintain search performance.
- Spring Security: Enforces method-level ABAC and zero-trust validation across internal components.
- Resilience4j: Implements circuit breakers for external payment gateway calls.

## Rationale
This architecture uses an asynchronous CDC pattern with Kafka to meet the strict 99th-percentile search response time under 800 ms without database lock contention. A modular monolith design combined with EU-hosted infrastructure ensures full compliance with data residency constraints.