## Overview
[System: Real-Time Payment Fraud Screening System] screens card-not-present payment authorizations for fraud before approval and provides case management for analyst reviews.

## Key Elements
• Merchant / Payment Gateway
• Fraud Analyst
• Risk & Compliance Officer
• Real-Time Payment Fraud Screening System (Target)
• Payment Processing Core / Acquirer
• Identity Provider (IdP)
• AWS Audit & Compliance Store
• Notification / Alerting Service
• AWS CloudWatch / Observability Platform
• CI/CD & Model Registry Pipeline

## Relationships
• Merchant / Payment Gateway -> Real-Time Payment Fraud Screening System via gRPC / HTTPS
• Fraud Analyst -> Real-Time Payment Fraud Screening System via HTTPS (TLS 1.3)
• Real-Time Payment Fraud Screening System -> AWS Audit & Compliance Store via HTTPS / S3 API
• Real-Time Payment Fraud Screening System -> Notification / Alerting Service via API
• Payment Processing Core -> Real-Time Payment Fraud Screening System via mTLS

## Technology Stack
• AWS (eu-west-1): Chosen for localized managed infrastructure within budget and team capacity
• gRPC: Enables low-latency communication for sub-50ms P99 responses
• OAuth2/OIDC & IdP: Secures authentication, RBAC, and hardware-backed MFA for analysts
• AWS S3 Object Lock (Compliance Mode): Ensures 7-year tamper-evident WORM audit retention
• AWS CloudWatch & AWS X-Ray: Provides centralized observability and distributed tracing

## Rationale
This architecture balances PCI-DSS compliance, strict sub-50ms performance, and a 7-year tamper-evident audit trail. It remains operable by a 3-engineer team within a 25,000 EUR monthly AWS budget.