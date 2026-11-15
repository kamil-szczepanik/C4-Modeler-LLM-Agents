## Overview
The Real-Time Payment Fraud Screening System processes card-not-present payment authorizations in AWS (`eu-west-1`) to evaluate fraud risks and manage suspicious transaction reviews. It balances strict PCI-DSS compliance and a 7-year audit requirement within a fixed infrastructure budget and small engineering team.

## Key Elements
- **Payment Gateway / Acquirer**: External source sending authorization requests.
- **Fraud Analyst**: Internal persona reviewing flagged transactions via case management.
- **Identity Provider (IdP)**: External OIDC service handling SSO and MFA.
- **Real-Time Payment Fraud Screening System**: Core AWS container processing scoring and case management.
- **Audit Sink**: Write-only Amazon S3 bucket with Object Lock for tamper-evident storage.
- **Secrets Manager**: AWS Secrets Manager storing mTLS certificates and IdP secrets.

## Relationships
- **Payment Gateway → Fraud Screening System**: Ingests traffic using gRPC over TLS 1.3 with mutual TLS (mTLS).
- **Fraud Analyst → Fraud Screening System**: Accesses case management interfaces via HTTPS using OpenID Connect (OIDC).
- **Fraud Screening System → Audit Sink**: Streams cryptographic audit logs via HTTPS/TLS with AWS KMS encryption.

## Technology Stack
- **AWS (`eu-west-1`)**: Core cloud provider selected for regional alignment and managed service availability within budget constraints.
- **gRPC over TLS 1.3 (with mTLS)**: Selected for high-throughput, low-latency communication meeting the <50ms P99 requirement at 3,000 TPS.
- **Amazon S3 Object Lock**: Utilized to provide write-once-read-many (WORM) tamper-evident storage for the 7-year audit requirement.
- **AWS KMS**: Enforces envelope encryption with customer-managed keys for data security.
- **AWS Secrets Manager**: Automates credential and certificate rotation to minimize operational overhead for a 3-engineer team.

## Rationale
This architecture uses high-performance gRPC protocols and managed AWS services to achieve low-latency scoring at scale without exceeding the 25,000 EUR monthly budget. Strict edge tokenization, mTLS, and immutable S3 Object Lock storage satisfy PCI-DSS Level 1 and 7-year audit mandates while keeping operational complexity manageable for three engineers.