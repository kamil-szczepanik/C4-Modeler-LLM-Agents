## Overview
The system screens card-not-present payment authorizations for fraud in real-time and provides case management for human analysts. It operates on AWS within a strict PCI-DSS Level 1 compliance boundary.

## Key Elements
- AWS ALB (Ingress / API Gateway) with path-based routing
- AWS WAF with core OWASP rules (applied strictly to analyst routes)
- AWS Certificate Manager (ACM) for TLS 1.3 termination
- Payment Gateway / Acquirer and Fraud Analysts (Users)
- Fraud Scoring Engine & Case Management API

## Relationships
- Payment Gateway / Acquirer -> AWS ALB (Ingress / API Gateway): Sends payment authorizations [gRPC over mTLS]
- Fraud Analysts -> AWS ALB (Ingress / API Gateway): Accesses case management workflows [HTTPS / OAuth 2.0 / OIDC]
- AWS ALB (Ingress / API Gateway) -> AWS WAF: Inspects incoming HTTP/HTTPS traffic [Internal AWS API]
- AWS ALB (Ingress / API Gateway) -> Fraud Scoring Engine: Forwards screening requests [gRPC over mTLS]
- AWS ALB (Ingress / API Gateway) -> Case Management API: Forwards case management requests [HTTPS]

## Technology Stack
- AWS Application Load Balancer: Routes traffic, terminates TLS, and enforces path-based separation to meet the 50ms P99 latency SLA.
- AWS WAF: Secures the analyst portal against web attacks while bypassing the gRPC payment path to preserve performance.
- AWS ACM: Manages TLS 1.3 certificates and automated rotation to maintain PCI-DSS compliance.
- Terraform / AWS Load Balancer Controller: Enables declarative, GitOps-managed deployments for zero-downtime updates.

## Rationale
This architecture uses a single optimized AWS ALB to stay within the 25,000 EUR monthly budget and operational capacity of a 3-person engineering team. Path-based routing and targeted WAF bypassing successfully balance strict PCI-DSS security with the mandatory <50ms P99 latency requirement.