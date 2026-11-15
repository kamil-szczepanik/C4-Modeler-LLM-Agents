## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for a mid-size payment processor and manages analyst reviews. It provides automated scoring, case management, and strict compliance enforcement within AWS.

## Key Elements
- AWS API Gateway / Envoy (Ingestion Layer)
- Scoring Engine Container (Go/Rust on AWS ECS Fargate)
- Case Management Backend (Node.js/Python on ECS Fargate)
- Case Management UI (React on AWS S3 + CloudFront)
- Amazon ElastiCache (Redis Feature Store)
- AWS QLDB / S3 Object Lock (Immutable Audit Storage)

## Relationships
- Payment Processor Systems -> AWS API Gateway / Envoy: Sends payment authorizations for screening [HTTPS/gRPC]
- AWS API Gateway / Envoy -> Scoring Engine Container: Routes scoring requests [gRPC over internal VPC mTLS]
- Scoring Engine Container -> Amazon ElastiCache: Retrieves features [Redis Protocol]
- Scoring Engine Container -> AWS QLDB / S3 Object Lock: Stores audit decisions [AWS SDK / HTTPS]

## Technology Stack
- AWS API Gateway / Envoy: Handles high-throughput secure edge routing and Wasm tokenization.
- AWS ECS Fargate: Runs backend services with serverless container orchestration to meet budget limits.
- Amazon ElastiCache (Redis): Provides low-latency feature lookups for sub-50ms P99 performance.
- AWS QLDB / S3 Object Lock: Ensures tamper-evident, 7-year regulatory auditability.

## Rationale
This architecture uses serverless and managed AWS services to meet the strict 25,000 EUR monthly budget constraint while supporting 3,000 requests per second. Decoupled ECS containers and robust edge routing ensure PCI-DSS compliance and high availability.