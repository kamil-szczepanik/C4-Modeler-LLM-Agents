## Overview
Real-Time Payment Fraud Screening screens card-not-present payment authorizations for a mid-size payment processor before approval and provides case management for suspicious payments. It ensures PCI-DSS Level 1 compliance and 7-year tamper-evident auditability within a 25,000 EUR monthly budget operated by three engineers.

## Key Elements
- Cardholder / End Customer
- Fraud Operations Analyst
- Risk Manager / Quant
- Fraud Ops Team Lead / Administrator
- Engineers (Team of 3)
- AWS Application Load Balancer (ALB)
- Scoring Container (AWS ECS Fargate)
- Case Management Container (AWS ECS Fargate)
- Amazon Aurora Serverless
- Amazon S3 with Object Lock
- AWS KMS
- AWS IAM Identity Center

## Relationships
- Fraud Operations Analyst -> AWS IAM Identity Center: Authenticates via hardware-backed MFA [HTTPS / SAML 2.0]
- Risk Manager / Quant -> AWS IAM Identity Center: Authenticates via hardware-backed MFA [HTTPS / SAML 2.0]
- Fraud Ops Team Lead / Administrator -> AWS IAM Identity Center: Authenticates via hardware-backed MFA [HTTPS / SAML 2.0]
- Engineers -> AWS IAM Identity Center: Authenticates via OAuth 2.0 / OIDC token-binding [HTTPS]
- AWS IAM Identity Center -> Enterprise IdP: Federates authentication via SCIM and SAML 2.0

## Technology Stack
- AWS IAM Identity Center: Centralized access management and authentication with hardware-backed FIDO2/WebAuthn MFA to meet PCI-DSS Level 1 without custom identity plumbing.
- Terraform: Infrastructure-as-code automation for provisioning AWS SSO Admin modules and role assignments.
- Amazon CloudTrail, Amazon EventBridge & Kinesis Firehose: Continuous streaming and archival of authentication logs to Amazon S3 with Object Lock for 7-year tamper-evident auditability.
- AWS Organizations SCPs: Enforces administrative guardrails preventing manual modifications outside the Terraform pipeline.

## Rationale
Centralizing authentication through AWS IAM Identity Center with SCIM and Terraform minimizes operational overhead for the 3-person engineering team. Rigorous MFA, session limits, and automated S3 Object Lock log archival satisfy strict PCI-DSS Level 1 and 7-year auditability mandates cost-effectively.