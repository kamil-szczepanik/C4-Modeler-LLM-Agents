## Overview
This architecture summary outlines the Catalog & Search Service for the Online Bookstore, enabling high-performance book discovery. It provides scalable, secure, and multi-currency catalog browsing to satisfy global customer demands.

## Key Elements
- API Router Component (Go/Gin)
- Search Engine Client (Go, Elasticsearch Client)
- Catalog Repository (Go, database/sql)
- Index Synchronization Worker (Go, Debezium CDC)
- Pricing & Localization Resolver (Go)
- Cache Management Middleware (Go, Redis Client)
- Elasticsearch / Amazon OpenSearch Service
- Amazon Aurora PostgreSQL
- Amazon ElastiCache (Redis)

## Relationships
- API Router Component -> Search Engine Client [In-process Go interfaces]
- API Router Component -> Cache Management Middleware [In-process Go interfaces]
- Cache Management Middleware -> Caching Layer [Redis Protocol over TLS]
- Search Engine Client -> Elasticsearch [HTTP/REST over TLS]
- Search Engine Client -> Pricing & Localization Resolver [In-process Go structs]
- Catalog Repository -> Database [PostgreSQL Protocol over TLS]
- Index Synchronization Worker -> Database & Elasticsearch [Transactional Outbox via CDC]

## Technology Stack
- Go with Gin framework: Chosen for high-throughput, low-latency REST API routing.
- Elasticsearch / Amazon OpenSearch Service: Provides fast, typo-tolerant keyword search and multi-facet filtering.
- Amazon Aurora PostgreSQL: Delivers reliable, multi-AZ relational persistence for catalog records.
- Amazon ElastiCache (Redis): Caches search snippets to ensure sub-2-second page loads.
- AWS Fargate & ECS: Runs containerized services scalably across multiple global regions.

## Rationale
The micro-component decomposition using Go ensures high performance and low latency to meet strict 3G load constraints. Integrating Redis caching and a transactional outbox pattern guarantees high availability, scalability, and data consistency across global regions.