## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to approve, decline, or flag suspicious transactions while managing analyst reviews. It operates within strict compliance and budgetary constraints to ensure secure, low-latency financial transaction processing.

## Key Elements
- Payment Gateway / Merchants (API Client)
- Fraud Analyst & Risk/Compliance Officer
- Real-Time Payment Fraud Screening System (AWS-hosted)
- Card Tokenization Vault (External Service)
- Identity Provider (AWS IAM / Cognito)
- Immutable Audit Sink (AWS S3 Object Lock)

## Relationships
- Payment Gateway to System: Sends authorization requests via gRPC and HTTPS using TLS 1.3 with mTLS.
- System to Card Tokenization Vault: Interfaced via outbound HTTPS APIs for tokenized data validation.
- System to AWS S3 Object Lock: Ingests decision inputs, model versions, and explanations into WORM storage using AWS KMS CMK encryption.
- System to Amazon CloudWatch & Route 53: Emits real-time health metrics and heartbeats for boundary monitoring.

## Technology Stack
- Cloud Infrastructure: AWS (`eu-west-1` region) chosen to leverage managed services within the €25,000/month budget.
- Security & Authentication: TLS 1.3 with mTLS, AES-256 encryption, and AWS IAM / Cognito for Role-Based Access Control.
- Audit & Storage: AWS S3 Object Lock configured for WORM compliance to retain immutable records for 7 years.
- Observability: Amazon CloudWatch and AWS Route 53 health checks for sub-second telemetry and boundary monitoring.

## Rationale
This architecture uses managed AWS services to satisfy PCI-DSS Level 1 compliance and tamper-evident 7-year auditability while minimizing operational overhead for a three-engineer team. Bounding the system scope and offloading edge fail-safes to upstream gateways ensures sub-50ms P99 latency at 3,000 TPS within a fixed monthly budget.