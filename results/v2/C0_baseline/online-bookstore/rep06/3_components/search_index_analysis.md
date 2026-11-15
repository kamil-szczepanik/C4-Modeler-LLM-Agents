## Overview
The Search Index container provides high-performance, typo-tolerant catalogue search and near-real-time indexing for the Online Bookstore. It is architected to support 1M MAU, sub-second query responses, and global multi-region deployments while meeting strict security and compliance requirements.

## Key Elements
*   **Search Index (AWS OpenSearch):** Parent container providing distributed search and storage.
*   **Query Processor:** Component handling incoming search requests, typo-tolerance, analysis pipelines, and input sanitization.
*   **Indexing Engine:** Component consuming catalogue mutation events for near-real-time index updates.
*   **Cluster State & Storage:** Component managing primary-replica shards, EBS NVMe storage, and backup tiers across availability zones.
*   **Catalog & Search Service:** External container generating search queries.
*   **Event Bus (AWS SQS / EventBridge):** External messaging service delivering catalogue mutation events.

## Relationships
*   Catalog & Search Service -> Query Processor: HTTP/REST [TLS 1.3, AWS IAM SigV4]
*   Event Bus -> Indexing Engine: HTTP/REST [TLS 1.3, AWS IAM SigV4 via OpenSearch Bulk API]
*   Cluster State & Storage -> AWS S3: HTTPS [TLS 1.3 for Cross-Region Snapshots]

## Technology Stack
*   **AWS OpenSearch:** Distributed search engine providing multi-AZ sharding, cross-cluster replication, and 99.95% uptime.
*   **Lucene Analysis Pipeline:** Token filters, synonym mapping, and fuzzy-matching algorithms for search relevance.
*   **AWS IAM SigV4:** Zero-trust authentication enforcing strict service-to-service authorization.
*   **AWS KMS:** Customer Managed Keys (CMK) ensuring encryption-at-rest.
*   **AWS CloudWatch:** Monitoring, audit logging, and SIEM integration.

## Rationale
This architecture uses managed AWS OpenSearch with dedicated VPC isolation and IAM SigV4 to meet rigorous OWASP Top-10 security constraints and GDPR/CCPA compliance. Furthermore, the decoupling of the Query Processor and Indexing Engine with bulk API batching guarantees sub-second page loads and rapid catalog updates across all target regions.