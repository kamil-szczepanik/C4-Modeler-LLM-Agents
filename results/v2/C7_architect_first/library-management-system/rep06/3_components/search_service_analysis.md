## Overview
The Search Service provides high-performance catalogue searching for the Library Management System, meeting strict sub-second response times and EU data residency constraints. It processes physical and digital item queries securely while supporting advanced ranking and facet filtering.

## Key Elements
- **API Gateway**: Kong or Spring Cloud Gateway forwarding requests via gRPC with mTLS.
- **Search Service Container**: Python/FastAPI runtime housing search components.
- **Search API Controller**: FastAPI endpoint validating JWT claims from gRPC metadata.
- **Query Pipeline Processor**: Combines query parsing, facet/filter processing, and the relevance/ranking engine.
- **Search Repository**: `elasticsearch-py` client executing queries against Elasticsearch.
- **Index Synchronizer**: Consumes domain events from RabbitMQ to maintain index freshness.
- **Caching Layer**: In-memory Redis cache with role-based cache key segregation.
- **Elasticsearch**: Dedicated data nodes with NVMe storage in an EU-only Kubernetes cluster.
- **RabbitMQ**: Message broker with AMQP protocol, TLS/SASL, and a dead-letter queue (DLQ).

## Relationships
- API Gateway -> Search API Controller [gRPC with mTLS]
- Search API Controller -> Query Pipeline Processor [In-process]
- Query Pipeline Processor -> Search Repository [In-process / AsyncIO]
- Index Synchronizer -> Search Repository [In-process / AsyncIO]
- Index Synchronizer <- RabbitMQ Message Broker [AMQP with TLS/SASL]
- Search Repository -> Elasticsearch Cluster [Transport Layer Security with RBAC]

## Technology Stack
- **Python / FastAPI**: Chosen for asynchronous request handling and low-latency performance.
- **Elasticsearch**: Native sub-second P99 search performance over catalogued items.
- **RabbitMQ**: Asynchronous event consumption for search index synchronization.
- **Redis**: In-memory caching for frequent, non-personalized search optimization.
- **Kubernetes**: EU-only cluster deployment with Horizontal Pod Autoscalers.
- **OpenTelemetry**: Distributed tracing across gRPC boundaries.

## Rationale
This architecture uses FastAPI and Elasticsearch to guarantee P99 search latency below 800ms under peak load. Strict EU Kubernetes placement, TLS encryption, and role-based access controls satisfy regional data residency and security mandates.