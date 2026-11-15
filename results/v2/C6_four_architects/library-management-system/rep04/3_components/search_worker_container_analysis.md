## Overview
[Component-level architecture for the Search Worker Container within the Library Management System, designed to synchronize database updates to search indices.]

## Key Elements
- CDC Source Connector Component (Debezium Embedded, Java/Quarkus)
- Search Transformer/Indexer Component (Apache Camel, Java/Quarkus)
- Local DLQ/Retry Handler Component (Camel Error Handler)
- Metrics Exporter Component (Micrometer)
- External Dependencies: PostgreSQL Database, RabbitMQ Message Broker, Elasticsearch Search Container

## Relationships
- PostgreSQL -> CDC Source Connector: Tails database Write-Ahead Logs [PostgreSQL Replication Protocol]
- CDC Source Connector -> Message Broker: Publishes raw change events [AMQP]
- Message Broker -> Search Transformer/Indexer: Consumes batched sync payloads [AMQP]
- Search Transformer/Indexer -> Search Container: Bulk indexes documents [HTTPS/REST]
- Local DLQ/Retry Handler -> Message Broker: Routes permanently failed payloads to DLX [AMQP]
- Metrics Exporter -> Monitoring: Exposes Prometheus-compatible metrics [HTTP]

## Technology Stack
- Java/Quarkus: Runtime platform for high throughput and fast startup
- Debezium Embedded: Native, low-latency PostgreSQL replication log-tailing
- Apache Camel: Handles schema mapping, batching, and circuit-broken bulk indexing
- Micrometer: Exposes operational metrics to track replication lag
- TLS 1.3: Secures all data in transit within the EU data boundary

## Rationale
[Asynchronous event-driven batching and local dead-letter handling protect the primary database and Elasticsearch from overload, ensuring sub-800ms search responses. All components operate exclusively within the EU to comply with strict data residency constraints.]