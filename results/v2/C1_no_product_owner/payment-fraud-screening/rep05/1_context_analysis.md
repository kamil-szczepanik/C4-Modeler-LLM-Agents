## Overview
Real-Time Payment Fraud Screening System screens card-not-present payment authorizations for fraud at 3,000 TPS while supporting analyst case management. It operates in AWS eu-west-1 within a 25,000 EUR monthly budget, meeting PCI-DSS Level 1 compliance and 7-year audit retention.

## Key Elements
* Real-Time Payment Fraud Screening System (System of Interest)
* Payment Gateway / Core Processing System (External Actor)
* Fraud Analysts and ML Engineers (External Actors)
* Card Schemes / Tokenization Service (External System)
* AWS ECS Fargate, Application Load Balancer, and Global Accelerator (Containers)
* AWS S3 with Object Lock and AWS KMS (Containers/Storage)
* AWS CloudWatch and AWS X-Ray (Containers/Observability)

## Relationships
* Payment Gateway to Screening System via synchronous gRPC over TLS with mTLS and AWS IAM Signature v4 (R-01, R-04)
* Fraud Analysts to Screening System via HTTPS with RBAC, IAM/OIDC, and mandatory MFA (R-02)
* Screening System to Tokenization Service via secure API for PAN tokenization (R-05)
* Screening System to S3 Audit Archive via AWS KMS-encrypted writes with S3 Object Lock (R-06)

## Technology Stack
* AWS ECS Fargate with provisioned capacity: Guarantees sub-50ms P99 latency at 3,000 TPS without serverless cold starts
* gRPC over TLS: Minimizes serialization overhead to meet high-throughput performance requirements
* AWS S3 Object Lock (Compliance Mode) with AWS KMS: Ensures tamper-evident, 7-year audit retention
* AWS CloudWatch and AWS X-Ray: Provides low-overhead telemetry manageable by a 3-engineer team
* Local cached fallback engine: Enforces high availability without bypassing fraud checks (R-07)

## Rationale
This architecture uses managed AWS services on ECS Fargate to balance sub-50ms latency at 3,000 TPS with a 25,000 EUR monthly budget. It strictly enforces PCI-DSS Level 1 compliance and 7-year tamper-evident auditing for a 3-person engineering team.