## Overview
Real-Time Payment Fraud Screening is a cloud-native system that screens card-not-present payment authorizations for fraud and manages analyst review cases. It operates within a mid-size payment processor infrastructure to protect merchant revenue while enforcing security mandates.

## Key Elements
- Shopper / Cardholder
- Merchant
- Fraud Analyst
- Risk / Compliance Officer
- Real-Time Payment Fraud Screening System (Target)
- Payment Gateway / Acquirer (External)
- Card Networks / Identity Providers (External)
- Compliance & Audit Archival Storage (External)
- Identity Provider / IdP (External)
- Notification / Alerting Service (External)

## Relationships
- Payment Gateway to Fraud Screening System via REST/gRPC using mTLS for authorization requests and synchronous decisions
- Fraud Screening System to Compliance & Audit Storage via TLS for immutable log streaming
- Fraud Analysts and Risk Officers to Fraud Screening System via HTTPS/OIDC/SAML through IdP
- Fraud Screening System to Notification Service via HTTPS/SMTP for operational alerts

## Technology Stack
- AWS eu-west-1: Target cloud provider and single region deployment for budget control
- Amazon ECS Fargate / AWS Lambda: Container and serverless compute ensuring minimal infrastructure management for a 3-engineer team
- AWS S3 Object Lock: WORM storage tier guaranteeing 7-year tamper-evident audit log retention
- AWS Secrets Manager: Automated credential and secret rotation
- Terraform / AWS CDK: Infrastructure as Code and GitOps pipeline tooling

## Rationale
Managed AWS services eliminate operational overhead, allowing a 3-engineer team to maintain high availability and sub-50ms latency within a 25,000 EUR monthly budget. Strict single-region architecture, tokenization, and WORM storage satisfy PCI-DSS Level 1 compliance and 7-year auditability mandates.