## Overview
- The Catalog & Search Container powers high-performance product browsing, keyword search, and localized pricing for the Online Bookstore.
- It delivers a scalable, low-latency search experience designed to handle 1M MAU globally across AWS regions.

## Key Elements
- Search API Handler (`Go`)
- Catalog Management Service (`Go`)
- Index Synchronizer (`Go` / `AWS Lambda`)
- Product Read Model Cache (`Redis`)
- Localization & Currency Resolver (`Go`)
- Search Analytics Emitter (`Go`)
- Amazon OpenSearch
- Aurora PostgreSQL
- Amazon Kinesis

## Relationships
- API Gateway -> Search API Handler [gRPC over mTLS]
- Search API Handler -> Amazon OpenSearch [REST/HTTPS]
- Catalog Management Service -> Aurora PostgreSQL [SQL/TCP]
- Index Synchronizer -> Aurora PostgreSQL & Amazon OpenSearch [CDC/Debezium]
- Search API Handler -> Product Read Model Cache [TCP/Redis Protocol]
- Search API Handler -> Localization & Currency Resolver [Internal gRPC]
- Search Analytics Emitter -> Amazon Kinesis [Async/TCP]

## Technology Stack
- Go: Chosen for high-throughput, low-latency concurrency in search and ingestion handlers.
- Amazon OpenSearch: Provides typo-tolerant keyword search and advanced filtering.
- Aurora PostgreSQL: Acts as the primary relational source of truth with multi-region replication.
- Redis: Powers low-latency product read caching and currency rate lookups.
- Amazon Kinesis: Enables asynchronous, non-blocking telemetry and search analytics streaming.
- AWS ECS (Fargate): Manages containerized microservice deployments with auto-scaling.

## Rationale
- Decoupling reads from writes via asynchronous CDC indexing ensures sub-2s performance under heavy load.
- Multi-region replication and resilient circuit-breakers guarantee 99.95% uptime and global scalability.