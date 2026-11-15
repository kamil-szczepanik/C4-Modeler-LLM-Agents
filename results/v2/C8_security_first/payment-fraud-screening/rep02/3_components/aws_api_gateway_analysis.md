## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud prior to approval and provides a case management interface for fraud analysts. It is operated by a three-engineer team on AWS within a 25,000 EUR monthly budget while maintaining PCI-DSS Level 1 compliance.

## Key Elements
- Payment Gateway / Acquirer (External System)
- AWS API Gateway (Ingress/TLS Termination Container)
- Go Scoring Engine (ECS Fargate Container)
- Node.js Case Management (ECS Fargate Container)
- Edge Router & WAF Integrator (API Gateway Component)
- Request Validator & Sanitizer (API Gateway Component)
- Upstream Router (API Gateway Component)

## Relationships
- Payment Gateway / Acquirer -> AWS API Gateway: Sends payment authorizations via HTTPS (TLS 1.3)
- AWS API Gateway -> Go Scoring Engine: Routes scoring requests via gRPC over mTLS using AWS VPC Links and Network Load Balancers
- AWS API Gateway -> Node.js Case Management: Routes analyst review traffic via HTTPS

## Technology Stack
- AWS API Gateway: Chosen for native edge routing, WAF integration, and low latency without cold starts
- AWS WAF: Provides rate-limiting to protect the strict <50ms P99 latency SLA against DDoS
- AWS Secrets Manager: Stores mTLS client certificates securely for internal container routing
- Terraform / AWS CDK: Used for GitOps-based infrastructure deployment to comply with audit requirements

## Rationale
This architecture uses serverless edge routing and managed container services to meet stringent <50ms P99 latency and PCI-DSS Level 1 security requirements. Lean managed AWS services keep operational overhead minimal for a three-engineer team within a strict budget.