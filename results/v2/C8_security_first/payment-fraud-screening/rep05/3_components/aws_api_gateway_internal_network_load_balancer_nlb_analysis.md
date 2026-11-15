## Overview
[Real-Time Payment Fraud Screening System screens card-not-present payment authorizations for a mid-size payment processor using AWS, ensuring sub-50ms P99 latency and PCI-DSS Level 1 compliance.]

## Key Elements
- AWS Network Load Balancer (NLB)
- AWS API Gateway (HTTP API)
- Scoring Engine Container (ECS Fargate)
- Case Management API Container (ECS Fargate)
- Fraud Analyst SPA

## Relationships
- Payment Gateway -> AWS Network Load Balancer (NLB): Ingests payment authorizations [TCP/TLS 1.3]
- AWS Network Load Balancer (NLB) -> Scoring Engine Container: Routes raw payloads [TCP over TLS 1.3 with mTLS]
- Fraud Analyst SPA -> AWS API Gateway (HTTP API): Submits management actions [HTTPS/REST]
- AWS API Gateway (HTTP API) -> Case Management API Container: Forwards authenticated traffic [HTTPS/REST]

## Technology Stack
- AWS NLB & HTTP API: Ingress routing balancing cost and performance
- AWS ECS Fargate: Container orchestration managed by a 3-engineer team via Terraform/OpenTofu
- Rust or Go: High-performance scoring engine implementation for sub-50ms latency
- AWS Private CA / Secrets Manager: Automated internal mTLS certificate rotation
- AWS CloudWatch & OpenTelemetry: Distributed tracing and metric alarms for availability tracking

## Rationale
[The dual-path routing separates high-throughput payment traffic through an NLB from management traffic via API Gateway, guaranteeing sub-50ms latency at 3,000 TPS within a 25,000 EUR monthly budget. This architecture strictly limits the PCI-DSS scope and satisfies all availability, auditability, and security constraints.]