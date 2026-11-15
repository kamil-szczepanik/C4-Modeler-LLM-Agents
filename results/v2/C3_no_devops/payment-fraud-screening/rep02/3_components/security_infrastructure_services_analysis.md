## Overview
[Security & Infrastructure Services manages authentication, secrets, asynchronous auditing, and tamper-evident storage for the real-time fraud screening system on AWS eu-west-1.]

## Key Elements
*   **Authentication & Identity Component**: AWS Cognito (OIDC/OAuth2 tokens, MFA)
*   **Secrets & Vault Component**: AWS Secrets Manager (automated rotation)
*   **Audit & Tamper-Evident Storage Component**: Amazon S3 with Object Lock (Compliance Mode) and Glacier Flexible Archive
*   **Asynchronous Ingestion Bus**: Amazon SQS with AWS KMS SSE
*   **Monitoring & Alerting**: AWS CloudTrail and Amazon EventBridge

## Relationships
*   **Fraud Analysts** -> **Authentication & Identity Component**: Authenticates via HTTPS/TLS 1.3 [OIDC/OAuth2]
*   **Real-Time Scoring Engine** -> **Asynchronous Ingestion Bus**: Publishes asynchronous audit logs [HTTPS/TLS 1.3, IAM Signed SQS]
*   **Asynchronous Ingestion Bus** -> **Audit & Tamper-Evident Storage Component**: Persists immutable transaction payloads [AWS SDK]
*   **Secrets & Vault Component** -> **Real-Time Scoring Engine & Case Management Backend**: Injects credentials [Secure Local IPC]
*   **Monitoring & Alerting** -> **Engineering Team**: Triggers anomaly alerts [Amazon EventBridge]

## Technology Stack
*   **AWS Cognito**: Manages user access with mandatory MFA to protect analysts and satisfy PCI-DSS.
*   **AWS Secrets Manager**: Stores and rotates database/service credentials every 90 days via Lambda templates.
*   **Amazon S3 Object Lock (Compliance Mode)**: Guarantees tamper-evident 7-year audit storage without human overrides.
*   **Amazon S3 Glacier Flexible Archive**: Reduces long-term storage costs by over 70% after 90 days.
*   **Amazon SQS**: Decouples the scoring engine to preserve the <50ms latency constraint.
*   **AWS KMS**: Provides customer-managed encryption keys for secure message transport.

## Rationale
[Fully managed AWS services eliminate maintenance overhead for a three-person team while meeting strict PCI-DSS Level 1 and 7-year auditability mandates. Lifecycle policies and managed scaling respect the 25,000 EUR monthly budget constraint.]