## Overview
The Online Bookstore System is an e-commerce platform enabling users to browse, search, and purchase physical and electronic books with integrated reviews and recommendations. It utilizes a microservices architecture deployed across multiple AWS regions to support high scalability and availability.

## Key Elements
- Customer / Reviewer [person, context]
- Store Administrator [person, context]
- Single Page App / Mobile App [container] (React / React Native)
- API Gateway / BFF Container [container] (AWS API Gateway / Envoy)
- Catalog & Search Container [container] (Node.js / Go)
  - Search API Controller [component] (Go / Fiber)
  - Query Parser & Facet Engine [component] (Go)
  - Catalog Management Service [component] (Go)
  - Search Indexer Client [component] (Go)
  - Pricing & Currency Resolver [component] (Go)
  - Audit Logging Middleware [component] (Go)
- Checkout & Order Container [container] (Java / Spring Boot)
- Notification & Review Container [container] (Node.js / Express)
- Admin Dashboard Container [container] (React)
- Database Containers [container] (Amazon Aurora Global PostgreSQL)
- Amazon OpenSearch Service [externalSystem, container]
- Amazon ElastiCache (Redis) [container]

## Relationships
- Customer / Reviewer -> Single Page App / Mobile App [HTTPS]
- Single Page App / Mobile App -> API Gateway / BFF Container [HTTPS / REST]
- API Gateway / BFF Container -> Catalog & Search Container [Internal mTLS / REST]
- Search API Controller -> Amazon OpenSearch Service [HTTPS / REST, TLS 1.3]
- Catalog Management Service -> Database Containers [Internal mTLS / PostgreSQL Protocol]
- Audit Logging Middleware -> Amazon S3 [HTTPS / AWS IAM]

## Technology Stack
- Go / Fiber: Chosen for high-throughput, low-latency search and catalog routing.
- Amazon OpenSearch Service: Provides managed full-text search and faceted filtering independent of the primary database.
- Amazon Aurora Global PostgreSQL: Delivers transactional data storage with cross-region replication.
- Amazon ElastiCache (Redis): Caches multi-currency exchange rates and queries to ensure sub-2s latency.
- AWS IAM / KMS: Enforces least-privilege access, encryption in-transit (TLS 1.3), and encryption at-rest.

## Rationale
This architecture uses Go-based microservices and managed search/cache tiers to easily handle the 1M MAU scalability target and sub-2s page load performance. Multi-region AWS deployment with automated replication ensures 99.95% uptime and global compliance.