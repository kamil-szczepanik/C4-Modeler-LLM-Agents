## Overview
[The Catalog Service container manages book catalog browsing, searching, inventory, and localization for the Online Bookstore system.]
[It provides high-performance search, multi-currency support, and real-time inventory tracking to serve global users at scale.]

## Key Elements
- Catalog API Controller (Go, gRPC)
- Search Engine Adapter (Go)
- Inventory Manager (Go)
- Catalog Cache Layer (Go, go-redis)
- Pricing & Localization Interceptor (Go)
- Inventory Write-Through / Event Publisher (Go)
- Amazon OpenSearch
- Amazon Aurora PostgreSQL
- Amazon ElastiCache (Redis)
- Amazon SQS/SNS

## Relationships
- Catalog API Controller -> Search Engine Adapter & Inventory Manager [In-process method calls]
- Search Engine Adapter -> Amazon OpenSearch [Query DSL over HTTPS]
- Inventory Manager -> Amazon Aurora PostgreSQL [PostgreSQL Wire Protocol via TCP]
- Catalog Cache Layer -> Amazon ElastiCache (Redis) [RESP protocol via TCP]
- Inventory Write-Through / Event Publisher -> Amazon SQS/SNS [AWS SDK / HTTPS]

## Technology Stack
- Go: Chosen for high-throughput concurrency and low memory footprint in microservices.
- gRPC over HTTP/2: Selected for low-latency, strongly typed internal inter-service communication.
- Amazon OpenSearch: Deployed for high-performance keyword search and faceted catalog browsing.
- Amazon Aurora PostgreSQL: Utilized for ACID-compliant transactional data storage with multi-region read replicas.
- Amazon ElastiCache (Redis): Implemented for sub-second catalog detail caching and resiliency fallbacks.

## Rationale
[This component architecture directly satisfies sub-2s page load and 1M MAU scalability requirements via aggressive caching and search indexing.]
[It enforces strict regional availability, security controls, and real-time data consistency to support global multi-currency e-commerce operations.]