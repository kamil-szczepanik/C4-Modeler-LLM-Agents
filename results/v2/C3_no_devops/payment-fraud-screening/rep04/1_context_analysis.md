## Overview
The Real-Time Payment Fraud Screening System screens card-not-present payment authorizations for fraud within strict latency limits while providing case management for analysts. It ensures PCI-DSS Level 1 compliance and 7-year tamper-evident auditability within a fixed budget and small engineering team.

## Key Elements
* **Payment Processor (External):** Sends transaction authorizations via gRPC.
* **Fraud Analyst & Risk Manager (Users):** Access case management and rule update interfaces via HTTPS.
* **Compliance / Auditor (User):** Queries audit logs for merchant support and compliance.
* **Identity Provider (External):** Manages user authentication via AWS Cognito (OIDC).
* **API Gateway / ALB (Container):** Enforces perimeter security, tokenization, and mTLS.
* **Scoring Engine (Container):** Evaluates transactions against fraud models in an isolated VPC.
* **Case Management Service (Container):** Handles analyst review workflows.
* **Amazon S3 Object Lock & AWS KMS (Containers):** Provides WORM storage with envelope encryption for audit logs.

## Relationships
* **Payment Processor to API Gateway:** Sends authorization requests via gRPC over mTLS (<50ms P99 latency).
* **Users to API Gateway:** Accesses case management, rule updates, and reporting via HTTPS over public internet.
* **API Gateway to Identity Provider:** Authenticates users via OIDC.
* **Scoring Engine to S3 & KMS:** Writes tamper-evident decision logs using client-side envelope encryption.

## Technology Stack
* **AWS (eu-west-1):** Cloud provider chosen for managed services to fit the 3-engineer constraint.
* **gRPC / mTLS:** Used for high-throughput, low-latency communication with payment processors.
* **Amazon S3 Object Lock (Compliance Mode) & AWS KMS:** Implemented for tamper-evident, 7-year WORM audit storage.
* **AWS Cognito:** Provides managed OIDC authentication satisfying PCI-DSS access controls.

## Rationale
This architecture uses managed AWS services to minimize operational overhead for a three-engineer team within a 25,000 EUR monthly budget. Isolated VPCs, strict tokenization boundaries, and S3 Object Lock guarantee PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.