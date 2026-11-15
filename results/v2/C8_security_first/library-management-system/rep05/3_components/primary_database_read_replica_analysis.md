## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within EU data residency constraints. It guarantees sub-800ms search performance and secure transactional data management.

## Key Elements
- Patrons & Library Staff
- Patron Self-Service Portal (Web/Mobile App)
- Staff Management Console (Web)
- Search & Catalogue Service (Java / Spring Boot, Elasticsearch)
- Circulation & Loan Engine, Analytics & Reporting Service (Python / FastAPI, Pandas)
- Notification Engine (Go)
- Primary Database & Read-Replica (PostgreSQL, PgBouncer, Patroni)
- Message Broker (RabbitMQ / Kafka)
- EU-bound API Gateway, Payment Gateway, Digital Content Providers, Inter-Library Loan Networks

## Relationships
- Patron Self-Service Portal -> PgBouncer: Queries and updates data [SQL over TLS 1.3 / mTLS]
- Search & Catalogue Service -> PostgreSQL Read-Replica: Fetches catalogue data [SQL over TLS 1.3 via PgBouncer port 6433]
- Circulation & Loan Engine -> PostgreSQL Primary: Executes transactions [SQL over TLS 1.3 via PgBouncer port 6432]
- Analytics & Reporting Service -> PostgreSQL Read-Replica: Queries reporting data [SQL over TLS 1.3]
- PostgreSQL Primary -> PostgreSQL Read-Replica: Streams replication [Streaming Replication in asynchronous mode]

## Technology Stack
- PostgreSQL: Core transactional storage with AES-256 encryption at rest and column-level PII encryption.
- PgBouncer: Connection pooling sidecar routing traffic via ports 6432 (writes) and 6433 (reads).
- Patroni: Automated leader election and health checking for PostgreSQL high availability.
- CloudNativePG Operator: Kubernetes-based deployment for EU data residency and automated management.
- HashiCorp Vault: Dynamic database credential injection via automated sidecars.
- pgaudit: Database-level audit logging for GDPR compliance.

## Rationale
This architecture uses streaming read-replicas and PgBouncer connection pooling to offload read traffic, guaranteeing the 99th-percentile search latency under 800 ms. Strict VPC isolation, mTLS, and EU-bound managed operators satisfy regional data residency and GDPR security constraints.