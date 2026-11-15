## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations to approve, decline, or flag them for manual review. It maintains PCI-DSS Level 1 compliance while enforcing strict P99 latency limits and a 7-year tamper-evident audit trail.

## Key Elements
- **Payment Gateway / Acquirer**: External actor sending authorization requests.
- **Fraud Analyst & Fraud Operations Manager**: Internal users reviewing suspicious cases and monitoring metrics.
- **Risk Rule Author / Data Scientist**: Internal users managing fraud models.
- **Regulatory / Compliance Auditor**: External actor reviewing audit logs.
- **Low-Latency Scoring Engine**: Container handling real-time authorization scoring.
- **Case Management Portal**: Container handling analyst reviews and reporting.
- **AWS Infrastructure**: Cloud provider hosting ECS, EC2, S3, and Secrets Manager.

## Relationships
- **Payment Gateway to Scoring Engine**: REST/gRpC over mTLS (TLS 1.3).
- **Analysts & Managers to Case Management Portal**: HTTPS over TLS 1.3 with OAuth2/OIDC.
- **Scoring Engine to AWS S3 Object Lock**: Tamper-evident audit logging via AWS SDK.
- **Scoring Engine to Model Registry**: Secure model retrieval via HTTPS with digital signature verification.

## Technology Stack
- **AWS ECS on EC2**: Chosen for the scoring engine to maintain warm caches and meet the <50ms P99 latency SLA.
- **AWS S3 with Object Lock**: Chosen for tamper-evident audit log retention to meet the 7-year compliance mandate.
- **mTLS (TLS 1.3)**: Chosen for secure transport-layer encryption across all external and internal service boundaries.
- **AWS Secrets Manager & IAM**: Chosen to eliminate static credentials and enforce least-privilege access.

## Rationale
This architecture balances ultra-low latency and strict PCI-DSS Level 1 compliance by decoupling the high-throughput scoring engine from the case management portal. It operates reliably within a 3-engineer team and fixed 25,000 EUR monthly AWS budget.