## Overview
The Catalog & Search component provides high-performance, sub-second product discovery and faceted filtering for the Online Bookstore. It is architected to support 1 million monthly active users globally across three AWS regions while maintaining strict availability.

## Key Elements
- Shoppers & Store Staff (Users)
- API Gateway (Amazon API Gateway)
- Search Controller & Facade (Spring Boot)
- Catalog Management Service (Spring Boot)
- Search & Indexing Engine (Amazon OpenSearch)
- Sync Worker (Spring Boot / AWS Lambda)
- Search Analytics Collector (Spring Boot)
- Primary Database (Amazon RDS PostgreSQL)
- Event Bus & Stream (Amazon EventBridge, Amazon Kinesis Data Streams)

## Relationships
- API Gateway -> Search Controller & Facade: Routes internal traffic via [gRPC]
- Catalog Management Service -> Amazon RDS PostgreSQL: Persists source of truth via [JDBC / SQL]
- Catalog Management Service -> Sync Worker: Publishes mutations via [Amazon EventBridge (JSON)]
- Sync Worker -> Search & Indexing Engine: Updates indices via [HTTPS / REST]
- Search Controller & Facade -> Search Analytics Collector: Dispatches telemetry via [Spring ApplicationEvent]
- Search Analytics Collector -> Amazon Kinesis Data Streams: Streams metrics via [HTTPS / AWS SDK]

## Technology Stack
- Spring Boot: Powers microservices for low-latency business logic and controllers.
- Amazon OpenSearch: Delivers full-text search, typo tolerance, and cross-cluster replication.
- Amazon RDS PostgreSQL: Ensures reliable relational data storage for catalog metadata.
- Amazon EventBridge & Kinesis: Handle asynchronous event-driven sync and telemetry streaming.

## Rationale
This decoupled architecture separates reads from writes, enabling sub-second search latencies that protect conversion rates. Multi-region replication and asynchronous telemetry collection ensure high availability (99.95%) and scalability without performance degradation.