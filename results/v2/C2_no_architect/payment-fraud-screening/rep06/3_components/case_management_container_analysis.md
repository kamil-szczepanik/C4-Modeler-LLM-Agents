## Overview
This system provides real-time payment fraud screening and case management for card-not-present transactions. It ensures rapid, auditable fraud decisions while maintaining strict PCI-DSS Level 1 compliance.

## Key Elements
- Fraud Analyst
- Case Management Container
- Scoring Engine Container
- AWS S3 Object Lock Bucket
- AWS KMS

## Relationships
- Fraud Analyst -> Case Management Container: Reviews flagged transactions via HTTPS (OAuth 2.0 / OIDC JWT)
- Case Management Container -> Scoring Engine Container: Queries and manages case details via internal REST APIs (mTLS via AWS App Mesh)
- Case Management Container -> AWS S3 Object Lock: Streams cryptographically signed audit logs via AWS IAM

## Technology Stack
- AWS ECS on Fargate: Hosts containers with auto-scaling based on analyst session metrics to stay within the 25,000 EUR monthly budget
- AWS App Mesh: Automates mTLS sidecars to meet zero-trust requirements without manual certificate rotations for a 3-person team
- AWS S3 Object Lock & Glacier: Provides 7-year tamper-evident audit storage with automated lifecycle transitions
- AWS KMS: Handles cryptographic signing of audit event payloads for non-repudiation

## Rationale
This architecture balances strict PCI-DSS Level 1 security and 7-year auditability with the operational constraints of a 3-person engineering team. Automated infrastructure and risk-based security controls maximize analyst productivity while adhering to a fixed budget.