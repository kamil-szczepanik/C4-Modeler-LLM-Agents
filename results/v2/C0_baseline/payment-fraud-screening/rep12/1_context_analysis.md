## Overview
The system is a real-time payment fraud screening engine that evaluates payment authorizations and provides case management for fraud analysts. Its core purpose is to prevent fraudulent transactions while maintaining strict latency and compliance standards.

## Key Elements
- Payment Processor Systems / Acquirer
- Fraud Analysts and Risk Managers
- Fraud Screening Engine (AWS-hosted distributed service)
- AWS KMS, CloudTrail, and AWS Secrets Manager
- Amazon S3 with Object Lock

## Relationships
- Payment Processor Systems to Fraud Screening Engine via gRPC over mTLS (R-01, R-04)
- Fraud Analysts and Risk Managers to Fraud Screening Engine via HTTPS over TLS 1.3 (R-02, R-03)
- Fraud Screening Engine to AWS KMS via AWS SDK for data encryption (R-05)
- Fraud Screening Engine to Amazon S3 via AWS SDK for audit log storage (R-06)

## Technology Stack
- AWS ECS (Fargate): Chosen for immutable infrastructure and zero-downtime model updates.
- gRPC over mTLS: Selected to meet sub-50ms P99 latency at 3,000 TPS.
- Amazon S3 with Object Lock: Used for cost-effective, 7-year tamper-evident audit storage.
- AWS KMS: Implemented for envelope encryption and data-at-rest protection.

## Rationale
This architecture utilizes fully-managed AWS services to operate efficiently within a three-engineer team constraint and a strict 25,000 EUR monthly budget. It meets PCI-DSS Level 1 compliance and low-latency performance requirements through optimized protocols and robust cloud security controls.