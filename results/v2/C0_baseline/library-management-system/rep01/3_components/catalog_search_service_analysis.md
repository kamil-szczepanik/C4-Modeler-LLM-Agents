## Overview
- The Catalog & Search Service provides high-performance item discovery and inventory tracking for the Library Management System.
- It delivers sub-800ms faceted searches and real-time branch availability for patrons and librarians while enforcing EU data residency.

## Key Elements
- **Search API Controller (Go)**: Exposes endpoints for multi-faceted search and discovery workflows.
- **Indexing Worker (Go)**: Consumes catalog change events to update Elasticsearch indices.
- **Event Consumer Worker (Go)**: Processes inventory events from the message broker.
- **Local Availability Cache Component (Go/BigCache)**: Stores real-time branch availability in-memory.
- **Elasticsearch Cluster**: Backs multi-faceted queries and catalogue metadata storage.

## Relationships
- **API Gateway -> Search API Controller**: Routes incoming queries [gRPC over mTLS].
- **Search API Controller -> Elasticsearch**: Executes search queries [HTTP/REST over TCP].
- **Search API Controller -> Local Availability Cache**: Performs local status lookups [In-memory lookup, <5ms].
- **Event Consumer Worker -> Local Availability Cache**: Updates inventory states [In-memory write].
- **Indexing Worker -> Elasticsearch**: Syncs metadata [HTTP with HMAC/mTLS].
- **Catalog & Search Service -> Observability Platform**: Streams Prometheus metrics and traces [OTLP over TLS].

## Technology Stack
- **Go**: Chosen for high-throughput API handling and low-latency component execution.
- **Elasticsearch**: Enables multi-faceted search under the 800ms performance SLA (R-05).
- **Go BigCache (In-Memory)**: Eliminates synchronous database bottlenecks for real-time item availability.
- **AES-256 & TLS 1.3/mTLS**: Secures data at rest and internal communications within the EU region.

## Rationale
- Asynchronous caching and dedicated search indexing decouple availability checks from core databases to guarantee sub-800ms responses. Strict EU deployment, encryption, and RBAC meet regulatory and security constraints.