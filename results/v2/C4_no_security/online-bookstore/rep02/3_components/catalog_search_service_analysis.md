## Overview
The Online Bookstore Catalog & Search Service provides high-performance book discovery, faceted filtering, and inventory management for 1M MAU. It uses a multi-region cloud architecture on AWS to ensure global scalability and sub-2-second page loads.

## Key Elements
- **Book Shopper & Store Administrator**: Primary system users interacting via the frontend.
- **Catalog Controller**: Exposes REST/gRPC endpoints and handles multi-currency formatting (USD, EUR, GBP).
- **Search Engine Client**: Integrates with Amazon OpenSearch for keyword search and faceted queries.
- **Inventory Manager**: Manages stock levels, pricing mutations, and includes an Audit Interceptor.
- **Cache Facade**: Manages hot-key caching with Redis, utilizing distributed locks and request collapsing.
- **Catalog Event Listener**: Consumes events from Amazon SQS/EventBridge for cache invalidation.
- **Amazon Aurora PostgreSQL**: Primary relational database for catalog and inventory persistence.
- **Amazon OpenSearch**: Search and indexing engine deployed in multi-AZ clusters.
- **Redis (ElastiCache)**: In-memory cache for high-throughput read performance.

## Relationships
- **AWS API Gateway** -> **Catalog Controller**: Routes catalog and search requests via internal HTTPS/gRPC.
- **Catalog Controller** -> **Faceted Navigation Component**: Delegates filtering and currency formatting via in-memory Java method calls.
- **Search Engine Client** -> **Amazon OpenSearch**: Queries search data using the AWS SDK.
- **Inventory Manager** -> **Amazon Aurora PostgreSQL**: Persists inventory changes via JDBC.
- **Cache Facade** -> **Redis**: Manages hot-key caching via the Redis Protocol.
- **Inventory Manager** -> **Amazon EventBridge**: Publishes stock and pricing mutation events asynchronously.

## Technology Stack
- **Java / Spring Boot**: Core framework for the Catalog & Search Service components.
- **Amazon Aurora PostgreSQL (Global Database)**: Relational store ensuring reliable persistence and multi-region replication.
- **Amazon OpenSearch**: Search engine for typo-tolerant, faceted catalog queries.
- **Redis (ElastiCache)**: Caching layer to mitigate high-traffic latency and support sub-2-second page loads.
- **Amazon SQS & EventBridge**: Messaging infrastructure for asynchronous event-driven synchronization.
- **Terraform**: Infrastructure as Code tool for managing multi-region AWS resources.

## Rationale
This architecture uses Amazon OpenSearch and Redis caching to meet strict performance and search requirements under high traffic. Decoupled asynchronous event listeners and circuit-breaking mechanisms ensure 99.95% availability across multiple AWS regions.