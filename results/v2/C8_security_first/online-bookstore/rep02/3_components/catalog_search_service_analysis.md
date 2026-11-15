## Overview
The Online Bookstore Catalog & Search Service delivers scalable, sub-2-second book browsing and typo-tolerant keyword search for 1M MAU. It utilizes a containerized Node.js application backed by Elasticsearch and Redis, deployed globally across AWS regions.

## Key Elements
- Shoppers / Customers
- Book Publishers / Administrators
- Search & Catalog API Router (Express.js, TypeScript)
- Catalog Business Logic (Node.js)
- Elasticsearch Client (@elastic/elasticsearch)
- Distributed Cache Client (ioredis)
- Amazon OpenSearch Service
- Amazon ElastiCache for Redis
- Amazon ECS with AWS Fargate

## Relationships
- AWS API Gateway -> Search & Catalog API Router: Routes catalogue and search requests [gRPC over mTLS with JWT]
- Search & Catalog API Router -> Catalog Business Logic: Delegates HTTP/gRPC requests and validates JWT claims [Internal Function Call]
- Catalog Business Logic -> Distributed Cache Client: Fetches cached multi-currency search payloads [TCP / Redis Protocol over TLS]
- Catalog Business Logic -> Elasticsearch Client: Executes sanitized, typo-tolerant DSL queries [Internal Function Call]
- Elasticsearch Client -> Amazon OpenSearch Service: Executes search queries and index updates [HTTPS, TLS 1.3 with IAM/SigV4]

## Technology Stack
- Node.js & Express (TypeScript): Powers the lightweight, high-performance API router and business logic.
- Amazon OpenSearch Service: Managed search backend providing faceted and typo-tolerant search capabilities.
- Amazon ElastiCache for Redis: In-memory cache utilizing TLS and encryption at rest for rapid query retrieval.
- Amazon ECS with AWS Fargate: Serverless container orchestration ensuring auto-scaling for 1M MAU.
- AWS KMS & Secrets Manager: Secures data at rest (AES-256) and eliminates hardcoded credentials.

## Rationale
This architecture leverages managed AWS services and in-memory caching to achieve 99.95% uptime and sub-2-second latency under high loads. Fargate containers combined with multi-region OpenSearch clusters ensure global scalability and compliance.