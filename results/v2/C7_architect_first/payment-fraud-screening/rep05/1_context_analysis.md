## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for a mid-size payment processor in AWS (eu-west-1) to detect fraud and manage reviews. It satisfies PCI-DSS Level 1 compliance while maintaining sub-50ms P99 latency at 3,000 TPS within a 25,000 EUR monthly budget operated by three engineers.

## Key Elements
* Payment Gateway / Acquirer Systems (External Software System)
* Fraud Analysts and Risk Operations Managers (Persons)
* Core Fraud Screening System (Target Software System)
* Card Networks / Tokenization Vault (External System)
* AWS API Gateway with built-in circuit-breaking and latency-based routing
* Immutable Audit Log Sink (AWS S3 Object Lock, AWS KMS, CloudTrail Lake)

## Relationships
* Payment Gateway -> Core Fraud Screening System: gRPC over TLS (mTLS) with strict SLA timeout contracts for real-time scoring (R-01, R-04).
* Fraud Analysts & Risk Operations Managers -> Core Fraud Screening System: HTTPS via ZTNA / identity-aware proxies with SSO for case management and reporting (R-02, R-03).
* Core Fraud Screening System -> Tokenization Vault: Secure API calls for card token validation without storing PANs (R-05).
* Core Fraud Screening System -> Immutable Audit Log Sink: Automated cryptographic log shipping and S3 Object Lock for 7-year audit retention (R-06).

## Technology Stack
* AWS (eu-west-1): Target cloud provider ensuring fixed-budget infrastructure under 25,000 EUR per month.
* gRPC over TLS (mTLS): Protocol for high-throughput, low-latency inter-system authorization scoring.
* AWS API Gateway: Manages edge ingress, cryptographic payload validation, and automated circuit-breaking for predictable degradation (R-07).
* AWS S3 Object Lock, KMS, and CloudTrail Lake: Implements tamper-evident, encrypted 7-year audit logging (R-06).
* OIDC/OAuth 2.0 with ZTNA and MFA: Secures access for internal analysts and managers while preventing unauthorized exposure of card data (R-05).

## Rationale
This architecture ensures strict regulatory compliance and tamper-evident auditability while operating reliably under tight budget and staffing constraints. By leveraging managed AWS services, it achieves high-throughput real-time performance without exceeding operational capacity.