## Overview
An Amazon-style online bookstore providing high-performance catalogue browsing, secure checkout, and recommendations for 1M MAU. It features a microservices architecture deployed globally across three AWS regions to ensure high availability and low latency.

## Key Elements
- Shopper and Store Administrator
- AWS API Gateway & WAF
- Catalogue Service (AWS ECS Fargate)
- Search & Query Engine (Amazon ElastiCache Redis, Amazon DynamoDB)
- Product Management Service (Amazon Aurora PostgreSQL)
- Localization & Currency Service
- Event Bus (AWS EventBridge / SNS)

## Relationships
- Shopper -> AWS API Gateway: Browses catalogue and executes searches [HTTPS / REST]
- AWS API Gateway -> Catalogue Service: Routes internal traffic [gRPC with mTLS]
- Catalogue Service -> Amazon ElastiCache (Redis): Serves low-latency keyword searches [Internal VPC Connection]
- Catalogue Service -> Amazon DynamoDB: Queries fast catalogue read models [Internal VPC Connection]
- Product Management Service -> Amazon Aurora PostgreSQL: Persists administrative write models [Internal VPC Connection]
- Product Management Service -> AWS EventBridge: Publishes domain events like ProductPriceUpdated [Async JSON over VPC]

## Technology Stack
- Node.js (NestJS) or Go (Gin): Selected for high-throughput, non-blocking I/O in the Catalogue API Controller.
- AWS ECS Fargate: Provides container orchestration and auto-scaling without managing underlying EC2 instances.
- Amazon ElastiCache (Redis) & DynamoDB: Delivers sub-10ms read performance for high-traffic catalogue browsing.
- Amazon Aurora PostgreSQL: Serves as the ACID-compliant primary data store for administrative writes.
- AWS EventBridge / SNS: Powers decoupled, asynchronous event-driven state synchronization.

## Rationale
This architecture decouples public read models from administrative write models, using caching and circuit breakers to maintain sub-second response times under peak load. Multi-region AWS deployment ensures the system meets its 99.95% uptime SLA and performance targets.