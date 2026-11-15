## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud prior to approval and provides a case management workflow for fraud analysts. It operates on AWS within a strict PCI-DSS Level 1 compliance framework.

## Key Elements
* Payment Gateway / Acquirer Systems: External actor submitting payment authorizations.
* Fraud Analysts: Internal actors reviewing suspicious transactions.
* Regulatory / Compliance Auditors: External actors verifying 7-year audit logs.
* Real-Time Payment Fraud Screening System: Core software system handling scoring and case management.
* Identity Provider (IdP): External system managing authentication and RBAC.
* External Tokenization/Vault Service: External system handling card data.

## Relationships
* Payment Gateway to Screening System: Submits authorizations via gRPC/REST over TLS.
* Fraud Analysts to Screening System: Reviews payments via HTTPS.
* Auditors to Screening System: Accesses audit records via secure export/audit portal.
* Screening System to IdP: Authenticates users via OAuth2/OIDC over HTTPS.
* Screening System to Tokenization Service: Resolves payment tokens via gRPC/mTLS.

## Technology Stack
* AWS Cloud (eu-west-1): Selected as the target infrastructure provider within the 25,000 EUR monthly budget.
* AWS Cognito: Used as the Identity Provider to minimize operational overhead for a 3-engineer team.
* gRPC and REST over TLS: Protocol for high-throughput, low-latency payment ingestion.
* HTTPS: Protocol for secure analyst web interface access.
* mTLS: Protocol for secure integration with the tokenization service.

## Rationale
This architecture separates high-throughput synchronous scoring from asynchronous analyst reviews to easily meet the 50 ms P99 latency constraint at 3,000 TPS. Leveraging AWS-managed components satisfies PCI-DSS Level 1 security and 7-year auditability requirements while respecting the limits of a small engineering team and fixed budget.