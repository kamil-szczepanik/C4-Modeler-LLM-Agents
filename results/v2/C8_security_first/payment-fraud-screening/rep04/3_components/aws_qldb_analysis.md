## Overview
The system screens card-not-present payment authorizations for fraud in real time while securely managing cases for compliance analysts. It ensures tamper-evident auditability and PCI-DSS compliance within a fixed budget.

## Key Elements
- Fraud Analysts & Risk Operations
- Compliance & Audit Officer
- Envoy Proxy
- Scoring Engine Container (Go)
- Case Management API Container (Node.js / NestJS)
- Audit & Compliance Ledger Container
- Amazon ElastiCache / SQS
- Amazon Aurora PostgreSQL
- AWS QLDB (Ledger Journal Storage Component, Ion Document Storage Component, QLDB PartiQL API Component)
- Amazon S3, Amazon Athena, AWS Lambda, Amazon EventBridge

## Relationships
- Audit & Compliance Ledger Container -> AWS QLDB: Writes tamper-evident records via PartiQL API [AWS PrivateLink / TLS 1.3]
- AWS QLDB -> Amazon S3: Streams journal revisions asynchronously [AWS Lambda / EventBridge]
- Compliance & Audit Officer -> Amazon Athena: Queries historical audit data [HTTPS / IAM]
- External Payment Gateway -> Envoy Proxy: Forwards authorization requests [HTTPS / gRPC]

## Technology Stack
- AWS QLDB: Provides managed, cryptographically secure, append-only journal storage for R-06 auditability.
- Amazon S3 with Object Lock: Delivers cost-effective 7-year cold storage meeting tamper-evident compliance.
- Amazon Athena: Enables serverless SQL querying of historical JSON/Parquet audit records.
- AWS PrivateLink & IAM: Secures network transit and enforces least-privilege database access.
- Terraform: Automates infrastructure provisioning and prevents drift for the 3-person engineering team.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead for a three-engineer team while strictly enforcing PCI-DSS compliance. It guarantees 7-year tamper-evident auditability and low latency within the 25,000 EUR monthly budget constraint.