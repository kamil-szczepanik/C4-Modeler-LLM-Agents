## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for academic and public libraries. It uses an event-driven architecture strictly confined to EU infrastructure to meet data residency and performance requirements.

## Key Elements
- Library Patrons, Librarians, Library Administrators
- Web Application (React / TypeScript)
- API Gateway (Nginx / Envoy)
- Core Services API (Node.js / NestJS Modular Monolith)
- Search Engine (Elasticsearch / OpenSearch)
- Database (PostgreSQL)
- Async Message Broker (Apache Kafka on Strimzi/Kubernetes)
- External Systems: EU Identity Provider, S3-compatible EU Object Storage, SEPA/Stripe EU API Payment Gateway, External Notification Service, Centralized SIEM / Monitoring Platform, Interlibrary Loan (ILL) Partners

## Relationships
- Web Application -> API Gateway: Routes client requests [HTTPS / REST / WebSocket]
- API Gateway -> Core Services API: Forwards authenticated requests [HTTP / gRPC]
- Core Services API -> Search Engine: Queries catalog items [HTTP / REST]
- Core Services API -> Database: Persists relational data [PostgreSQL Wire Protocol / TCP]
- Core Services API -> Async Message Broker: Publishes domain events [TCP / Kafka Protocol]
- Async Message Broker -> Centralized SIEM / Monitoring Platform: Streams metrics and audit logs [OTLP / Prometheus metrics over TLS]

## Technology Stack
- Apache Kafka: Chosen for immutable, append-only log architecture supporting 30-day compliance replay and EU data residency.
- Node.js / NestJS: Modular monolith design ensuring fast transaction processing for circulation workflows.
- PostgreSQL: Reliable relational storage for core library metadata and patron records.
- Elasticsearch / OpenSearch: Delivers sub-800ms 99th-percentile search performance for catalog items.
- Kubernetes / Strimzi: Manages EU-hosted container orchestration and multi-AZ Kafka replication.

## Rationale
This architecture uses a decoupled, event-driven message broker to ensure high responsiveness and zero data-loss resilience across circulation workflows. Hosting all components within an EU cloud region strictly enforces data residency mandates while maintaining enterprise-grade scalability.