## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for a mid-size payment processor and provides case management for suspicious payments. It ensures high-performance fraud prevention while meeting strict regulatory, security, and auditability constraints.

## Key Elements
*   **Payment Gateway / Core Processing Platform:** Upstream external system.
*   **Identity Provider (IdP):** External authentication provider.
*   **SIEM / Compliance Archive:** External storage sink.
*   **Fraud Analyst & Risk Officer:** Internal actors.
*   **Real-Time Payment Fraud Screening System:** Core AWS-hosted system containing API Gateway, ECS Fargate scoring services, Redis cache, and S3 Object Lock storage.

## Relationships
*   **Payment Gateway to Core System:** Submits authorization requests via gRPC over mTLS.
*   **Fraud Analyst to Core System:** Manages cases and reviews transactions via HTTPS over TLS 1.3 protected by AWS WAF.
*   **IdP to Core System:** Authenticates users via OIDC / OAuth2.
*   **Core System to SIEM:** Exports compliance and audit logs asynchronously via AWS EventBridge / Kinesis.

## Technology Stack
*   **AWS ECS Fargate:** Selected for compute orchestration to minimize operational overhead for a 3-engineer team while supporting 3,000 TPS.
*   **AWS S3 with Object Lock:** Chosen for tamper-evident storage to satisfy the 7-year audit retention constraint (R-06).
*   **Redis Cache:** Deployed locally for high-performance fail-open heuristics, supporting the 1-minute availability requirement (R-07).
*   **AWS Secrets Manager:** Used for secure secret management with automatic rotation.

## Rationale
This architecture uses fully managed AWS services to stay within the 25,000 EUR monthly budget and operational capacity of a three-engineer team. It enforces strict separation of concerns, tokenization, and multi-layered resilience to satisfy PCI-DSS Level 1 compliance and sub-50ms P99 latency requirements.