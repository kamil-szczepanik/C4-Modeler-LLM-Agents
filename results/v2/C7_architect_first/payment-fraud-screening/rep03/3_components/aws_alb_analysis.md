## Overview
AWS ALB acts as the secure entry point and traffic router for the real-time payment fraud screening platform in `eu-west-1`. It terminates client connections, enforces security policies, and routes authorized payment payloads to downstream microservices.

## Key Elements
* AWS ALB Native Listener with ACM: Terminates TLS 1.3 and enforces mTLS via AWS Private CA.
* AWS WAF: Provides L7 threat inspection, DDoS protection, and rate-limiting.
* AWS ALB Target Groups: Handles path-based routing, connection draining, and circuit-breaker health checks.
* S3 Bucket with Object Lock: Stores immutable ALB access logs for compliance.

## Relationships
* Payment Gateway -> AWS ALB Native Listener: Ingress traffic via HTTPS / TLS 1.3 with mTLS [mTLS/HTTPS]
* AWS ALB Native Listener -> AWS WAF: Inspects decrypted L7 payloads [Internal]
* AWS ALB Target Groups -> Fraud Scoring Engine: Forwards sanitized traffic with internal TLS 1.3 [HTTP/2 over gRPC]
* AWS ALB -> S3 Bucket: Streams access logs for auditability [HTTPS]

## Technology Stack
* AWS ALB: Selected for managed scalability, sub-millisecond routing overhead, and native integration with security services.
* AWS ACM & Private CA: Chosen to automate certificate lifecycle management and enforce robust mTLS.
* AWS WAF: Deployed to mitigate L7 attacks, credential stuffing, and control cloud infrastructure costs.
* Amazon S3 Object Lock: Utilized to guarantee tamper-evident, 7-year audit logging required for compliance.

## Rationale
This architecture achieves sub-50ms P99 decision latencies and strict PCI-DSS Level 1 compliance by offloading transport security and routing to managed AWS edge services. It operates efficiently within a 25,000 EUR monthly budget while supporting a 3-engineer team through automated health checks, zero-downtime deployments, and immutable audit logging.