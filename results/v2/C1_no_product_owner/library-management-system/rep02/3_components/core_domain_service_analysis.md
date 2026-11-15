## Overview
## Overview
- Library Management System for cataloging items, managing circulation, and self-service portals.
- Built with strict EU-only data residency and 99th-percentile search response under 800 ms.

## Key Elements
- Web Application (React, TypeScript)
- API Gateway (Spring Cloud Gateway / Envoy)
- Core Domain Service (Java / Spring Boot)
- Search Service (Java / Elasticsearch / OpenSearch)
- Notification Service (Node.js / TypeScript)
- PostgreSQL Database (AES-256 encryption)
- Managed Event Bus (Kafka / EventBridge)

## Relationships
- API Gateway -> Core Domain Service: Routes internal service requests [gRPC over mTLS]
- Core Domain Service -> PostgreSQL Database: Reads and writes transactional data [JDBC / TLS]
- Core Domain Service -> Managed Event Bus: Publishes and consumes domain events [TLS-encrypted TCP with SASL/OAuth2]

## Technology Stack
- Java / Spring Boot: Core business and transactional logic framework
- PostgreSQL: Relational database with AES-256 storage and column-level PII encryption
- Kafka / EventBridge: Managed event bus for asynchronous domain events
- React / TypeScript: Frontend web application framework

## Rationale
- Decoupled services and managed event bus ensure high performance and strict EU data residency.
- Robust containerization and secure protocols meet stringent performance and security constraints.