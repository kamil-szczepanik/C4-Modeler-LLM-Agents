## Overview
The system provides real-time fraud screening for card-not-present payment authorizations and case management for fraud analysts. It screens transactions with sub-50ms latency while ensuring PCI-DSS Level 1 compliance and 7-year auditability.

## Key Elements
- Fraud Analyst UI (React SPA via Amazon S3 / CloudFront)
- API Gateway & Ingress (Java / Spring Cloud Gateway)
- Real-Time Scoring Engine (Java / Spring Boot + ONNX)
- Case Management Backend (Node.js / TypeScript)
- Model & Rule Management Service (Python / FastAPI)
- Audit Worker (Node.js / Python worker)
- Amazon Kinesis Data Streams (Amazon Kinesis)
- Amazon Aurora PostgreSQL (Amazon Aurora PostgreSQL)
- Amazon ElastiCache (Amazon ElastiCache (Redis)):
  - Feature Store Cache (Redis Cluster)
  - Blacklist / Denylist Registry (Redis In-Memory Set / Hash)
  - Session & Idempotency Store (Redis Strings with TTL)
  - Real-Time Model Feature Cache (Redis Sorted Sets)
  - Tokenized Entity Cache (Redis Encrypted Hash)

## Relationships
- Real-Time Scoring Engine -> Feature Store Cache: Fetches sliding-window user velocity metrics via `RESP` over TCP
- Real-Time Scoring Engine -> Blacklist Registry: Fast membership checks via `RESP` over TCP
- API Gateway & Ingress -> Session & Idempotency Store: Validates request tokens and locks via `RESP` over TCP
- Audit Worker / Model Service -> Feature Cache: Updates real-time aggregations via `RESP` over TCP
- Real-Time Scoring Engine -> Tokenized Entity Cache: Fetches token mappings via `RESP over TLS`

## Technology Stack
- AWS (eu-west-1): Target cloud infrastructure provider
- Redis Cluster / ElastiCache: Delivers microsecond-latency feature lookups and sliding-window velocity tracking within budget
- Java / Spring Boot & ONNX: Powers high-throughput, low-latency payment scoring
- Amazon Aurora PostgreSQL: Stores auditable transaction decisions and case data

## Rationale
This architecture uses managed AWS services and in-memory caching to achieve sub-50ms latency at 3,000 TPS within a 25,000 EUR monthly budget. It enforces PCI-DSS Level 1 compliance and 7-year auditability while remaining maintainable by a three-engineer team.