## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service patron portals. It incorporates a dedicated Search Indexer container to guarantee sub-800ms search performance under strict EU data residency constraints.

## Key Elements
- **Search Indexer Container**: Houses internal components for high-performance catalogue searching and ingestion.
- **Indexing Worker Component**: Python/Celery worker handling asynchronous payload sanitization and bulk-writes.
- **Index Management API Component**: Python FastAPI service exposing administrative health checks and re-index triggers.
- **Elasticsearch Engine Component**: Elasticsearch v8 cluster providing inverted indices with AES-256 encryption at rest.
- **Message Broker**: RabbitMQ instance managing asynchronous ingestion queues with AMQP over TLS 1.3.
- **Library Staff & Administrators**: Authenticated users accessing monitoring dashboards via JWT role-based access control.

## Relationships
- Message Broker (RabbitMQ) -> Indexing Worker Component: Consumes catalogue events [AMQP over TLS 1.3]
- Indexing Worker Component & Index Management API Component -> Elasticsearch Engine Component: Bulk-writes and searches [HTTP/REST over mTLS]
- Web Application Container -> Index Management API Component: Exposes administrative controls [HTTPS/JSON with JWT RBAC]

## Technology Stack
- **Python / Celery / FastAPI**: Chosen for the Indexing Worker and Index Management API to provide rapid asynchronous processing and clean API design.
- **Elasticsearch v8**: Selected for its proven capability to deliver sub-800ms search latency across massive catalogues.
- **RabbitMQ**: Deployed to decouple core cataloguing from search ingestion and maintain high system resilience.
- **TLS 1.3 / mTLS / AES-256**: Enforced across all internal channels and storage to satisfy strict EU data residency and security mandates.

## Rationale
This architecture decouples ingestion, search execution, and administrative controls to consistently achieve the required sub-800ms search response times under heavy workloads. Strict security boundaries, EU-pinned persistent volumes, and asynchronous messaging ensure full compliance with regional regulations while granting library staff autonomous oversight.