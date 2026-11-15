## Overview
[AWS Application Load Balancer (ALB) routes, secures, and isolates high-throughput real-time payment authorization traffic and low-volume fraud analyst workflows. It enforces PCI-DSS Level 1 compliance through strict TLS termination, WAF rate-limiting, and path-based target group separation.]

## Key Elements
* AWS Application Load Balancer (ALB) / Ingress Router
* AWS WAF v2
* Scoring Target Group (Scoring Engine Container - Rust)
* Case Management Target Group (Case Management Container - Python)
* AWS Certificate Manager (ACM) Private CA & Secrets Manager
* AWS CloudWatch & S3 (Access Logs with Object Lock)

## Relationships
* Payment Gateway / Merchant Systems -> AWS ALB: Sends authorization requests [HTTPS / mTLS (TLS 1.3)]
* Fraud Operations Analysts & Risk Managers -> AWS ALB: Accesses case management workflows [HTTPS (OAuth 2.0 / OIDC, RBAC, MFA via AWS Cognito)]
* AWS ALB -> Scoring Engine Container (Rust): Routes real-time scoring requests [gRPC over internal TLS]
* AWS ALB -> Case Management Container (Python / FastAPI): Routes analyst traffic [HTTPS (HTTP/1.1)]

## Technology Stack
* AWS Application Load Balancer (ALB): Selected for native path-based routing, target group isolation, and low-latency performance.
* AWS WAF v2: Deployed for DDoS protection and OWASP Top 10 rule enforcement to safeguard the <50ms P99 SLA.
* gRPC over internal TLS: Used for scoring traffic to minimize serialization overhead and maintain internal data-in-transit encryption.
* AWS Certificate Manager (ACM) & Secrets Manager: Automates TLS certificate rotation and secures mTLS credentials.

## Rationale
[This architecture fits the requirements by isolating latency-critical payment traffic from heavy analyst workflows, ensuring sub-50ms P99 decision latencies. It maintains PCI-DSS compliance and stringent auditability while remaining manageable for a three-engineer team within a €25,000 monthly budget.]