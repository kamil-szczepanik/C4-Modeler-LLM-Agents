## Overview
- Real-Time Payment Fraud Screening system screens card-not-present payment authorizations and manages fraud analyst reviews.
- Designed for PCI-DSS Level 1 compliance, sub-50ms P99 latency at 3,000 TPS, and 7-year immutable auditability within a 25,000 EUR/month budget.

## Key Elements
- Cardholder / End Customer
- Fraud Operations Analyst
- AWS Application Load Balancer (ALB)
- AWS WAF
- Scoring Container (AWS ECS Fargate)
- Case Management Container (AWS ECS Fargate)
- Amazon S3 with Object Lock
- AWS IAM Identity Center

## Relationships
- Cardholder / End Customer -> AWS ALB: Submits payment authorizations [HTTPS / TLS 1.3]
- Fraud Operations Analyst -> AWS ALB: Accesses case management portal [HTTPS / OIDC via IAM Identity Center]
- AWS ALB -> AWS WAF: Inspects requests for volumetric and injection attacks [In-line filtering]
- AWS ALB -> Scoring Container: Routes payment traffic with priority rules [ECS Service Connect / mTLS]
- AWS ALB -> Case Management Container: Routes analyst UI traffic [Internal TLS]
- AWS ALB -> Amazon S3: Streams access logs with Object Lock [HTTPS / S3 API]

## Technology Stack
- AWS Application Load Balancer: Entry point providing path-based routing, weighted target groups for canary deployments, and TLS 1.3 termination.
- AWS WAF: Provides rate-based rules and managed rule sets to protect against DDoS and injection attacks within budget.
- AWS ECS Fargate: Runs containerized scoring and case management workloads without server provisioning overhead.
- Amazon S3 with Object Lock: Ensures tamper-evident storage of access logs and audit trails for 7 years.
- AWS IAM Identity Center: Secures analyst authentication and session authorization via OIDC and JWT validation.

## Rationale
- The architecture uses managed AWS services like ALB, WAF, and ECS Fargate to handle 3,000 TPS under strict cost constraints.
- Security and compliance controls—such as TLS 1.3, S3 Object Lock, and IAM Identity Center—satisfy PCI-DSS Level 1 and 7-year audit requirements.