## Overview
This architecture defines the Catalog & Search Service for an online bookstore designed to support 1 million MAU with high performance. It provides secure, low-latency catalog browsing, faceted keyword search, and multi-currency pricing.

## Key Elements
* Search Controller (Spring MVC)
* Search Indexer / Sync Worker (Spring Cloud Stream, Elasticsearch Java Client)
* Catalog Management Service (Spring Data JPA)
* Currency Conversion Processor
* Catalog Event Publisher
* Amazon OpenSearch Service
* Amazon Aurora PostgreSQL
* Amazon SQS (with Dead Letter Queues)

## Relationships
* API Gateway -> Search Controller: Routes search requests via mTLS and AWS IAM
* Search Controller -> Amazon OpenSearch Service: Executes search and aggregation queries over HTTPS with TLS 1.3
* Catalog Management Service -> Amazon Aurora PostgreSQL: Persists source-of-truth data using IAM Database Authentication
* Catalog Management Service -> Amazon SQS: Publishes catalog and inventory mutation events via AWS SDK
* Search Indexer / Sync Worker -> Amazon OpenSearch Service: Performs near-real-time index updates using AWS SigV4 over HTTPS

## Technology Stack
* AWS ECS Fargate: Runs containerized Spring Boot services with task auto-scaling for cost-efficient compute
* Amazon OpenSearch Service: Managed search engine replacing self-managed Elasticsearch for automated snapshots and multi-AZ resilience
* Amazon Aurora PostgreSQL: Relational data store providing ACID compliance and cross-region replication
* Amazon SQS: Decouples write operations from search indexing to protect read-path latency
* Spring Boot / Spring Cloud Stream: Provides robust enterprise Java frameworks for REST routing and asynchronous event processing

## Rationale
Decomposing the catalog service into decoupled Spring Boot components with asynchronous SQS synchronization protects read-path performance under heavy traffic. Utilizing managed AWS services like OpenSearch and Aurora ensures strict GDPR/CCPA compliance, security, and multi-region scalability.