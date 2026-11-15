## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud under 50 milliseconds while providing case management for fraud analysts. It operates within AWS eu-west-1, ensuring PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.

## Key Elements
- Payment Gateway / Shoppers (External System)
- Real-Time Scoring Engine (AWS ECS Fargate, ECS Service Connect)
- Tokenization Proxy (AWS ECS Fargate)
- Audit & Cryptographic Signer Sidecar (AWS ECS Fargate, AWS CloudHSM, AWS KMS)
- Case Management Service (AWS ECS Fargate, AWS Cognito)
- Model Management Service (AWS ECS Fargate)
- Fraud Analysts & Risk Managers (Users)

## Relationships
- Payment Gateway / Shoppers -> Real-Time Scoring Engine: Sends payment authorizations for fraud screening [HTTPS/TLS 1.3, mTLS, signed JWT]
- Real-Time Scoring Engine -> Tokenization Proxy: Tokenizes payment data [gRPC over mTLS]
- Real-Time Scoring Engine -> Audit & Cryptographic Signer Sidecar: Sends audit logs and attribution bitmasks for tamper-evident signing [Local IPC / Unix domain sockets]

## Technology Stack
- AWS ECS Fargate: Container orchestration chosen for operational simplicity with a 3-engineer team.
- AWS ECS Service Connect: Internal service mesh enforcing mTLS and zero-trust transport security.
- AWS CloudHSM & KMS: Cryptographic signing and secrets management for 7-year auditability and runtime decryption.
- AWS Application Auto Scaling (RequestCountPerTarget): Cost-optimized scaling staying within the 25,000 EUR/month budget.

## Rationale
This architecture uses serverless containers and managed AWS security services to achieve sub-50ms latency at 3,000 TPS within a strict 25,000 EUR budget. It minimizes PCI-DSS scope via tokenization proxies and ensures auditability via cryptographic sidecars managed by a three-engineer team.