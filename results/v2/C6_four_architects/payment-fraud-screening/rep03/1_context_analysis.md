## Overview
The Real-Time Payment Fraud Screening System processes card-not-present payment authorizations in AWS (`eu-west-1`) to detect fraud and support analyst reviews. It balances strict sub-50ms P99 latency requirements at 3,000 TPS with PCI-DSS Level 1 compliance and a 7-year immutable audit constraint.

## Key Elements
- Payment Gateway / Core Ledger (Source of authorization requests)
- Fraud Analysts (System users for case management)
- Card Schemes / Issuer 3DS Directory Servers (EMVCo 3DS 2.x APIs)
- ML Feature Store / Threat Intelligence Provider (External IP/device fingerprinting APIs)
- Identity Provider (IdP for authentication and RBAC)
- Notification Service (Email/SMS alerts)
- Model Training & Experimentation Environment (Amazon SageMaker Studio)
- AWS CloudFront & ALB (Perimeter ingress)
- AWS KMS & S3 Object Lock (Cryptographic audit and storage)

## Relationships
- Payment Gateway to System: Ingress via gRPC over HTTP/2 with mTLS (3,000 TPS)
- Fraud Analysts to CloudFront/ALB: Ingress via HTTPS (TLS 1.3) with AWS WAF protection
- System to Card Schemes / Feature Store: Outbound egress via HTTPS
- System to S3 Object Lock / KMS: Tamper-evident 7-year audit logging and encryption via AWS IAM policies
- Training Environment to System: Secure, signed model artifact transfer via AWS S3 Cross-Account Policies

## Technology Stack
- AWS (`eu-west-1`): Cloud infrastructure provider chosen for managed compliance and regional data residency
- gRPC over HTTP/2: Low-latency transport protocol meeting the <50ms P99 SLA at 3,000 TPS
- AWS CloudFront, ALB & WAF: Perimeter security, TLS 1.3 termination, and DDoS mitigation
- AWS KMS & S3 Object Lock: Tamper-evident, immutable 7-year audit data storage (R-06)
- Amazon SageMaker Studio: Out-of-band model development and zero-downtime updates (R-03)
- AWS Secrets Manager: Automated credential rotation for PCI-DSS compliance

## Rationale
This architecture uses managed AWS services to meet stringent PCI-DSS Level 1 compliance and 7-year auditability constraints without exceeding a three-engineer team capacity. High-throughput gRPC communication and serverless edge components ensure P99 latency remains under 50 ms at 3,000 TPS within a 25,000 EUR monthly budget.