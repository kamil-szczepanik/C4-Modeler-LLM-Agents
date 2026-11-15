## Overview
The system screens card-not-present payment authorizations for fraud in real-time and provides case management for human analysts. It processes financial transactions under strict compliance, latency, and budget constraints.

## Key Elements
- High-Performance Scoring Engine (AWS ECS on Fargate)
- Feature Store (AWS ElastiCache for Redis)
- Cold Historical Feature Storage (Amazon S3 / DynamoDB)
- Async Event Bus (AWS EventBridge / SQS)
- API Gateway / Ingestion Container (AWS API Gateway / Envoy proxy)
- Fraud Analyst (Person)

## Relationships
- API Gateway / Ingestion Container -> High-Performance Scoring Engine: Forwards authorization requests [HTTPS / gRPC]
- High-Performance Scoring Engine -> Feature Store (AWS ElastiCache for Redis): Fetches operational features using batch pipelining [Redis Protocol]
- Feature Store -> Async Event Bus: Publishes immutable point-in-time feature snapshots [AWS SDK / JSON over TLS]
- High-Performance Scoring Engine -> Cold Historical Feature Storage: Fallback lookup for historical features [HTTPS]

## Technology Stack
- AWS ElastiCache for Redis: In-memory feature store chosen for sub-millisecond retrieval latency.
- Dual-Tier Storage (Redis + S3/DynamoDB): Balances ultra-low latency operational needs with 7-year audit requirements within budget.
- Protocol Buffers & Schema Registry: Ensures strict payload serialization and prevents schema drift across services.
- AWS ECS on Fargate: Serverless container management minimizing operational overhead for a 3-engineer team.

## Rationale
This architecture achieves sub-50ms P99 latency at 3,000 requests per second using Redis pipelining and an L1 cache, while remaining within the 25,000 EUR budget through managed AWS services. It guarantees PCI-DSS Level 1 compliance and 7-year auditability via cryptographic key tokenization, immutable snapshots, and dual-tier storage.