## Overview
[The Online Bookstore system provides a scalable e-commerce platform for browsing, searching, and purchasing physical and electronic books with integrated recommendations and reviews. The Catalog Service component handles high-performance book inventory, metadata management, and keyword search operations.]

## Key Elements
- API Controller: Validates inputs and routes gRPC/mTLS requests [Go, net/http]
- Catalog Manager: Handles core business logic for book metadata and inventory [Go]
- Search Indexer / Query Engine: Optimizes keyword search and indexing [Go]
- Cache Manager Component: Manages hot book details and search caching [Go]
- Data Access Repository: Executes persistence operations via `pgx` driver [Go]
- Amazon Aurora PostgreSQL: Stores persistent catalog data
- Amazon ElastiCache (Redis): Caches catalog data and search results globally

## Relationships
- API Controller -> Cache Manager: Checks read-through cache [In-memory]
- Cache Manager -> Data Access Repository: Fallback on cache miss [In-memory]
- Catalog Manager -> Search Indexer: Queries search indexes [In-memory]
- Data Access Repository -> Amazon Aurora PostgreSQL: SQL queries [PostgreSQL Protocol, TLS 1.3]
- Catalog Service -> Amazon ElastiCache: Reads/writes cached data [Redis Protocol, TLS]

## Technology Stack
- Go (net/http): Chosen for high-throughput, low-latency API handling
- AWS ECS Fargate: Container orchestration for scalable, serverless microservices deployment
- Amazon Aurora PostgreSQL: Relational database ensuring ACID compliance for catalog data
- Amazon ElastiCache (Redis): In-memory data store for sub-2s search performance under high load

## Rationale
[This architecture uses a Go-based microservice on AWS ECS Fargate combined with Redis caching and PostgreSQL to deliver sub-2-second page loads and high availability for 1 million monthly active users. Multi-region ElastiCache Global Datastores and robust security controls satisfy strict global scalability, performance, and GDPR/CCPA compliance requirements.]