## Overview
The Library Management System provides physical/digital cataloging, circulation management, and self-service portals. It uses a containerized modular monolith deployed on Kubernetes, strictly enforcing EU data residency.

## Key Elements
- **Users**: Library Patrons, Library Staff, Library Administrators
- **Core Services API**: Node.js / NestJS Modular Monolith
- **Internal Modules**: Catalog Module, Circulation Module, Fines & Fees Module, Search Orchestrator Module, Data Governance Interceptor
- **Data & Storage**: PostgreSQL (Database), Elasticsearch / OpenSearch (Search Engine), S3-compatible EU Object Storage
- **Infrastructure & Integration**: Nginx / Envoy (API Gateway), RabbitMQ / Apache Kafka (Async Message Broker), SEPA / Stripe EU API Payment Gateway, Centralized SIEM / Monitoring Platform

## Relationships
- API Gateway -> Core Services API: Forwards routed requests [REST/gRPC]
- Core Services API -> PostgreSQL: Reads/writes transactional data [TCP]
- Core Services API -> OpenSearch: Queries/indexes search data [TCP]
- Core Services API -> RabbitMQ / Apache Kafka: Publishes/consumes async messages [AMQP]
- Core Services API -> SEPA / Stripe EU API Payment Gateway: Processes fines and fees [REST API over HTTPS]
- Core Services API -> Centralized SIEM / Monitoring Platform: Sends audit logs and telemetry [HTTPS/TLS 1.3]

## Technology Stack
- **Backend**: Node.js / NestJS for the modular monolith architecture
- **Database**: PostgreSQL with TypeORM for relational data storage
- **Search**: OpenSearch / Elasticsearch for low-latency search (<800ms SLA)
- **Deployment**: Kubernetes with containerized workloads and Istio/Envoy gateway
- **Observability**: OpenTelemetry for request tracing and structured JSON logging

## Rationale
The modular monolith structure supports rapid feature delivery while isolating high-churn domain logic. Containerizing on Kubernetes with strict EU data residency enforcement guarantees both high availability and regulatory compliance.