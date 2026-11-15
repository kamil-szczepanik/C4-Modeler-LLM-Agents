## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud within sub-50ms latency while supporting secure case management and 7-year tamper-evident audits. It operates on AWS within a 25,000 EUR monthly budget, maintaining PCI-DSS Level 1 compliance for a three-engineer team.

## Key Elements
* Payment Gateway / Core Processing Engine
* Real-Time Payment Fraud Screening System (AWS-hosted)
* Fraud Analyst, ML Engineer / Data Scientist, and Finance / Operations Manager
* Card Schemes / Identity Providers
* Archival Storage / Compliance Ledger

## Relationships
* Payment Gateway to Screening System: Synchronous gRPC over mTLS
* Fraud Analysts, ML Engineers, Finance Managers to Screening System: HTTPS via OIDC/OAuth2 with RBAC/MFA
* Screening System to Archival Storage / Compliance Ledger: Asynchronous, cryptographically signed event streams (AWS Kinesis to S3 Object Lock)

## Technology Stack
* AWS (eu-west-1): Managed cloud infrastructure fitting the €25k monthly budget and supporting a 3-engineer team
* gRPC over mTLS: Low-latency, secure machine-to-machine communication for sub-50ms P99 scoring
* OIDC/OAuth2: Standardized identity federation and access control for internal users
* AWS Kinesis and S3 Object Lock: Scalable event streaming and write-once-read-many storage ensuring 7-year tamper-evident auditability

## Rationale
Managed AWS services minimize operational overhead, enabling a three-engineer team to maintain the platform within strict budget limits. Decoupled synchronous scoring and asynchronous auditing satisfy high-throughput performance demands while strictly enforcing PCI-DSS Level 1 compliance and 7-year non-repudiation.