## Overview
[Library Management System catalogue and search engine backend using Elasticsearch 8.x to meet strict performance requirements and data residency constraints.]

## Key Elements
- Elasticsearch 8.x Cluster (Managed or Self-hosted)
- REST API / Transport Layer
- Query DSL & Search Engine
- Index & Storage Engine (Lucene)
- Index Lifecycle Management (ILM) Engine
- Cluster Coordination & Node Management

## Relationships
- Catalog & Search Service -> Elasticsearch: HTTP/2 over TLS (JSON) via Port 9200
- Elasticsearch -> EU-hosted Log & Telemetry Aggregator: Prometheus exporters and audit logging over TLS
- Elasticsearch -> EU-hosted Secrets Manager: Secure credential injection at startup

## Technology Stack
- Elasticsearch 8.x: Core search and indexing engine
- Lucene: Underlying storage and indexing engine
- Kubernetes StatefulSet: Multi-zone deployment across 3 availability zones in an EU cloud region
- mTLS & AES-256: Transport-layer and Encryption-at-Rest security
- Prometheus: Cluster health, JVM heap usage, and latency monitoring

## Rationale
[This architecture ensures 99th-percentile search responses under 800 ms through optimized querying, replica routing, and ILM tiering while strictly enforcing EU-only data residency via isolated infrastructure.]