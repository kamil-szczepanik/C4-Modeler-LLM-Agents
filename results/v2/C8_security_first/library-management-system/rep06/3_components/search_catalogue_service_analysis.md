## Overview
- Search & Catalogue Service for the Library Management System, providing high-performance item discovery and cataloging.
- Built to handle multi-format physical and digital assets while strictly enforcing EU data residency constraints.

## Key Elements
- Search API Controller (Go, Gin/gRPC)
- Catalog Management Engine (Python, FastAPI)
- Search Index Client (OpenSearch wrapper with Facet Configuration Component)
- Analytics & Logging Collector (Async Worker)
- OpenSearch Cluster (StatefulSet, EU-localized Persistent Volumes)
- HashiCorp Vault (Secret Management)

## Relationships
- API Gateway -> Search API Controller: Queries catalogue via gRPC with mTLS
- Search API Controller -> Search Index Client: Executes search queries via OpenSearch REST API over TLS 1.3
- Catalog Management Engine -> Search Index Client: Synchronizes metadata updates via OpenSearch Bulk API over TLS 1.3
- Search API Controller -> Analytics & Logging Collector: Offloads anonymized query metrics via Kafka/RabbitMQ
- Internal Components -> HashiCorp Vault: Dynamic secret injection via HashiCorp Vault sidecars

## Technology Stack
- Go (Gin/gRPC): Selected for the Search API Controller to ensure high-throughput, low-latency search query handling.
- Python (FastAPI): Chosen for the Catalog Management Engine to efficiently handle complex metadata ingestion and synchronization.
- OpenSearch: Implemented for multi-format indexing, faceting, and relevance scoring, compliant with EU-only data residency constraints.
- Kubernetes StatefulSet: Used for stateful OpenSearch deployment with regional EU anti-affinity rules.
- HashiCorp Vault: Utilized for secure, dynamic credential management and TDE encryption keys.

## Rationale
- Decomposing the service into independent read (Search API) and write (Catalog Engine) components enables isolated horizontal autoscaling for peak loads.
- Asynchronous analytics offloading and strict mTLS/JWT security boundaries protect the 99th-percentile <800ms search latency SLA (R-05) and EU compliance mandates.