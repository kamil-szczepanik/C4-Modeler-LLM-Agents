## Overview
[The Catalog & Search Service is a high-performance Node.js container providing sub-second product discovery and faceted keyword search for the Online Bookstore. It handles 1M MAU through asynchronous event-driven synchronization and resilient caching layers.]

## Key Elements
- Search Controller (Node.js/Express)
- Search Engine Client (TypeScript)
- Product Repository (TypeScript/Prisma)
- Cache Manager (ioredis)
- Catalog Sync Worker (Node.js/BullMQ)
- Amazon OpenSearch Service
- Amazon Aurora PostgreSQL
- Amazon ElastiCache (Redis)
- Amazon SQS/SNS

## Relationships
- Search Controller -> Search Engine Client: Invokes search queries [In-process / Function Call]
- Search Controller -> Product Repository: Fetches product details [In-process / Function Call]
- Search Engine Client -> Amazon OpenSearch: Executes full-text search [HTTPS / AWS SigV4]
- Product Repository -> Amazon Aurora PostgreSQL: Reads/Writes product data [TCP/PostgreSQL wire protocol]
- Amazon SQS/SNS -> Catalog Sync Worker: Pushes catalog events [HTTPS / SQS Polling]
- Catalog Sync Worker -> Amazon OpenSearch: Updates search index [HTTPS / AWS SigV4]

## Technology Stack
- Node.js/Express: Chosen for lightweight, high-throughput routing
- Amazon OpenSearch: Selected for sub-second full-text search and synonyms
- Amazon Aurora PostgreSQL: Used for ACID-compliant relational product metadata
- Amazon ElastiCache (Redis): Deployed for sub-2s hot-cache performance
- BullMQ: Implemented for reliable asynchronous background job processing

## Rationale
[This architecture satisfies scalability and sub-2s performance requirements by decoupling read-heavy search traffic from write-heavy inventory ingestion using Redis caching and asynchronous OpenSearch indexing. Robust security controls, including AWS SigV4 authentication and private VPC subnets, ensure full GDPR/CCPA and OWASP compliance.]