## Overview
Real-Time Payment Fraud Screening screens card-not-present payment authorizations for fraud before approval and provides case management for analysts. It ensures sub-50ms P99 latency at 3,000 TPS while maintaining strict PCI-DSS Level 1 compliance.

## Key Elements
- Real-Time Scoring Engine (Go, ONNX Runtime, AWS ECS Fargate)
- Redis (ElastiCache) (Redis, AWS ElastiCache)
- AWS Aurora PostgreSQL (PostgreSQL, AWS Aurora)
- Amazon SQS
- API Gateway (Envoy) (Envoy)
- Case Management Backend (Node.js / Spring Boot)
- Web Application (React SPA, AWS S3, CloudFront)
- Audit Log Worker (Go)

## Relationships
- Real-Time Scoring Engine -> Redis (ElastiCache): Retrieves cached features and stores behavioral data using pipelined commands [TCP/RESP]
- Redis (ElastiCache) -> AWS S3: Exports automated daily RDB snapshots [HTTPS]
- API Gateway (Envoy) -> Real-Time Scoring Engine: Forwards authorization requests [HTTP/gRPC]
- Real-Time Scoring Engine -> Amazon SQS: Publishes asynchronous review and audit events [AMQP/HTTPS]

## Technology Stack
- Redis (ElastiCache): Low-latency feature caching using Hash and String data structures with `volatile-lru` eviction policy
- AWS ECS Fargate: Container orchestration for microservices, minimizing operational overhead for a 3-engineer team
- Go: High-performance systems language utilized for the scoring engine and audit log worker to meet P99 latency constraints
- PostgreSQL (AWS Aurora): Relational data store for persistent case management and tamper-evident audit logs

## Rationale
The architecture combines in-memory Redis caching with containerized Go services on AWS Fargate to effortlessly achieve the sub-50ms latency requirement at peak loads. Strict security controls, encrypted storage, and lean component sizing ensure full PCI-DSS Level 1 compliance while staying within the 25,000 EUR monthly budget for a three-engineer team.