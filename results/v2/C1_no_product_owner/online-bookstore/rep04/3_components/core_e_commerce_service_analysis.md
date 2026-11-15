## Overview
The system is an online bookstore providing catalog browsing, secure checkout, reviews, and recommendations. It is architected as a distributed microservices platform deployed on AWS across multiple global regions.

## Key Elements
- Checkout & Fulfillment Service (Node.js, TypeScript, AWS ECS Fargate)
- Checkout Orchestrator Component
- Fulfillment Coordinator Component
- Data Access Repository Component
- Amazon Aurora PostgreSQL Global Database
- Amazon ElastiCache Redis
- Amazon SQS / SNS with DLQs
- AWS App Mesh
- AWS Secrets Manager & KMS

## Relationships
- Checkout Orchestrator -> Payment Gateway: Secure payment processing via HTTPS
- Fulfillment Coordinator -> Amazon SQS / SNS: Publishes asynchronous fulfillment events via TLS / IAM
- Checkout & Fulfillment Service -> Amazon Aurora PostgreSQL: Transactional data persistence via gRPC over mTLS
- Checkout & Fulfillment Service -> Amazon ElastiCache Redis: Cart and session state management via mTLS
- Internal Tasks -> Internal Tasks: East-West communication via gRPC over mTLS using AWS App Mesh

## Technology Stack
- Node.js & TypeScript: Provides robust runtime and type safety for business logic
- AWS ECS Fargate: Enables serverless container execution with independent scaling per component
- AWS App Mesh: Enforces zero-trust mTLS and traffic management
- Amazon Aurora PostgreSQL: Provides globally distributed relational storage with multi-region failover
- AWS Secrets Manager & KMS: Secures credentials and encrypts data at rest using customer-managed keys

## Rationale
Splitting microservices into independent Fargate tasks isolates PCI-compliant checkout flows from public browsing to meet security and GDPR constraints. Global database replication and zero-trust mTLS networking ensure high availability, low latency, and strict resilience under 1M MAU scale.