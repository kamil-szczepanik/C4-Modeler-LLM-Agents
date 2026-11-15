## Overview
- Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud and manages case reviews for analysts.
- Operates under strict PCI-DSS Level 1 compliance with a P99 latency below 50 ms at 3,000 TPS within a 25,000 EUR monthly budget.

## Key Elements
- Fraud Analysts, Data Scientists / Risk Managers, Regulatory / Compliance Auditors
- Payment Gateway / Acquirer Systems, Card Networks / Tokenization Providers
- API Gateway (Nginx / AWS ALB)
- Fraud Scoring Engine (Go service with embedded ONNX runtime)
- Case Management Backend (Node.js / Express service)
- Model/Rule Manager (Python / FastAPI service)
- Amazon ElastiCache for Redis (Redis Engine v7.x, Cluster Proxy, AOF Persistence)
- Amazon Aurora Serverless v2
- Amazon S3
- Amazon MSK Serverless
- AWS ECS Fargate

## Relationships
- Fraud Scoring Engine -> Amazon ElastiCache for Redis: Performs real-time feature lookups [TCP over TLS]
- API Gateway -> Fraud Scoring Engine: Routes payment authorization requests [HTTPS / gRPC]
- Fraud Scoring Engine -> Amazon MSK Serverless: Publishes transaction decisions and audit payloads [Kafka Protocol]
- Case Management Backend -> Amazon Aurora Serverless v2: Persists case reviews and analyst actions [PostgreSQL Wire Protocol]

## Technology Stack
- Go (Fraud Scoring Engine): Chosen for high concurrency and low memory footprint to achieve sub-50ms latency.
- Amazon ElastiCache for Redis (Feature Store): Chosen for sub-millisecond feature lookups using `volatile-lru` eviction and TTLs.
- Amazon Aurora Serverless v2: Chosen for auto-scaling relational data storage matching variable transaction volumes.
- AWS ECS Fargate: Chosen for serverless container orchestration within a 3-engineer team capacity.

## Rationale
- The architecture uses decoupled microservices and in-memory caching to achieve high throughput and strict P99 latency targets.
- Security controls, Multi-AZ deployments, and automated failovers ensure PCI-DSS Level 1 compliance and high availability under 25,000 EUR monthly budget limits.