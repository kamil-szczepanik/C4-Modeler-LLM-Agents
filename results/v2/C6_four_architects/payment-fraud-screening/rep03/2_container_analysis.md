## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud within milliseconds and manages suspicious payment reviews. It is architected as a secure, low-maintenance cloud system optimized for a three-engineer team within a fixed budget.

## Key Elements
- Fraud Analysts
- AWS Application Load Balancer (ALB)
- Scoring Engine Container
- Case Management Backend Container
- Tokenization Proxy Container
- Amazon DynamoDB
- Amazon S3 Object Lock

## Relationships
- Fraud Analysts interact with Case Management Backend via AWS ALB using HTTPS.
- AWS ALB routes external authorization traffic to Scoring Engine via HTTPS/gRPC.
- Scoring Engine communicates with external Feature Stores via gRPC.
- Scoring Engine writes hot state to Amazon DynamoDB and audit logs to Amazon S3 Object Lock via AWS SDK.
- Case Management Backend reads and writes investigation data to Amazon DynamoDB via VPC Endpoints.

## Technology Stack
- **AWS ECS Fargate:** Serverless container orchestration chosen to minimize operational overhead for a three-engineer team.
- **Go:** Programming language for the Scoring Engine to ensure sub-50ms P99 latency and predictable memory footprints.
- **ONNX Runtime:** Embedded C++ scoring engine within Go for zero-downtime model updates.
- **Node.js / TypeScript:** Backend framework for case management workflows.
- **AWS Nitro Enclaves:** Hardware-level isolation for tokenization to ensure PCI-DSS compliance and protect card data.
- **Amazon S3 Object Lock:** Compliance-mode storage ensuring tamper-evident 7-year audit retention.
- **AWS ALB Circuit Breaker:** Edge-level fail-open mechanism ensuring availability constraints during outages.

## Rationale
This architecture meets sub-50ms latency and strict PCI-DSS Level 1 security requirements by combining high-performance Go/ONNX scoring with isolated tokenization proxies. It respects budget and operational constraints by utilizing serverless AWS primitives that require minimal maintenance from a three-engineer team.