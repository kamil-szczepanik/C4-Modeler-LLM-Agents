## Overview
The Search & Catalog Service provides typo-tolerant discovery, faceted search, and real-time indexing for physical and digital library items. It ensures a 99th-percentile search response time under 800 ms while enforcing EU-only data residency.

## Key Elements
- **API Gateway**: Routes external requests via gRPC and internal mTLS using Kong or NGINX.
- **Search & Catalog Service**: Spring Boot application decomposed into `SearchController`, `CatalogQueryService`, `IndexSyncWorker`, `SearchTelemetryPublisher`, and `SearchAnalyzerConfigurator`.
- **Elasticsearch**: Clustered search engine with disk-level encryption and custom shard routing.
- **Apache Kafka**: Message broker for catalog mutation events using mTLS or SCRAM-SHA-512 authentication.
- **Analytics Service**: Receives telemetry via OpenTelemetry.
- **Infrastructure**: EU Kubernetes Cluster, EU Cloud Provider's HSM, and Secret Store CSI Driver.

## Relationships
- **API Gateway -> Search & Catalog Service**: Routes catalog and search requests [Internal mTLS and gRPC]
- **IndexSyncWorker -> Apache Kafka**: Consumes catalog mutation events [mTLS or SCRAM-SHA-512]
- **SearchTelemetryPublisher -> Analytics Service**: Emits query metrics and zero-result tracking [OpenTelemetry]

## Technology Stack
- **Java / Spring Boot & Spring WebFlux**: Provides reactive, non-blocking execution to handle high concurrent patron search loads and protect performance SLAs.
- **Elasticsearch**: Delivers typo-tolerant discovery, faceted search, and multi-lingual tokenization.
- **Resilience4j**: Implements circuit breakers to fail fast and prevent cascading failures during high latency or GC pressure.
- **EU Cloud Provider's HSM & Secret Store CSI**: Manages encryption keys and injects secrets securely to enforce EU data residency (R-05).

## Rationale
Decomposing the service into reactive components and asynchronous workers isolates query paths from heavy indexing workloads to maintain the <800ms SLA. Strict security controls, least-privilege Elasticsearch roles, and EU-bound infrastructure ensure compliance with data residency constraints.