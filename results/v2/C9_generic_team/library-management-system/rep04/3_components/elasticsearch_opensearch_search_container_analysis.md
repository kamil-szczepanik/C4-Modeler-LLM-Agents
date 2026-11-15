## Overview
The Library Management System provides cataloging, circulation, and self-service portals for academic and public libraries. The search infrastructure relies on Elasticsearch/OpenSearch to achieve high-performance querying under strict EU data residency constraints.

## Key Elements
* Elasticsearch / OpenSearch Search Container: Core search engine
* Redis Distributed Cache Container: Caching layer
* RabbitMQ / Kafka Message Broker: Asynchronous event pipeline
* Catalog Management & Circulation Containers: Spring Boot microservices emitting domain events
* Log/Metrics Collector Agent: OTel Collector / Fluentd observability agent

## Relationships
* Catalog Management -> RabbitMQ / Kafka: Publishes domain events [TCP]
* Circulation -> RabbitMQ / Kafka: Publishes domain events [TCP]
* RabbitMQ / Kafka -> Elasticsearch / OpenSearch: Asynchronous index synchronization [TCP]
* Redis Distributed Cache Container -> Elasticsearch / OpenSearch: Read-through caching pattern [TCP]
* Client / User Agent -> API Gateway Container: Search requests [HTTPS]

## Technology Stack
* Elasticsearch / OpenSearch: Decouples search to meet sub-800ms P99 performance requirements (R-05)
* Redis: Read-through cache to offload repetitive queries and reduce latency
* RabbitMQ / Kafka: Asynchronous message broker for decoupled index synchronization
* Index Aliases: Blue-green zero-downtime reindexing strategy
* Index Lifecycle Management (ILM): Automated tiering for EU-hosted persistence volumes

## Rationale
This architecture guarantees high-performance search responses under 800 ms (R-05) by decoupling workloads via asynchronous synchronization and caching. It maintains strict EU data residency and system resilience through resource governance and automated index management.