## Overview
[Real-Time Payment Fraud Screening System] screens card-not-present payment authorizations for fraud at 3,000 TPS while supporting analyst case reviews. It enforces PCI-DSS Level 1 compliance and 7-year tamper-evident auditability within a €25k/month AWS budget.

## Key Elements
* Payment Gateway / Core Processing Platform
* Fraud Analyst
* Compliance Officer / Auditor
* Cardholder
* Identity Provider (IdP)
* AWS Cloud Services (eu-west-1)

## Relationships
* Payment Gateway to Real-Time Payment Fraud Screening System via gRPC over TLS 1.3
* Fraud Analyst to Real-Time Payment Fraud Screening System via HTTPS (Web-based UI)
* Compliance Officer to AWS S3 via HTTPS
* Real-Time Payment Fraud Screening System to Identity Provider via OAuth2/OIDC

## Technology Stack
* AWS ECS/EKS Fargate: Managed container orchestration to minimize operational overhead for a 3-engineer team.
* AWS S3 with Object Lock: Provides cost-effective, tamper-evident 7-year audit retention (Compliance Mode).
* Envoy Sidecar: Implements lightweight circuit-breaking for rapid fail-open handling (R-07).
* AWS Secrets Manager: Secures internal credentials with automated rotation.
* AWS Distro for OpenTelemetry: Implements tail-based sampling to manage monitoring costs under the €25k budget.

## Rationale
The architecture prioritizes managed cloud services and strict boundary definitions to maintain PCI-DSS Level 1 compliance with only three engineers. Protocol and caching decisions ensure sub-50ms P99 latency at 3,000 TPS while respecting the fixed monthly infrastructure budget.