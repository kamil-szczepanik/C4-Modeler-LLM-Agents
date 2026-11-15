## Overview
The Catalog & Search Service provides high-performance item discovery for the Library Management System. It delivers sub-800ms search responses while enforcing strict EU data residency constraints.

## Key Elements
- **Search API Controller**: Spring MVC controller handling gRPC requests from the Core API Gateway.
- **Search Query Engine**: Spring Data Elasticsearch component executing faceted search and auto-suggestion queries with typo tolerance.
- **Catalog Indexer**: Spring Integration and RabbitMQ Client consuming item mutation events via AMQP over TLS.
- **Elasticsearch Cluster**: Stateful search backend deployed via Kubernetes StatefulSets with persistent volumes.
- **RabbitMQ**: Message broker managing event synchronization and Dead Letter Queues (DLQ).

## Relationships
- **Core API Gateway -> Search API Controller**: Routes search queries using [gRPC].
- **Search API Controller -> Search Query Engine**: Invokes methods via internal [Java interface].
- **Catalog Indexer -> Elasticsearch Cluster**: Synchronizes index data using [HTTP/REST over TLS].
- **RabbitMQ -> Catalog Indexer**: Publishes mutation events using [AMQP over TLS].
- **Search Query Engine -> Centralized Observability Platform**: Ships telemetry and metrics using [gRPC].

## Technology Stack
- **Spring Boot**: Core application framework chosen for rapid enterprise service development.
- **Elasticsearch**: Dedicated search engine selected to guarantee p99 search performance under 800 ms.
- **Spring Data Elasticsearch**: Simplifies integration and query translation for Elasticsearch DSL.
- **RabbitMQ**: Asynchronous message broker providing reliable event consumption and DLQ error handling.
- **Kubernetes StatefulSets**: Orchestrates stateful Elasticsearch nodes with persistent storage.

## Rationale
This architecture uses Elasticsearch and Spring Boot to meet strict sub-800ms search performance requirements. Stateful Kubernetes deployment and localized messaging ensure full compliance with EU-only data residency constraints.