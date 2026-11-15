## Overview
The Real-Time Payment Fraud Screening System evaluates card-not-present payment authorizations for fraud prior to approval and provides a case management interface for fraud analysts. It operates on AWS (`eu-west-1`) to meet strict latency, security, and compliance constraints.

## Key Elements
*   **Payment Gateway / Core Ledger**: External system submitting tokenized payment authorizations.
*   **Fraud Analyst**: Internal persona reviewing flagged transactions.
*   **Identity Provider (IdP)**: Manages analyst authentication.
*   **Audit Archival Storage**: External system for long-term compliance storage.
*   **Fraud Screening System (Container)**: Core processing engine handling real-time scoring and case management.

## Relationships
*   **Payment Gateway -> Fraud Screening System**: Sends payment authorizations and receives approval, decline, or review decisions via synchronous gRPC/REST over TLS 1.3.
*   **Fraud Analyst -> Fraud Screening System**: Reviews suspicious payments using a secure Web UI via HTTPS.
*   **Fraud Screening System -> Identity Provider**: Authenticates analysts using OIDC/OAuth2.
*   **Fraud Screening System -> Audit Archival Storage**: Exports decision inputs, model versions, and explanations asynchronously.

## Technology Stack
*   **AWS (`eu-west-1`)**: Cloud provider hosting infrastructure within budget.
*   **gRPC / REST over TLS 1.3**: Protocol ensuring sub-50ms P99 decision latency for 3,000 TPS.
*   **AWS Cognito / IAM**: Handles Identity Provider functions for secure analyst access.
*   **AWS S3 with Object Lock**: Provides write-once-read-many (WORM) storage for 7-year tamper-evident auditability.

## Rationale
This architecture meets PCI-DSS Level 1 and 7-year auditability constraints by isolating tokenized data and leveraging immutable storage. It maintains high performance (sub-50ms P99 at 3,000 TPS) within a 25,000 EUR monthly budget using managed AWS services suitable for a three-engineer team.