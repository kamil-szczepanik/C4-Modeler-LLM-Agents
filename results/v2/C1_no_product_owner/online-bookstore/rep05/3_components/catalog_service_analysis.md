## Overview
The Online Bookstore system provides a scalable e-commerce platform for browsing, purchasing, and reviewing physical and electronic books. It ensures multi-region availability, GDPR/CCPA compliance, and secure high-performance operations.

## Key Elements
- **API Controller (Express Router):** Handles inbound gRPC/HTTP routing, payload validation, and request mapping.
- **Catalog Business Logic / Domain Core:** Encapsulates rules for category management, book metadata, and inventory linking.
- **Search & Indexing Adapter:** Interfaces with Amazon OpenSearch Service via HTTPS/REST for keyword search and faceting.
- **Data Access Repository:** Interfaces with Amazon DynamoDB using AWS SDK v3 for CRUD operations.
- **Cache-Aside Repository Wrapper:** Manages read-through/write-through caching strategy with Amazon ElastiCache (Redis).
- **Event Publisher/Consumer:** Interacts with Amazon EventBridge, SNS, and SQS to broadcast catalog updates.

## Relationships
- **API Controller -> Catalog Business Logic:** Invokes core domain rules via dependency injection.
- **Search & Indexing Adapter -> Amazon OpenSearch Service:** Indexes and queries catalog data via HTTPS/REST [TLS 1.3, IAM roles].
- **Data Access Repository -> Amazon DynamoDB:** Executes high-throughput CRUD operations [TLS, IAM roles, regional KMS CMKs].
- **Cache-Aside Repository Wrapper -> Amazon ElastiCache (Redis):** Caches catalog data [in-transit TLS, at-rest KMS CMKs, LRU eviction].
- **Event Publisher/Consumer -> Amazon EventBridge, SQS, SNS:** Publishes and consumes domain events [JSON over HTTPS].

## Technology Stack
- **Node.js / Express:** Runtime and framework for the Catalog Service container ensuring lightweight, fast execution.
- **AWS ECS (Fargate):** Serverless container orchestration ensuring multi-AZ and multi-region scalability.
- **Amazon DynamoDB & OpenSearch Service:** NoSQL storage and search engine for low-latency reads and rich catalog queries.
- **Amazon ElastiCache (Redis):** In-memory cache utilizing `ioredis` to prevent database throttling and meet latency targets.
- **OpenTelemetry & CloudWatch/Datadog:** Observability stack for distributed tracing and performance monitoring.

## Rationale
This architecture decouples heavy search traffic from transactional storage to easily handle 1 million MAU with <2s page loads. Multi-region AWS deployment and strict caching strategies guarantee 99.95% uptime and high resilience.