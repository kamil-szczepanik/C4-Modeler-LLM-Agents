## Overview
The Search Service is a high-performance C4 component of the Library Management System providing sub-800ms P99 search responses. It indexes and queries physical and digital catalogue items while strictly enforcing EU data residency.

## Key Elements
- Search API Controller (FastAPI, Pydantic)
- Query Builder Component (Python)
- Index Synchronizer Component (aiokafka)
- Search Client Component (elasticsearch-py async client)
- Elasticsearch (External Database)
- API Gateway
- Async Event Broker (Apache Kafka)

## Relationships
- API Gateway -> Search API Controller: Routes search requests [gRPC/REST]
- Async Event Broker -> Index Synchronizer: Consumes CDC and domain events [TCP/Kafka Protocol]
- Search API Controller -> Query Builder: Delegates request parsing [In-process]
- Query Builder -> Search Client: Executes compiled queries [In-process]
- Index Synchronizer -> Search Client: Updates indices [In-process]
- Search Client -> Elasticsearch: Executes queries and bulk updates [TCP/HTTP, port 9200]

## Technology Stack
- Python with FastAPI: Chosen for high-throughput asynchronous request handling and non-blocking I/O.
- Elasticsearch: Selected for low-latency indexing and complex query capabilities.
- aiokafka: Utilized for efficient asynchronous event consumption from Kafka.
- Pydantic: Implemented for robust request validation and serialization.
- `elasticsearch-py` async client: Used to maintain non-blocking execution across FastAPI's event loop.

## Rationale
Decomposing the Search Service into decoupled read and mutation components ensures the system meets the strict <800ms P99 search latency requirement. Asynchronous ingestion and optimized Elasticsearch DSL querying preserve performance under load while adhering to EU-only data residency constraints.