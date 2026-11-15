## Overview
[The Online Bookstore Catalog & Search Container uses Spring Boot and Amazon OpenSearch to deliver high-performance product browsing, fuzzy search, and administrative catalog management. It provides sub-second search responses to support 1 million monthly active users while ensuring robust security and audit logging.]

## Key Elements
- Search Controller (Spring MVC REST endpoints)
- Admin Catalog Controller (Spring MVC administrative endpoints)
- Catalog Service (Business logic for product retrieval and inventory mapping)
- Search Indexer (Spring Data / OpenSearch Client for full-text search and fuzzy matching)
- Cache Manager (Spring Cache with Lettuce for Amazon ElastiCache Redis)
- Audit Logging Aspect (Spring AOP for modification tracking)

## Relationships
- AWS API Gateway -> Search Controller [REST / JSON over HTTP via mTLS]
- Search Controller -> Catalog Service & Search Indexer [In-process Java method calls]
- Admin Catalog Controller -> Catalog Service [In-process Java method calls with RBAC enforcement]
- Catalog Service -> Cache Manager [Redis Protocol to Amazon ElastiCache Redis]
- Catalog Service -> Amazon Aurora PostgreSQL [JDBC / TLS 1.3]
- Search Indexer -> Amazon OpenSearch [HTTPS / TLS 1.3]

## Technology Stack
- Java 17 / Spring Boot: Provides robust enterprise framework with dependency injection and security features.
- Amazon OpenSearch: Enables scalable full-text search, facets, and fuzzy typo-tolerance.
- Amazon ElastiCache Redis: Delivers sub-millisecond hot-item caching and rate-limiting storage.
- Amazon Aurora PostgreSQL: Stores persistent catalog data securely with IAM authentication.

## Rationale
[This architecture uses OpenSearch and Redis caching to meet strict sub-2-second performance and scalability requirements under high loads. Segregated administrative controllers and Spring AOP audit logging ensure compliance, data integrity, and strict RBAC enforcement.]