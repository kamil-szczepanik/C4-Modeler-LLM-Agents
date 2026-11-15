## Overview
[Real-Time Payment Fraud Screening system screens card-not-present payment authorizations and manages suspicious fraud cases. Core purpose is low-latency scoring coupled with 7-year tamper-evident auditability.]

## Key Elements
* Fraud Analysts
* External Payment Gateway
* API Gateway / Ingestion Service
* Scoring Engine
* Case Management & Admin UI
* Amazon S3 with Object Lock
* Amazon SQS
* AWS ECS with Fargate

## Relationships
* External Payment Gateway -> API Gateway / Ingestion Service [HTTPS/REST]
* API Gateway / Ingestion Service -> Scoring Engine [gRPC/Protobuf]
* Scoring Engine -> Amazon S3 with Object Lock [AWS SDK / Asynchronous Batching]
* Fraud Analysts -> Case Management & Admin UI [HTTPS]

## Technology Stack
* AWS ECS with Fargate: Hosts containerized services with minimal operational overhead for a 3-engineer team.
* Amazon S3 with Object Lock: Provides WORM compliance-mode storage for 7-year tamper-evident audit logs within a 25,000 EUR budget.
* Terraform: Codifies cloud infrastructure, IAM policies, and lifecycle configurations to prevent manual drift.
* AWS SDK: Handles asynchronous batching and flushing of cryptographically chained audit logs.

## Rationale
[This architecture uses asynchronous batching and local durable fallback to maintain strict P99 latency below 50 ms without violating compliance. Compliance-mode S3 Object Lock and cryptographic chaining ensure 7-year tamper-evident auditability within the fixed infrastructure budget and small engineering team constraints.]