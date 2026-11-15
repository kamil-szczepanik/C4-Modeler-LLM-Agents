## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud prior to approval and provides case management for analyst reviews. It operates within AWS eu-west-1 to deliver low-latency decisions while ensuring strict compliance and security.

## Key Elements
- **Payment Processor Systems / Payment Gateway:** External actor sending authorization requests.
- **Fraud Analysts:** Internal users reviewing flagged transactions via case management.
- **Risk & Compliance Officers:** Internal users auditing tamper-evident decision logs.
- **Fraud Engineers:** Internal users updating rules and models without downtime.
- **Identity Provider (IdP):** AWS IAM Identity Center handling SSO and MFA.
- **Notification Service:** Amazon SES for analyst review alerts.
- **Audit Ledger:** AWS QLDB or WORM-configured S3 storing tamper-evident logs.

## Relationships
- **Payment Gateway to Real-Time Fraud Screening System:** REST/gRPC over mTLS and TLS 1.3 via AWS API Gateway.
- **Fraud Analysts to Fraud Screening System:** HTTPS via SSO/OIDC and RBAC.
- **Fraud Screening System to Audit Ledger:** Encrypted write operations for 7-year retention.
- **Fraud Screening System to IdP:** OIDC/SAML for authentication.

## Technology Stack
- **Cloud Provider:** AWS (eu-west-1 region) for managed infrastructure and compliance controls.
- **Inbound Transport:** REST/gRPC over mTLS via AWS API Gateway for secure, low-latency processing.
- **Security & Cryptography:** AWS Certificate Manager Private CA, AWS KMS with customer-managed keys, and AWS WAF.
- **Identity & Access Management:** AWS IAM Identity Center for SSO, MFA, and RBAC.
- **Audit & Compliance Storage:** AWS QLDB / WORM-configured S3 and AWS CloudTrail for tamper-evident logging.
- **Notifications:** Amazon SES for alerting analysts.

## Rationale
This architecture leverages managed AWS services to minimize operational overhead for a three-engineer team while staying within the 25,000 EUR monthly budget. It enforces rigorous security and audit controls to satisfy PCI-DSS Level 1 compliance and 7-year retention mandates without compromising the sub-50ms P99 latency requirement.