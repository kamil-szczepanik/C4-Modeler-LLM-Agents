## Overview
The Elasticsearch component provides indexed full-text search and audit log queries for the Clinic Management System. It ensures sub-second retrieval of electronic medical records (EMR) while maintaining HIPAA and GDPR compliance.

## Key Elements
- Lucene Index Engine
- REST/Transport Interface layer
- Document Routing & Sharding Module
- Query Parser & Analyzer
- Index Lifecycle Management (ILM) Module

## Relationships
- Core Clinical Services -> Elasticsearch: Queries and indexes EMR search data and audit logs [HTTPS, Port 9200, JSON, mTLS]
- Elasticsearch Nodes -> Elasticsearch Nodes: Shard synchronization and cluster state updates [Transport Protocol, TLS 1.3, Ports 9300-9400]
- Elasticsearch -> Object Storage: Offloads cold indices for long-term retention [HTTPS, AES-256]

## Technology Stack
- Elasticsearch: Core search and analytics engine for high-performance EMR retrieval and audit logging
- Lucene Index Engine: Inverted index execution for sub-second query performance
- Kubernetes StatefulSets: Orchestrates multi-node cluster deployment with `bootstrap.memory_lock: true`
- TLS 1.3: Secures node-to-node cluster communication and transport traffic
- AES-256: Enforces data encryption at rest for all indices containing PHI

## Rationale
This architecture guarantees 99.99% availability and sub-second P95 performance through a resilient 3-node cluster and hot-warm-cold ILM tiering. It strictly satisfies healthcare security mandates via mTLS, RBAC, and AES-256 encryption.