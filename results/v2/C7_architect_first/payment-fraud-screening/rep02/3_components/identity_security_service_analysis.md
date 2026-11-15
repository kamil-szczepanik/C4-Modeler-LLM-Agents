## Overview
The Identity & Security Service manages authentication, secrets, encryption keys, and access control for the Real-Time Payment Fraud Screening system. It ensures PCI-DSS Level 1 compliance and 7-year auditability while preserving a strict sub-50ms P99 decision latency.

## Key Elements
- Authentication Component (AWS Cognito)
- Key Management Component (AWS KMS)
- Secrets Management Component (AWS Secrets Manager)
- Access Control & Policy Component (AWS IAM)
- Fraud Analysts and Compliance Auditors

## Relationships
- Fraud Analyst UI authenticates via Authentication Component using HTTPS/OIDC
- Fraud Scoring Engine and Case Management Backend retrieve secrets from Secrets Management Component via HTTPS/AWS SDK
- Access Control & Policy Component enforces IAM roles on backend containers via AWS STS/IAM API
- Audit Log Store uses Key Management Component via AWS KMS API for ledger table encryption

## Technology Stack
- AWS Cognito: Manages user authentication and short-lived JWT tokens for analysts
- AWS KMS: Handles envelope encryption, cryptographic signing, and data key caching via AWS Encryption SDK
- AWS Secrets Manager: Secures and automatically rotates database credentials and API keys
- AWS IAM: Enforces strict least-privilege service-to-service authorization and segregation of duties

## Rationale
This managed architecture secures sensitive financial data and achieves PCI-DSS Level 1 compliance with zero infrastructure overhead. Local in-memory caching of encryption keys protects the strict sub-50ms latency SLA while maintaining tamper-evident auditability.