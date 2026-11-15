## Overview
The Amazon OpenSearch Service component provides low-latency keyword searching and review queries for the Online Bookstore. It ensures high performance, scalability, and security for 1 million monthly active users.

## Key Elements
- OpenSearch REST API / Routing Layer (OpenSearch Core HTTP REST interface)
- Search & Query Engine (Apache Lucene / OpenSearch Query DSL)
- Indexing & Analysis Pipeline (OpenSearch Index Modules)
- Index State Management (ISM) Controller (OpenSearch ISM Engine)
- Dedicated Master Nodes (OpenSearch Cluster Nodes)

## Relationships
- Catalog Service -> OpenSearch REST API / Routing Layer: Submits payloads and queries [HTTPS, TLS 1.3, AWS SigV4]
- Search & Query Engine -> Indexing & Analysis Pipeline: Manages inverted indices [Internal Transport, EBS]
- ISM Controller -> Amazon S3: Exports automated snapshots [HTTPS, AWS KMS]

## Technology Stack
- OpenSearch Service: Managed search engine for scalable catalog and review queries
- Apache Lucene: Powers full-text search and fuzzy matching capabilities
- AWS KMS: Encrypts data at rest and snapshots for compliance
- Amazon S3: Stores disaster recovery snapshots and cold storage data

## Rationale
This architecture uses Multi-AZ deployments, dedicated masters, and Fine-Grained Access Control to achieve 99.95% availability and strict GDPR/CCPA compliance. Private VPC isolation and AWS SigV4 authentication secure data transport while supporting 1M MAU performance targets.