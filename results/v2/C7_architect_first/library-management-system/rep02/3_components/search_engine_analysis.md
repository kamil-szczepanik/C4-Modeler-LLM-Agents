## Overview
• A scalable, secure Search Engine container within the Library Management System providing low-latency catalog discovery and self-service portals.
• Designed to catalogue physical and digital items while guaranteeing EU-only data residency and sub-800ms search response times.

## Key Elements
• Query Parser Component: Lucene Query DSL engine handling sanitization, fuzzy matching, facets, and PII masking.
• Indexing Pipeline Component: Tokenizer and bulk ingestion pipeline featuring language analyzers and circuit breakers.
• Storage & Cluster Routing Component: Apache Lucene distributed shards hosted on multi-AZ OpenSearch data nodes.
• Redis Dead-Letter Queue (DLQ): Backpressure handler for bulk synchronization.
• Analytics Datastore: ClickHouse/TimescaleDB receiving search analytics, zero-result tracking, and audit logs.

## Relationships
• Core Services API -> Query Parser Component: Submits search queries via [HTTPS / REST] with mTLS.
• Async Worker -> Indexing Pipeline Component: Synchronizes catalogue item mutations via [HTTP / REST (Bulk API)] secured by mTLS/IAM.
• Query Parser Component -> Storage & Cluster Routing Component: Executes optimized Lucene search shards via [Internal Bolt/Transport Protocol].
• Search Engine Components -> Analytics Datastore: Streams metrics, slow-logs, and zero-results tracking.

## Technology Stack
• OpenSearch / Elasticsearch: Chosen for high-performance distributed search, Lucene query routing, and sharding capabilities.
• Lucene Query DSL: Powers advanced tokenization, fuzzy-matching, and real-time faceted aggregations.
• Redis: Implements a dead-letter queue for reliable bulk-sync backpressure management.
• TLS / mTLS: Secures service-to-service communication channels and client certificate authentication.

## Rationale
• The distributed sharding and JVM-tuned autoscaling directly achieve the sub-800ms P99 search response time constraint.
• Region-pinned data nodes, encrypted snapshots, and strict access controls enforce the mandatory EU-only data residency requirement.