## Overview
[The Real-Time Payment Fraud Screening platform evaluates card-not-present payment authorizations for fraud to protect revenue while enabling manual case review. It is engineered for a mid-size payment processor to meet strict PCI-DSS Level 1 compliance and 7-year auditability.]

## Key Elements
* **Users:** Cardholder, Fraud Analyst, Risk/Fraud Operations Manager
* **External Systems:** Payment Gateway
* **Containers:** API Gateway, Scoring Engine Container, Case Management Container, Redis Cache, S3 Glacier Object Lock Storage
* **Technologies:** AWS ECS (Fargate), AWS ElastiCache Serverless, AWS S3 Glacier with Object Lock, AWS KMS, AWS Cognito

## Relationships
* **Payment Gateway to API Gateway:** Sends payment authorization requests via HTTPS using mTLS and TLS 1.3.
* **API Gateway to Scoring Engine Container:** Routes scoring requests over internal VPC networking.
* **Scoring Engine Container to Redis Cache:** Queries cached fallback ruleset over isolated VPC subnet during outages (R-07).
* **Scoring Engine Container to S3 Glacier:** Writes cryptographically signed audit logs using AWS KMS envelope encryption.
* **Fraud Analyst / Manager to Case Management Container:** Accesses review UI and operational metrics via OAuth2/OIDC and AWS Cognito authentication.

## Technology Stack
* **AWS ECS (Fargate):** Selected for container orchestration to ensure zero-downtime rolling updates (R-03) with minimal operational overhead for a 3-person team.
* **AWS ElastiCache Serverless:** Powers the Redis degraded-mode fallback cache to support R-07 without manual cluster management.
* **AWS S3 Glacier with Object Lock:** Implements tamper-evident storage for 7-year audit logs (R-06) within budget limits.
* **AWS KMS:** Provides envelope encryption for cryptographic signing of decision audit logs.
* **AWS Cognito:** Manages user authentication and role-based access control (RBAC) for analysts and managers.

## Rationale
[The serverless-managed AWS architecture minimizes operational burden for a three-engineer team while strictly enforcing budget and compliance constraints. Decoupled tokenized boundaries and isolated audit logging ensure PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.]