## Overview
The Catalogue Service powers book browsing, faceted keyword search, and catalogue management for the Online Bookstore. It is designed to handle high-read concurrency while maintaining strict real-time inventory accuracy and multi-currency pricing support.

## Key Elements
- Shoppers / Customers: End-users browsing books and executing searches
- Store Administrators: Staff managing catalogue metadata, inventory, and pricing
- Web Frontend (SPA/SSR): React and Node.js interface consuming catalogue data
- Catalogue Service: Core container handling product data, deployed on AWS ECS/EKS
- AWS CloudFront: Edge-caching layer for static product metadata
- Amazon ElastiCache (Redis): Read-aside caching layer with circuit-breaker resilience
- AWS OpenSearch: Dedicated search indices for low-latency catalogue queries
- Amazon RDS: Transactional relational database for write operations
- AWS EventBridge / Kafka: Event bus for asynchronous CQRS synchronization
- AWS KMS: Customer-managed keys (CMK) for encryption at rest
- WORM S3 Bucket: Immutable storage for asynchronous administrative audit logs

## Relationships
- Web Frontend SPA/SSR -> Catalogue Service: Requests catalogue and product data via REST and gRPC over mTLS
- Store Administrators -> Catalogue Service: Submits inventory updates and metadata changes via authenticated REST APIs (OIDC/JWT, RBAC, MFA)
- Catalogue Service -> Amazon RDS: Executes transactional write operations for inventory and metadata changes
- Amazon RDS -> AWS EventBridge / Kafka: Emits real-time inventory change events
- Event Bus -> AWS OpenSearch: Synchronizes read indices asynchronously using a CQRS pattern
- Catalogue Service -> ElastiCache (Redis) & OpenSearch: Serves high-concurrency read queries with TLS 1.3 encryption

## Technology Stack
- AWS ECS/EKS: Container orchestration across multi-AZ clusters in `us-east-1`, `eu-west-1`, and `ap-southeast-1` to guarantee 99.95% uptime (R-07)
- AWS CloudFront & Amazon ElastiCache (Redis): Edge-caching and read-aside caching to ensure sub-2-second page loads on 3G (R-06)
- Amazon OpenSearch: Scalable search backend supporting fast faceted keyword searches for 1M MAU (R-05)
- Amazon RDS & EventBridge/Kafka: CQRS architecture decoupling heavy read traffic from transactional inventory writes
- AWS KMS: Data-at-rest encryption across RDS, OpenSearch, and S3 to meet GDPR and CCPA compliance
- OpenTelemetry & AWS X-Ray: Distributed tracing and observability for p99 latency tracking

## Rationale
This architecture decouples reads and writes via CQRS and multi-tier caching (CloudFront, Redis, OpenSearch) to achieve sub-2-second response times under 1M MAU concurrency. Multi-region AWS deployment with strict encryption, WORM audit logging, and RBAC security controls ensures 99.95% availability and compliance with GDPR and CCPA.