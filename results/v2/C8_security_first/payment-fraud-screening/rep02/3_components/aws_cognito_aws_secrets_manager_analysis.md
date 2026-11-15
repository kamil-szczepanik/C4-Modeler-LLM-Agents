## Overview
The system provides real-time card-not-present payment fraud screening and case management for a mid-size payment processor. It evaluates authorization requests and supports analyst reviews under strict compliance and budget constraints.

## Key Elements
- Fraud Analyst & Risk Manager
- Payment Gateway / Acquirer
- AWS API Gateway (Ingress/TLS Termination)
- Go Scoring Engine (AWS ECS on Fargate)
- Node.js Case Management (AWS ECS on Fargate)
- Amazon SQS / EventBridge
- Amazon Aurora PostgreSQL Serverless v2
- AWS QLDB
- AWS Cognito User Pool & Identity Pool
- Secrets Vault (AWS Secrets Manager)

## Relationships
- Fraud Analyst -> AWS Cognito: HTTPS (TLS 1.3) via AWS API Gateway for OIDC/SAML authentication and federation
- Go Scoring Engine & Node.js Case Management -> AWS Secrets Manager: HTTPS over AWS PrivateLink (VPC Endpoints) using AWS SDK with IAM Task Roles
- Secrets Manager -> AWS KMS: HTTPS for encrypted storage using Customer Managed Keys (CMKs)
- API Gateway -> Go Scoring Engine & Node.js Case Management: HTTP/gRPC for secure internal routing

## Technology Stack
- AWS Cognito: Manages user authentication, federation, MFA, and 15-minute JWT generation without custom blocklist infrastructure
- AWS Secrets Manager: Secures database credentials and keys with Terraform-managed rotation and in-memory SDK caching for low latency
- Terraform: Manages infrastructure-as-code to prevent configuration drift and operational toil
- AWS CloudWatch: Monitors system health, logs, and canary synthetic transactions

## Rationale
This architecture uses native, fully managed AWS services to minimize operational toil for a three-engineer team while satisfying PCI-DSS Level 1 compliance. It maintains low latency, strict auditability, and robust security within a fixed 25,000 EUR monthly budget.