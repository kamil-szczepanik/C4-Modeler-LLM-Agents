## Overview
An Amazon OpenSearch Service managed cluster provides sub-2s keyword search, catalog faceting, and merchandising-boosted relevance for the online bookstore. It processes up to 1M MAU across multi-region deployments while stripping all PII to maintain GDPR and CCPA compliance.

## Key Elements
* Shoppers and Administrators (Users)
* Catalog & Search Service (Container)
* Amazon SQS (Messaging Bus)
* Search Coordinator (Component: Java/Kotlin, OpenSearch Plugin)
* Indexing Worker with Merchandising Rules Engine (Component: OpenSearch Ingestion Engine)
* Index Shards & Storage (Component: Apache Lucene Engine, Amazon OpenSearch Service)
* Amazon S3 (Backup Storage)

## Relationships
* Catalog & Search Service -> Search Coordinator: Submits search queries [HTTPS / REST over secure VPC]
* Amazon SQS -> Indexing Worker: Delivers catalogue delta events [AWS SDK / SQS Pull]
* Indexing Worker -> Index Shards & Storage: Bulk-indexes documents and applies dynamic scoring [Internal Transport Protocol]
* Index Shards & Storage -> Amazon S3: Stores daily automated snapshots [AWS SDK / HTTPS]

## Technology Stack
* Amazon OpenSearch Service (Managed Cluster): Chosen for distributed search, multi-AZ high availability, and persistent EBS volumes.
* Apache Lucene Engine: Powers inverted indices, vector embeddings, and function_score merchandising queries.
* Terraform: Used for Infrastructure as Code management of cluster configurations and index templates.
* Amazon S3: Utilized for daily automated snapshots and point-in-time recovery.

## Rationale
Managed OpenSearch clusters guarantee 99.95% uptime and sub-2s query performance under high concurrency. Asynchronous SQS ingestion and multi-AZ shard replication decouple catalogue updates while meeting strict scalability and compliance constraints.