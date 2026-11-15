## Overview
The Catalog Service manages book discovery, search, pricing, and inventory status for the Online Bookstore. It processes high-volume catalog requests while maintaining strict security, multi-currency support, and sub-second performance.

## Key Elements
- Catalog API Controller (Express.js)
- Search & Query Engine (TypeScript)
- Pricing & Inventory Adapter (TypeScript)
- Catalog Cache Manager (Redis/ElastiCache)
- Amazon OpenSearch
- Amazon Aurora PostgreSQL

## Relationships
- Catalog API Controller -> Search & Query Engine: In-memory TypeScript function calls
- Search & Query Engine -> Amazon OpenSearch: HTTPS with TLS and IAM authentication
- Search & Query Engine -> Amazon Aurora PostgreSQL: TCP with TLS and IAM authentication
- Catalog API Controller -> Catalog Cache Manager: RESP over TLS to Amazon ElastiCache
- Pricing & Inventory Adapter -> Order & Checkout Service: gRPC over mTLS

## Technology Stack
- Node.js & Express.js: Powers the Catalog Service for asynchronous request handling
- TypeScript: Ensures type safety across component modules
- Amazon OpenSearch: Delivers scalable keyword search and indexing
- Amazon Aurora PostgreSQL: Stores relational book metadata securely
- Amazon ElastiCache (Redis): Caches frequent queries and pricing to meet performance goals

## Rationale
Decomposing the Catalog Service into specialized components ensures high scalability for 1M MAU and sub-2-second page loads. Integrating ElastiCache caching and multi-region replication meets uptime and performance SLAs.