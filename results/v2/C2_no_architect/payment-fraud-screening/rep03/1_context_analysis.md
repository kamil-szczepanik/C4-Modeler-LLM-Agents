## Overview
[A real-time payment fraud screening system that evaluates card-not-present transactions for a mid-size payment processor and provides case management for fraud analysts.]
[The system ensures PCI-DSS Level 1 compliance, maintains sub-50ms P99 latency at 3,000 TPS, and provides 7-year tamper-evident auditability within a 25,000 EUR monthly AWS budget in eu-west-1.]

## Key Elements
* **Payment Gateway / Processing Engine:** External system submitting payment authorizations via mTLS.
* **Fraud Analyst:** Internal user reviewing suspicious transactions via case management UI.
* **Risk Manager / Data Scientist:** Internal user updating rules and models without downtime.
* **Compliance & Audit Officer:** Internal user auditing 7-year tamper-evident transaction logs.
* **API Gateway / ALB:** Ingress point handling OAuth2/OIDC token validation and TLS 1.3.
* **Scoring Engine:** Core container evaluating transactions with cached heuristic fallback.
* **Case Management UI:** Interface for fraud analysts with strict data masking.
* **Audit & Ledger Storage:** AWS QLDB and Amazon S3 Glacier for 7-year retention.

## Relationships
* **Payment Gateway -> API Gateway / ALB:** Submits payment authorization requests using mTLS and HTTPS (TLS 1.3).
* **API Gateway / ALB -> Scoring Engine:** Routes authorization scoring requests via internal VPC protocols.
* **Scoring Engine -> Audit & Ledger Storage:** Writes cryptographically secured decision logs using AWS KMS and Amazon QLDB.
* **Fraud Analyst -> Case Management UI:** Accesses case management via HTTPS with OIDC/SAML and hardware-token MFA.
* **Risk Manager -> Scoring Engine:** Updates fraud models and rules via secure administrative APIs.

## Technology Stack
* **Cloud Provider:** AWS (eu-west-1 region) chosen for managed services and predictable regional pricing.
* **Compute:** AWS ECS Fargate chosen to maintain operations with a 3-engineer team without managing Kubernetes.
* **Database & Ledger:** Amazon DynamoDB for low-latency scoring state and Amazon QLDB for tamper-evident audit logs.
* **Security & Encryption:** AWS KMS with customer-managed keys (CMK), TLS 1.3, and mTLS for strict data protection and PCI-DSS compliance.
* **Storage Archiving:** Amazon S3 Glacier for cost-effective 7-year log retention within the 25,000 EUR monthly budget.

## Rationale
[Serverless and managed AWS primitives eliminate operational overhead, allowing a 3-engineer team to maintain high availability and sub-50ms P99 latency at 3,000 TPS within budget.]
[Cryptographic ledger storage and strict tokenization satisfy PCI-DSS Level 1 and 7-year tamper-evident auditability requirements without compromising checkout speed.]