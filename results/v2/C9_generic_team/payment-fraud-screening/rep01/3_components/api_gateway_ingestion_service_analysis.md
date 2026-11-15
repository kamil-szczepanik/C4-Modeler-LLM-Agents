## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud prior to approval and provides a case management interface for analysts. It operates on AWS within a strict infrastructure budget and PCI-DSS Level 1 compliance requirements.

## Key Elements
- External Payment Gateway
- API Gateway / Ingestion Service
- Scoring Engine
- Case Management & Admin UI
- Amazon S3 with Object Lock
- Amazon SQS
- AWS ECS with Fargate

## Relationships
- External Payment Gateway -> API Gateway / Ingestion Service: Sends authorization requests via HTTPS/REST
- API Gateway / Ingestion Service -> Scoring Engine: Forwards scoring payloads via gRPC/Protobuf

## Technology Stack
- Go: Selected for the API Gateway to achieve sub-50ms P99 latency at 3,000 req/s while avoiding garbage collection pauses.
- OpenAPI: Used at the edge for strict, declarative schema validation and contract-first development.
- AWS ECS with Fargate: Runs containerized services to meet the 25,000 EUR monthly budget with minimal operational overhead for a 3-engineer team.
- Prometheus: Provides managed metrics scraping for HTTP request rates and gRPC upstream latencies.

## Rationale
The architecture prioritizes high-throughput, low-latency Go microservices deployed on serverless AWS containers to satisfy strict performance and availability constraints. Strict tokenization, circuit breaking, and automated data masking ensure PCI-DSS Level 1 compliance and auditability within a small team capacity.