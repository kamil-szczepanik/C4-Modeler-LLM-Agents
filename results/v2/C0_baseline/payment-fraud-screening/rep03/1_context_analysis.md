## Overview
Real-Time Payment Fraud Screening system for a mid-size payment processor that evaluates card-not-present transactions for fraud, and provides case management for analysts. It operates within AWS eu-west-1 with strict PCI-DSS Level 1 compliance, sub-50ms P99 latency, and a 25,000 EUR monthly budget.

## Key Elements
* Payment Gateway / Processing Engine (External Actor): Submits authorization requests.
* Fraud Analyst / Risk Manager (External Actors): Perform case reviews and update fraud rules.
* Identity Provider (External System): Manages OIDC/OAuth2 authentication and MFA.
* Payment Card Network / Tokenization Vault (External System): Provides tokenized card data.
* Real-Time Payment Fraud Screening System (AWS Software System): Core scoring and case management platform.
* Secure Audit Archive (External System): Cold storage for tamper-evident retention.

## Relationships
* Payment Gateway to Fraud Screening System: Submits card-not-present authorizations via gRPC over TLS (mTLS) for sub-50ms scoring.
* Fraud Analysts to Fraud Screening System: Interacts via HTTPS (Web UI) protected by OIDC/OAuth2 for case management and rule updates.
* Fraud Screening System to Tokenization Vault: Resolves payment tokens via mTLS/HTTPS to enforce PCI-DSS scope reduction.
* Fraud Screening System to Secure Audit Archive: Writes decisions, model versions, and inputs via AWS SDK/S3 API using S3 Object Lock.
* Fraud Analysts/Risk Managers to Identity Provider: Authenticates via OIDC/OAuth2 over HTTPS with mandatory MFA.

## Technology Stack
* AWS Fargate on ARM64 (Graviton): Runs containerized workloads to optimize performance-per-dollar and maintain the 25,000 EUR budget.
* AWS Network Load Balancer (NLB): Handles gRPC traffic routing with strict health checks and automated 1-minute fail-open caching.
* AWS KMS: Cryptographically signs fallback tokens using short-lived asymmetric keys to prevent replay attacks during outages.
* AWS S3 Object Lock (Compliance Mode): Ensures tamper-evident 7-year auditability of decisions, model versions, and inputs.
* AWS CloudWatch & Managed Prometheus/Grafana: Provides distributed tracing (X-Ray) and metrics without self-hosted operational overhead.

## Rationale
The architecture prioritizes a managed AWS serverless/container approach (Fargate, S3, KMS) to support a 3-engineer team within a 25,000 EUR monthly budget. Using gRPC/mTLS, AWS NLB, and cryptographic fallback caches satisfies sub-50ms P99 latency and 1-minute fail-open availability requirements while strictly maintaining PCI-DSS Level 1 compliance and 7-year auditability.