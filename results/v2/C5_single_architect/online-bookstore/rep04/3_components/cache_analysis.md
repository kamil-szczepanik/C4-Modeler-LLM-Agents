## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform designed for purchasing physical and electronic books with integrated recommendations and reviews. The Cache container provides high-performance in-memory storage to support low-latency page loads and high scalability across global regions.

## Key Elements
- Customer (Person)
- Single Page Application (React / TypeScript, AWS S3/CloudFront)
- API Gateway (AWS API Gateway)
- Catalog Service (Go, PostgreSQL (RDS))
- Order & Checkout Service (Node.js, PostgreSQL (RDS))
- Recommendation Service (Python FastAPI, Vector DB)
- Review Service (Java Spring Boot, MongoDB)
- Cache Container (Amazon ElastiCache with Redis)
  - Cache Routing & Policy Engine (Go / Redis Go Client)
  - In-Memory Storage Engine (Redis Open Source Core)
- External Systems (Payment Gateway, Shipping Provider API, Identity Provider, Notification Service, Tax Calculation Service)

## Relationships
- Catalog Service, Order & Checkout Service, Recommendation Service, Review Service -> Cache Routing & Policy Engine: Reads and writes cached data using RESP over TCP
- Cache Routing & Policy Engine -> In-Memory Storage Engine: Executes localized commands via TCP Loopback
- Customer -> Single Page Application: Browses catalog and manages cart via HTTPS

## Technology Stack
- Amazon ElastiCache (Redis): Provides sub-millisecond in-memory data access to meet performance and availability constraints
- Go / Redis Go Client: Powers the cache routing and policy engine for connection pooling and TTL enforcement
- Redis Open Source Core: Executes fast single-threaded key-value operations with volatile-lru eviction

## Rationale
This architecture uses an in-memory Redis cache to handle high-throughput read operations, ensuring page loads under 2 seconds on 3G networks. The multi-region AWS deployment model directly satisfies strict 99.95% uptime availability and global scalability requirements for 1 million MAU.