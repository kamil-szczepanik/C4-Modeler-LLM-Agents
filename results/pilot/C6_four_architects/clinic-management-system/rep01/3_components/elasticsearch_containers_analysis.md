## Overview
The Elasticsearch Containers subsystem provides high-performance text-search indexing and CQRS read model storage for the Clinic Management System. It ensures sub-second EMR search latencies and supports long-term audit trail and clinical data queries.

## Key Elements
- Elasticsearch 3-node cluster deployed on Kubernetes StatefulSets
- Master, Data, and Ingest node tiers across separate failure domains
- Lucene Index Searcher and Document Routing/Parsing engine
- Index Lifecycle Management (ILM) and Snapshot Lifecycle Management (SLM) execution engines
- Security Plugin module with role-based access control and mTLS
- Internal monitoring and Prometheus metrics exporter component

## Relationships
- Patient & EMR Service -> Elasticsearch Containers: Retrieves indexed clinical records and patient demographics via gRPC over Envoy sidecar (port 9200/HTTPS)
- Apache Kafka -> Elasticsearch Containers: Ingests change data capture (CDC) streams for real-time synchronization over HTTPS
- Elasticsearch Containers -> Minio Object Storage Gateway Container: Backs up indices via Snapshot and Restore engine for 10-year retention
- Elasticsearch Containers -> Observability Collector Container: Exports JVM and cluster metrics via Prometheus scrape endpoints over HTTP

## Technology Stack
- Elasticsearch official Docker image: Core search engine selected for sub-second retrieval performance (R-07)
- Kubernetes StatefulSets & PVCs: Provides persistent, ordered deployment with encrypted block storage
- POSIX Filesystem with `bootstrap.memory_lock: true`: Locks JVM heap (max 32GB) to prevent swapping and optimize Lucene performance
- Transport Protocol (port 9300) & REST API (port 9200): Inter-node synchronization and secure internal service communication
- Debezium & Apache Kafka: Change Data Capture pipeline for near real-time CQRS synchronization

## Rationale
This architecture guarantees high availability (99.99%) and HIPAA/GDPR compliance through isolated cluster tiers, encrypted storage, and automated snapshot policies. Separating search workloads from relational databases ensures sub-second EMR search performance under heavy clinical load.