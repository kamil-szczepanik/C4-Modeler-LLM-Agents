## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud prior to approval and provides a case management interface for fraud analysts. It operates within a single AWS region while meeting strict latency, security, and auditability constraints.

## Key Elements
* Payment Gateway / Acquirer
* Fraud Analyst & Risk Engineer
* Payment Network / Card Schemes
* Real-Time Payment Fraud Screening System (AWS Hosted)
* Audit / Compliance Archive (AWS S3 Object Lock)
* External Notification / Alerting Service (PagerDuty)

## Relationships
* Payment Gateway to Fraud Screening: Real-time authorization requests via gRPC / HTTPS with mTLS (TLS 1.3)
* Fraud Analyst to Fraud Screening: Case management and review via HTTPS (OIDC / OAuth 2.0)
* Fraud Screening to Audit Archive: Tamper-evident 7-year log storage via AWS S3 Object Lock (Compliance Mode)
* Fraud Screening to Alerting Service: Operational incident webhooks via HTTPS

## Technology Stack
* Cloud Platform: AWS (Region: `eu-west-1`) to minimize operational overhead for a 3-person team within a 25,000 EUR/month budget
* Security & Access: AWS IAM, OIDC/OAuth 2.0, and AWS NAT Gateway for least-privilege zero-trust egress filtering
* Storage & Compliance: AWS S3 Object Lock for WORM-compliant 7-year audit trails
* Monitoring: AWS X-Ray for distributed tracing and AWS Synthetics Canaries for latency probing

## Rationale
Restricting the architecture to a single AWS region with managed services ensures a 3-person team can maintain high availability within a 25,000 EUR monthly budget. Utilizing mTLS, tokenization, and WORM storage satisfies PCI-DSS Level 1 compliance and 7-year audit requirements without compromising sub-50ms latency goals.