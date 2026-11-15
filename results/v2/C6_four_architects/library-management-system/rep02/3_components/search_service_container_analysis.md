## Overview
The Search Service Container is a high-performance component of the Library Management System designed to handle catalogue item searches. It delivers sub-800ms 99th-percentile search responses while strictly enforcing EU data residency constraints.

## Key Elements
* Search API Router (FastAPI with integrated Query Sanitizer)
* Query Translator (Elasticsearch DSL / Python)
* Search Index Engine (OpenSearch with EU-only primary and replica shard placement)
* Index Synchronization Consumer (Kafka Consumer / Python)
* Redis Cache Container (System-level Redis cache for query results)

## Relationships
* API Gateway Container -> Search API Router: Forwards search queries [HTTP/JSON over TLS]
* Search API Router -> Redis Cache Container: Checks and stores frequent query results [Redis TCP over TLS]
* Search API Router -> Query Translator: Passes validated query parameters [In-process]
* Query Translator -> Search Index Engine: Executes query DSL on cache miss [REST/JSON over HTTP]
* Event Broker Container -> Index Synchronization Consumer: Streams catalog mutation events [Apache Kafka TCP over TLS]
* Index Synchronization Consumer -> Search Index Engine: Performs idempotent bulk upserts [REST/JSON over HTTP]

## Technology Stack
* FastAPI / Python: Selected for the Search API Router to provide lightweight, high-performance REST routing and middleware integration.
* OpenSearch: Chosen for the Search Index Engine under an Apache 2.0 open-source license to prevent vendor lock-in and support EU-only node deployment.
* Redis: Utilized as an external cache container to reduce query latency and protect the search engine under high load.
* Apache Kafka: Deployed for event streaming to ensure asynchronous, real-time catalogue index freshness.

## Rationale
This architecture achieves the required <800ms search performance by separating read paths through Redis caching and utilizing asynchronous Kafka-driven write ingestion. Strict EU data residency is guaranteed by restricting all OpenSearch shards and event streams exclusively to EU-hosted nodes.