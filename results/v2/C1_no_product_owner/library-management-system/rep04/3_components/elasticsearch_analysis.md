## Overview
[Library Management System provides catalogue and circulation management for public and academic libraries. The Elasticsearch component delivers high-performance full-text search while maintaining EU data residency.]

## Key Elements
- Search API (Java/Lucene REST API)
- Security Interceptor
- Query Caching Layer
- Lucene Index Engine (Apache Lucene)
- Cluster Coordinator (Zen Discovery)

## Relationships
- Catalogue Service -> Search API: Indexes and searches catalogue items [HTTP/REST over TLS 1.3 with mTLS]
- Search API [Security Interceptor] -> Search API [Query Caching Layer]: Validates JWT and permissions before cache check [In-memory]
- Search API [Query Caching Layer] -> Lucene Index Engine: Executes uncached queries [In-memory Java API]
- Cluster Coordinator -> Cluster Coordinator: Manages node communication [TLS 1.3]

## Technology Stack
- Java / Lucene REST API: Powers the search endpoint implementation
- Apache Lucene: Provides core indexing and full-text retrieval
- Zen Discovery: Manages cluster coordination and state
- AES-256: Secures data at rest via EU-hosted KMS
- Prometheus: Scrapes metrics for JVM heap and cache ratios

## Rationale
[Separating the search components ensures sub-800ms response times for catalogue searches. Strict encryption, mTLS, and EU-region storage satisfy data residency and security constraints.]