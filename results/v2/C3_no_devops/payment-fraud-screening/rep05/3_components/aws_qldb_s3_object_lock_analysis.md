## Overview
The Immutable Audit Storage container uses Amazon QLDB and Amazon S3 Object Lock to ensure every payment fraud screening decision is cryptographically verifiable and retained securely. It guarantees PCI-DSS Level 1 compliance and a 7-year audit trail while maintaining cost efficiency for a small engineering team.

## Key Elements
- **Audit Ingestion Service**: AWS Lambda written in Go, receiving batched decision logs.
- **QLDB Journal Ledger**: Amazon QLDB storing structured decision metadata, model versions, and cryptographic inclusion proofs.
- **S3 Compliance Vault**: Amazon S3 with Object Lock (Compliance Mode) storing raw payload inputs.
- **AWS KMS**: Manages Customer Managed Keys (CMKs) for data encryption at rest.
- **Risk & Compliance Officers / Fraud Analysts**: External personas accessing audit logs and compliance reports.

## Relationships
- **Audit Writer Sidecar** -> **Audit Ingestion Service**: Sends batched decision logs via `Amazon SQS` and `AWS SDK (HTTPS)`.
- **Audit Ingestion Service** -> **QLDB Journal Ledger**: Stores structured journal entries using `QLDB Driver (DQL/PartiQL)`.
- **Audit Ingestion Service** -> **S3 Compliance Vault**: Stores raw payloads using `AWS SDK (HTTPS)` over `AWS PrivateLink`.
- **Audit Ingestion Service** -> **AWS KMS**: Encrypts and decrypts data via `AWS SDK (HTTPS)`.
- **Auditor / Compliance Officer** -> **QLDB / S3 Vault**: Executes cryptographic verification via `AWS Console / AWS SDK (HTTPS)`.

## Technology Stack
- **Amazon QLDB**: Chosen for immutable, cryptographically verifiable transaction metadata.
- **Amazon S3 Object Lock (Compliance Mode)**: Chosen to enforce Write-Once-Read-Many (WORM) storage for raw payloads.
- **AWS Lambda (Go)**: Chosen for serverless, low-overhead event processing managed by three engineers.
- **AWS KMS**: Chosen for encryption at rest using Customer Managed Keys with annual key rotation.
- **S3 Glacier / Lifecycle Rules**: Chosen to transition data to deep archival tiers to remain under the 25,000 EUR monthly budget.

## Rationale
This architecture uses serverless managed AWS services to minimize operational overhead for a three-engineer team while strictly satisfying PCI-DSS Level 1 and 7-year auditability mandates (R-06). Cost constraints are respected through automated S3 Glacier lifecycle transitions.