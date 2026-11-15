## Overview
A real-time card-not-present fraud screening system processing payment authorizations with sub-50ms latency. It provides automated scoring, analyst case management, and tamper-evident 7-year audit logging.

## Key Elements
- Merchant / Payment Gateway
- Fraud Analyst
- Risk / Compliance Officer
- Real-Time Fraud Screening System
- Tokenization Provider
- Audit Archive (AWS S3 Object Lock)

## Relationships
- Merchant / Payment Gateway -> Real-Time Fraud Screening System via HTTPS / gRPC with mutual TLS (mTLS) for authorization scoring
- Fraud Analyst -> Real-Time Fraud Screening System via HTTPS with OIDC/MFA for case management
- Real-Time Fraud Screening System -> Tokenization Provider via HTTPS API for secure token resolution
- Real-Time Fraud Screening System -> Audit Archive via AWS SDK / S3 API for immutable decision trail storage

## Technology Stack
- AWS: Cloud provider in eu-west-1 region, selected for managed infrastructure primitives
- AWS Lambda / ECS Fargate: Compute layers utilizing Auto Scaling and aliases for zero-downtime model deployments
- ElastiCache Redis: Low-latency feature store ensuring sub-50ms P99 decision latency
- AWS S3 Object Lock: Tamper-evident long-term storage enforcing 7-year compliance retention
- AWS KMS / Secrets Manager: Encryption key management and automated secret rotation for PCI-DSS Level 1 compliance
- AWS X-Ray: Distributed tracing for real-time observability across services

## Rationale
Managed AWS serverless and container primitives maximize performance and availability while respecting the strict 25,000 EUR monthly budget and operating capacity of a three-engineer team. Strict architectural separation of the synchronous scoring pipeline from asynchronous case management guarantees compliance with PCI-DSS Level 1 and rigorous P99 latency SLAs.