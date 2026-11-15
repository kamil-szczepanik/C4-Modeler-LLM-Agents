## Overview
The Search Engine container provides high-performance, multilingual, and fuzzy-matching search capabilities for the Library Management System. It is designed to meet strict EU data residency constraints and a 99th-percentile search response time under 800ms.

## Key Elements
- **Query Processor (Java/Elasticsearch DSL)**: Handles incoming search requests with linguistic analysis and facets.
- **Index Manager (Elasticsearch)**: Manages index lifecycles, mappings, and bulk ingestion.
- **Data Synchronizer (Kafka)**: Consumes CDC events from the Catalogue Service for eventual consistency.
- **Analytics Aggregator (Elasticsearch Transform API)**: Produces anonymized query metrics and zero-result logs.
- **Elasticsearch Cluster**: Core storage and search engine deployed within EU-region availability zones.

## Relationships
- Catalogue Service -> Query Processor: Queries catalogue items [gRPC/TCP with mTLS]
- Catalogue Service -> Data Synchronizer: Publishes catalogue changes [Kafka topics with TLS 1.3]
- Analytics Aggregator -> Audit Logging Container: Publishes aggregated trending metrics [Kafka]

## Technology Stack
- **Search Engine**: Elasticsearch (chosen for sub-800ms latency and advanced search capabilities).
- **Internal Communication**: gRPC/TCP with mTLS (ensures low latency and secure inter-container transport).
- **Asynchronous Messaging**: Apache Kafka (enables reliable decoupling of write/sync pipelines).
- **Analytics**: Elasticsearch Transform API and Aggregations (computes native trends without external dependencies).
- **Infrastructure**: EU-region cloud availability zones with encrypted EBS volumes (satisfies strict EU data residency and security compliance).

## Rationale
The decomposed internal architecture isolates query parsing, write/sync operations, and analytics, ensuring high performance under heavy ingestion loads. Strict security controls, PII anonymization, and resource guardrails ensure regulatory compliance and robust availability within EU data boundaries.