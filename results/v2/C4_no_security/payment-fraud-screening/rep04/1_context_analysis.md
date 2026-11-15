## Overview
Real-Time Payment Fraud Screening System screens card-not-present payment authorizations for fraud and manages analyst reviews. It operates within a financial payment processing domain on AWS (`eu-west-1`).

## Key Elements
* **Real-Time Payment Fraud Screening System:** AWS-hosted serverless platform for scoring, case management, and auditing.
* **Fraud Analyst & Risk Manager:** Internal users managing reviews and fraud rules.
* **Payment Gateway / Acquirer & Merchant Platforms:** External systems sending authorization requests.
* **Identity Provider (IdP):** AWS Cognito or Okta for OAuth2/OIDC authentication.
* **Regulatory & Notification Sink:** Immutable AWS S3 object storage vault.

## Relationships
* **Payment Gateway / Merchant** -> **Screening System:** REST/gRPC over TLS 1.3 for sub-50ms authorization requests and decisions (R-01, R-04).
* **Fraud Analyst / Risk Manager** -> **Screening System:** HTTPS via IdP for case management (R-02) and rule updates (R-03).
* **Screening System** -> **Regulatory Sinking:** AWS S3 WORM policies for 7-year tamper-evident audit logs (R-06).

## Technology Stack
* **AWS Lambda & API Gateway:** Serverless compute and ingress, chosen to eliminate OS patching and auto-scaling overhead for a 3-engineer team while meeting <50ms P99 latency (R-04).
* **AWS DynamoDB:** Low-latency data store for transaction context and scoring states.
* **AWS S3:** Write-Once-Read-Many (WORM) storage for 7-year tamper-evident audit trails (R-06).
* **AWS Cognito / Okta:** OAuth2/OIDC identity management for secure access control (R-05).
* **AWS X-Ray & CloudWatch:** Distributed tracing and structured logging for latency SLA tracking.

## Rationale
Serverless architecture minimizes operational overhead, allowing a three-engineer team to maintain the system within the €25k monthly budget. Dedicated ingress boundaries and managed storage ensure PCI-DSS Level 1 compliance and immutable auditability.