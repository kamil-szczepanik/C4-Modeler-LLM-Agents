## Overview
The Online Bookstore system uses a microservices architecture on AWS to handle 1M MAU with 99.95% uptime. The Localization & Currency Service component ensures secure, real-time multi-currency conversion and localization mapping.

## Key Elements
- API Gateway & Security (AWS API Gateway, AWS WAF)
- Localization & Currency Service (AWS ECS Fargate): Decomposed into Currency Conversion Component, Exchange Rate Sync Worker, and Localization Mapping Component
- Amazon ElastiCache (Redis) with Global Datastore
- AWS Secrets Manager
- Third-Party Financial APIs and Shipping Provider APIs

## Relationships
- API Gateway -> Localization & Currency Service: Routes internal traffic via [gRPC with mTLS]
- Currency Conversion Component & Localization Mapping Component -> Amazon ElastiCache: Performs lookups via [Internal VPC Connection]
- Exchange Rate Sync Worker -> Third-Party Financial APIs: Pulls rates via [HTTPS]
- Exchange Rate Sync Worker -> AWS Secrets Manager: Retrieves credentials via [AWS SDK / Internal API]

## Technology Stack
- Node.js / TypeScript: Chosen for lightweight, high-performance asynchronous microservice components.
- AWS ECS Fargate: Provides serverless container orchestration with independent scaling capabilities.
- Amazon ElastiCache (Redis) Global Datastore: Enables low-latency cross-region caching, rate fallbacks, and multi-region replication across `us-east-1`, `eu-west-1`, and `ap-southeast-1`.
- AWS Secrets Manager: Secures external financial API credentials with automated rotation.
- gRPC with mTLS: Secures internal service-to-service communication.

## Rationale
Decomposing the service isolates third-party API dependencies from checkout traffic, protecting gross merchandise value through circuit breakers and stale-rate caching. Zero-persistence in-memory localization guarantees strict GDPR and CCPA compliance.