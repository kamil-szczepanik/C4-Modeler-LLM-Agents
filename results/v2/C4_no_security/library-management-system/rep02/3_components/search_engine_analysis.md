## Overview
The Library Management System provides cataloging, circulation, and self-service portals for libraries while strictly enforcing EU data residency. The Search Engine container delivers fast, typo-tolerant discovery of physical and digital items.

## Key Elements
*   **Search Engine (Elasticsearch)**: Dedicated container deployed across 3 EU-only availability zones.
*   **Query Parser Component (Lucene Query DSL / Java)**: Translates API Gateway requests, handling fuzzy matching.
*   **Indexing & Synchronization Component (Kafka Connect)**: Applies bulk upserts with a 1-second refresh interval.
*   **Data Storage Nodes Component (Elasticsearch Index Shards)**: Persists search indices on EU-localized storage with encrypted persistent volumes.
*   **Faceted Aggregation Engine Component (Elasticsearch Aggregations)**: Processes in-memory multi-faceted filters.

## Relationships
*   **API Gateway -> Query Parser Component**: Routes search queries via [gRPC / HTTPS].
*   **Async Message Broker (Kafka) -> Indexing & Synchronization Component**: Consumes catalogue mutation events via [Kafka Protocol / TCP].

## Technology Stack
*   **Elasticsearch**: Core search technology for out-of-the-box faceted filtering and typo-tolerance.
*   **Kafka Connect**: Standardized synchronization tool to meet the 5-second freshness target.
*   **Kubernetes StatefulSet**: Orchestrates Elasticsearch deployment with strict resource limits and JVM heap sizing.
*   **OpenTelemetry, Prometheus, Grafana**: Instruments components to track 99th-percentile latency against the <800ms SLA.

## Rationale
This architecture guarantees sub-800ms response times for patrons and staff while adhering to strict EU data residency constraints. Distributed index shards, async synchronization, and robust observability ensure high availability and performance.