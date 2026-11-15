## Overview
The Catalog Service manages book discovery, browsing, search, and metadata for the Online Bookstore. It ensures high-performance, multi-currency catalog operations supporting 1M MAU.

## Key Elements
- `CatalogController` (Node.js/Express)
- `AdminCatalogController` (Node.js/Express)
- `SearchService` (Node.js)
- `PricingService` (Node.js)
- `CatalogRepository` (Node.js / TypeORM)
- Amazon RDS (PostgreSQL)
- Amazon OpenSearch
- Amazon ElastiCache (Redis)
- AWS Fargate

## Relationships
- `API Gateway` -> `CatalogController`: Routes catalog queries [HTTPS / mTLS via AWS App Mesh]
- `CatalogController` -> `SearchService`: In-memory function calls [TypeScript]
- `SearchService` -> `Amazon OpenSearch`: Queries catalog index [HTTPS]
- `CatalogController` -> `PricingService`: In-memory calculation [TypeScript]
- `CatalogController` -> `CatalogRepository`: In-memory function calls [TypeScript]
- `AdminCatalogController` -> `CatalogRepository`: In-memory persistence calls [TypeScript]
- `CatalogRepository` -> `Amazon RDS (PostgreSQL)`: Reads/Writes structured data [TCP / SQL via TLS]
- `PricingService` -> `Amazon ElastiCache (Redis)`: Caches exchange rates and hot queries [TCP via TLS]

## Technology Stack
- Node.js & Express: Provides lightweight, fast execution for REST endpoints.
- TypeScript: Ensures type safety across component interactions.
- Amazon RDS (PostgreSQL): Stores authoritative book metadata and multi-currency pricing.
- Amazon OpenSearch: Delivers high-performance keyword search and filtering.
- Amazon ElastiCache (Redis): Caches exchange rates and hot queries for low latency.
- AWS Fargate: Runs containerized services serverlessly with auto-scaling.

## Rationale
This architecture uses dedicated search and caching layers to guarantee sub-2-second page loads and scale to 1M MAU. Isolated components and secure data stores ensure strict compliance, OWASP mitigations, and 99.95% uptime.