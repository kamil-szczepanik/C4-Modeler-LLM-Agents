## Overview
[Library Management System provides catalogue and circulation services for public and academic libraries. The system ensures secure, EU-compliant asset management and sub-second patron search experiences.]

## Key Elements
- Library Patrons, Librarians / Circulation Staff, Library Administrators
- API Gateway (Nginx / Kong)
- Catalogue & Search Service (Spring Boot)
- Search Controller & Query Optimizer
- Catalog Management Component
- OpenSearch Indexing & Sync Engine
- Data Access Repository
- Event Publisher Component
- Event Broker (Apache Kafka)
- Managed Databases (PostgreSQL, OpenSearch, ClickHouse)
- OpenTelemetry Collector & Audit Logging Service

## Relationships
- API Gateway -> Catalogue & Search Service: Routes queries using gRPC and internal REST over mTLS
- Catalogue & Search Service -> Managed Databases: Queries transactional data and search indexes via private VPC
- Catalogue & Search Service -> Event Broker: Publishes catalog changes and telemetry using Kafka protocol
- OpenSearch Indexing & Sync Engine -> Event Broker: Consumes domain events for asynchronous index synchronization

## Technology Stack
- Spring Boot: Core framework for the Catalogue & Search Service leveraging Project Reactor for reactive execution
- OpenSearch & PostgreSQL: Dual data stores for high-performance search and transactional metadata within EU perimeter
- Apache Kafka: Asynchronous event broker for telemetry and data synchronization
- OpenTelemetry: Distributed tracing and audit logging for latency isolation and compliance
- Resilience4j: Circuit breaking for fault tolerance on event publishing

## Rationale
[The reactive Spring Boot architecture with OpenSearch and dedicated caching layers directly satisfies the sub-800ms search latency requirement. Strict mTLS, TLS 1.3, and isolated managed storage within a private VPC guarantee adherence to EU-only data residency and security mandates.]