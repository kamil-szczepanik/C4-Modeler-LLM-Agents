## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within EU data residency constraints. The Search Engine component delivers high-performance item discovery meeting 99th-percentile response times under 800ms.

## Key Elements
- Library Patrons, Librarians, Library Administrators
- Core Services API (Node.js / NestJS)
- Search Engine Container (OpenSearch / Elasticsearch)
- Query Parser & Router Component
- Index & Ranking Component
- Ingestion & Synchronization Component
- Suggest & Spellcheck Component
- Search Analytics Collector Component
- Async Message Broker (RabbitMQ / Apache Kafka)
- Centralized SIEM / Monitoring Platform

## Relationships
- Core Services API -> Query Parser & Router: Submits search DSL/queries [HTTP/REST over TCP]
- Async Message Broker -> Ingestion & Synchronization Component: Delivers catalogue updates [AMQP / Kafka Protocol]
- Query Parser & Router -> Search Analytics Collector: Dispatches search query logs [In-Memory Queue]
- Search Analytics Collector -> Async Message Broker: Emits search telemetry [AMQP / Kafka Protocol]
- Search Engine -> Centralized SIEM / Monitoring Platform: Exposes Prometheus metrics and slow-query logs [HTTPS / Prometheus Scrape]

## Technology Stack
- OpenSearch / Elasticsearch: Chosen for high-performance faceted search, relevance tuning, and built-in Suggester API
- RabbitMQ / Apache Kafka: Decouples write spikes and telemetry logging from search latency to protect the 800ms SLA
- Prometheus: Collects cluster health, JVM heap usage, and slow-query logs for operational monitoring
- Persistent NVMe Storage: Deployed across 3 availability zones in the EU region to guarantee data residency and prevent split-brain scenarios

## Rationale
Decomposing the search container into isolated components with asynchronous ingestion and telemetry ensures strict adherence to the 800ms performance SLA. Circuit breakers, resource quotas, and EU-only NVMe storage guarantee system stability, query-cost governance, and regional data compliance.