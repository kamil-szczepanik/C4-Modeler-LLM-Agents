## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud at 3,000 transactions per second while providing case management for human analysts. It ensures sub-50ms decision latencies, strict PCI-DSS Level 1 compliance, and 7-year tamper-evident auditability within a fixed budget.

## Key Elements
- Payment Gateway / Merchants (API Client)
- Fraud Analysts and Compliance Officers
- Auditors / Regulators
- Real-Time Payment Fraud Screening System (AWS EKS Container Cluster)
- AWS API Gateway & VPC Endpoints
- AWS S3 with Object Lock and Glacier Deep Archive

## Relationships
- Payment Gateway sends authorization requests to AWS API Gateway via gRPC/REST
- Fraud Analysts access the Case Management UI via HTTPS
- System stores tamper-evident audit logs in AWS S3 using Object Lock via AWS SDK
- Auditors access compliance reports via secure export channels

## Technology Stack
- AWS EKS (eu-west-1): Provides container orchestration managed via GitOps within the 3-engineer team capacity.
- gRPC / REST: Ensures high-throughput, low-latency communication for real-time scoring (R-04).
- AWS S3 Object Lock & Glacier Deep Archive: Implements immutable 7-year storage for regulatory audit compliance (R-06) within the 25k EUR budget.
- OpenTelemetry / AWS X-Ray: Enables distributed tracing to meet the 1-minute availability fallback constraint (R-07).

## Rationale
This architecture uses single-region AWS managed services in eu-west-1 to maintain high availability and strict PCI-DSS compliance while operating within a €25,000 monthly budget. Immutable infrastructure and managed orchestration keep operational overhead minimal for a three-engineer team.