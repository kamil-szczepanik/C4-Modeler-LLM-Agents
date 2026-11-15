## Overview
The Search Engine container provides high-performance catalogue discovery for the Library Management System. It enables rapid retrieval of physical and digital items while enforcing strict EU data residency.

## Key Elements
- **Query Parser**: Sanitizes and translates search requests using Elasticsearch Query DSL.
- **Indexing Worker**: Consumes synchronization events to update the index.
- **Search Index (Storage Node)**: Lucene-based storage node enforcing EU data residency.
- **Ranking & Relevance Tuner**: Applies custom scoring scripts and synonym mappings.

## Relationships
- Core Domain -> Query Parser: Submits search requests [HTTP/JSON over TLS via Elasticsearch Java Client]
- Message Broker -> Indexing Worker: Streams catalog sync events [AMQP]
- Query Parser -> Ranking & Relevance Tuner: Applies custom scoring and boosts [Internal Lucene API]
- Query Parser -> Search Index: Executes low-latency index lookups [Internal Java Transport / Lucene API]

## Technology Stack
- **Elasticsearch**: Chosen as the core search engine to achieve sub-800ms 99th-percentile search response times.
- **Lucene API**: Utilized internally for efficient indexing, scoring, and storage operations.
- **LUKS**: Implemented for disk encryption at rest to satisfy EU data residency constraints.
- **Elasticsearch Java Client**: Standardized for communication between the Core Domain and Query Parser over HTTP/TLS.

## Rationale
This component architecture meets the sub-800ms performance requirement through dedicated indexing and query parsing mechanisms. Additionally, it guarantees compliance with EU-only data residency via isolated storage nodes and localized disk encryption.