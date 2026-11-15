## Overview
Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud and manages analyst reviews. It operates within AWS eu-west-1 to process payments securely while maintaining compliance and auditability.

## Key Elements
* Fraud Analysts and Merchant Risk Managers
* AWS API Gateway / Envoy (Ingestion)
* Scoring Engine Container (Go/Rust on AWS ECS Fargate)
* Case Management Backend (Node.js/Python on ECS Fargate)
* Case Management UI (React on AWS S3 + CloudFront)
* Rule & Model Distribution Service (AWS SQS + S3)
* Audit Writer Sidecar / Async Worker (Go/Lambda)
* Amazon ElastiCache (Redis Feature Store)
* AWS QLDB / S3 Object Lock (Immutable Audit Storage)
* AWS Secrets Manager and AWS App Mesh

## Relationships
* Payment Processor to AWS API Gateway via HTTPS/gRPC
* Scoring Engine to ElastiCache via VPC peering for feature lookups
* Scoring Engine to Audit Storage via Amazon SQS for asynchronous event streaming
* Control Plane to Scoring Engine via gRPC/S3 for zero-downtime config updates
* Case Management UI to Case Management Backend via HTTPS/REST

## Technology Stack
* AWS ECS Fargate: Container orchestration chosen for low operational overhead matching the 3-engineer team constraint.
* Go or Rust: Selected for the Scoring Engine to guarantee sub-50ms P99 decision latency.
* AWS QLDB / S3 Object Lock: Provides tamper-evident storage to satisfy 7-year auditability requirements.
* React on AWS S3 and CloudFront: Delivers zero-infrastructure-overhead frontend for case management.
* Amazon ElastiCache (Redis): Enables low-latency in-memory feature lookups.

## Rationale
This architecture uses managed AWS services to minimize operational burden for a three-engineer team while respecting the 25,000 EUR monthly budget constraint. It separates high-throughput synchronous scoring from asynchronous auditing to meet stringent sub-50ms latency and PCI-DSS compliance requirements.