## Overview
The Library Management System provides item cataloging, circulation management, and self-service portals with strict EU data residency. The architecture integrates an enterprise search engine to deliver high-performance item discovery.

## Key Elements
- Self-Service Patrons & Library Staff (Users)
- API Gateway (TLS termination and IAM validation)
- Core Business Services (Decoupled microservices)
- Search Engine Container (Elasticsearch/OpenSearch)
- Database Container (PostgreSQL)
- Async Event Broker Container (Apache Kafka or RabbitMQ)
- Shared Caching Container (Redis)
- Centralized Audit and Logging System

## Relationships
- Self-Service Patrons & Library Staff -> API Gateway: Accesses system [HTTPS]
- Core Business Services -> Search Engine Container: Queries search index [HTTP/REST]
- Database Container -> Async Event Broker Container: Propagates domain events [AMQP/TCP]
- Async Event Broker Container -> Search Engine Container: Ingests asynchronous updates [HTTP/REST]
- Core Business Services -> Shared Caching Container: Fallback query caching [RESP]

## Technology Stack
- Elasticsearch/OpenSearch: Selected for Search Engine Container to achieve < 800 ms 99th-percentile search performance (R-05).
- Apache Kafka/RabbitMQ: Decouples database updates from search indexing via event-driven architecture.
- Redis: Provides fallback caching and resilience against search cluster degradation.
- PostgreSQL: Serves as the primary persistent data store for library records.

## Rationale
This decoupled, event-driven architecture guarantees low-latency search capabilities while isolating EU-only data residency constraints within the search and storage infrastructure. Built-in caching fallbacks and circuit breakers ensure resilience and performance under high query loads.