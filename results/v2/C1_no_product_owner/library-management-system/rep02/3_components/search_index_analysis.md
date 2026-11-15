## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within the EU. The Search Index container delivers high-performance text retrieval to support sub-800ms search requirements while enforcing strict data residency constraints.

## Key Elements
- **Primary Data Node / Index Engine**: OpenSearch/Elasticsearch Core (Apache Lucene)
- **Query Parsing & Caching Component**: OpenSearch Query DSL & Node-level cache
- **Bulk Ingestion Buffer / Bulk Processing Engine**: OpenSearch Bulk API / Ingest Node
- **External Dependencies**: Search Service, Debezium CDC, EU Cloud Hosting Provider

## Relationships
- **Search Service -> Query Parsing & Caching Component**: Submits search queries via REST over HTTP/2 with mTLS
- **Debezium CDC -> Bulk Ingestion Buffer**: Streams asynchronous batch updates via REST/JSON over HTTP/2 with mTLS
- **Primary Data Node -> EU-Region Immutable Object Storage**: Automated encrypted snapshots

## Technology Stack
- **OpenSearch / Elasticsearch (Lucene)**: Selected for distributed, horizontally scalable search capabilities and low-latency index querying.
- **TLS 1.3 & mTLS**: Mandated for secure, encrypted network transport and service authentication.
- **AES-256**: Applied for persistent volume encryption at rest within the EU cloud provider.
- **OpenTelemetry**: Integrated for distributed tracing across search components.

## Rationale
Separating dedicated query-caching components from ingest nodes prevents write-heavy CDC synchronization from degrading read performance, directly fulfilling the sub-800ms search SLA. Strict private subnet isolation, EU-only data residency, and TLS 1.3 ensure comprehensive regulatory and security compliance.