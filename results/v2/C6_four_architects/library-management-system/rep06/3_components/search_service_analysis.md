## Overview
The Search Service is a high-performance Python/FastAPI component within the Library Management System designed to handle catalogue item queries. It ensures low-latency search capabilities while strictly enforcing EU-only data residency constraints.

## Key Elements
* `SearchController`: FastAPI router handling incoming requests and input validation.
* `QueryBuilder`: Python module translating filters into Elasticsearch Query DSL.
* `SearchRepository`: Elasticsearch client (`elasticsearch-py`) executing index queries.
* `IndexSyncConsumer`: RabbitMQ consumer processing asynchronous domain events.
* `SearchCacheManager`: Redis client (`redis-py`) managing search result caching.
* `CircuitBreaker`: Resilience module (`tenacity`) handling failovers to fallback cache.

## Relationships
* API Gateway -> `SearchController`: Routes search requests [gRPC over mTLS]
* `SearchController` -> `SearchCacheManager`: Checks/sets search cache [In-memory / TCP]
* `SearchCacheManager` -> Redis: Reads/writes cached results [RESP over TCP]
* `QueryBuilder` -> `SearchRepository`: Translates search filters [Python Function]
* `SearchRepository` -> Elasticsearch: Executes queries [HTTP/REST over TCP]
* RabbitMQ -> `IndexSyncConsumer`: Pushes catalog change events [AMQP]

## Technology Stack
* Python & FastAPI: Core framework for asynchronous request handling and high throughput.
* Elasticsearch: Document store for fast, full-text catalog searches.
* Redis: In-memory cache for frequent queries to maintain sub-800ms latency.
* RabbitMQ: Message broker for asynchronous event-driven index synchronization.
* Tenacity: Resilience library for circuit breaker implementation.

## Rationale
This architecture uses Redis caching and optimized Elasticsearch Query DSL to guarantee the sub-800ms search latency requirement. Furthermore, strict regional configurations on local data stores ensure full compliance with EU data residency mandates.