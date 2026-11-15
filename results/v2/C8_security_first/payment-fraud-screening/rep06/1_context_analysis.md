## Overview
- Real-time payment fraud screening system for card-not-present transactions on AWS.
- Screens authorizations in under 50ms, manages analyst reviews, and ensures strict PCI-DSS compliance.

## Key Elements
- Merchant / Payment Gateway (Upstream client system)
- Fraud Analyst (Internal user managing reviews and rules)
- Fraud Screening Engine (Core AWS Fargate containerized system)
- API Gateway (Edge router with perimeter tokenization)
- AWS QLDB / S3 Object Lock (Tamper-evident audit archive)
- Card Schemes / External Enrichment APIs (External risk data sources)

## Relationships
- Merchant to API Gateway: Sends payment authorizations via HTTPS/JSON over TLS 1.3 / mTLS.
- Fraud Analyst to Fraud Screening Engine: Accesses case management via HTTPS with RBAC and MFA.
- API Gateway to Fraud Screening Engine: Internal communication using gRPC.
- Fraud Screening Engine to AWS QLDB/S3: Asynchronously writes audit logs and decision metadata.
- Fraud Screening Engine to External Enrichment APIs: Fetches auxiliary risk signals via HTTPS.

## Technology Stack
- AWS Fargate: Container execution platform minimizing management overhead for a three-engineer team.
- AWS API Gateway & Route 53: Perimeter routing enforcing tokenization, TLS 1.3, and fail-open controls.
- gRPC: Internal communication protocol ensuring P99 decision latency remains below 50 ms.
- AWS QLDB & S3 Object Lock: WORM-compliant storage guaranteeing tamper-evident 7-year auditability.
- Terraform: Infrastructure-as-Code enforcing strict budget limits under 25,000 EUR per month.

## Rationale
- The single-region AWS Fargate architecture respects the operational capacity of a three-engineer team and the 25,000 EUR monthly budget constraint. Perimeter tokenization and gRPC internals fulfill PCI-DSS Level 1 security requirements and sub-50ms latency targets.