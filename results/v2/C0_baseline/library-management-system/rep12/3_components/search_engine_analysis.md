## Overview
The Search Engine component of the Library Management System provides instant, secure catalogue discovery for physical and digital items. It ensures high-performance searching, faceted navigation, and zero-results tracking while adhering to strict EU data residency constraints.

## Key Elements
- Query Processing Component (Elasticsearch Analysis & Query DSL, Synonym Token Filter, Aggregation Engine)
- Indexing & Synchronization Component (AMQP/Kafka Consumer)
- Search Analytics & Logging Component (HTTPS/TLS)
- 3-node Elasticsearch Cluster (Kubernetes, Frankfurt/AWS)
- Core Domain Services & API Gateway
- Async Event Bus (RabbitMQ / Apache Kafka)
- Logging & APM System

## Relationships
- Core Domain Services -> Query Processing Component [mTLS/REST]: Delivers search queries, faceted results, and promotional boosting rules
- Async Event Bus -> Indexing & Synchronization Component [SASL/SCRAM over TLS]: Consumes asynchronous catalogue updates
- Search Analytics & Logging Component -> Logging & APM [HTTPS/TLS]: Flushes search telemetry, zero-result events, and audit logs

## Technology Stack
- Elasticsearch: Core search and aggregation engine for sub-800ms P99 queries
- Elasticsearch Document- and Field-Level Security (FLS/DLS): Enforces query-level RBAC for patrons and staff
- AES-256 & EU-hosted HSM: Secures data at rest with strict key management
- Prometheus & OpenTelemetry: Scrapes cluster health metrics and distributed tracing

## Rationale
This architecture uses a dedicated, clustered search engine with decoupled ingestion and aggressive memory tuning to consistently achieve sub-800ms P99 responses. Robust security controls and local NVMe storage guarantee compliance with EU-only data residency requirements.