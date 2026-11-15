## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for a mid-size payment processor and provides case management for fraud analysts. It operates on AWS (`eu-west-1`) to meet PCI-DSS Level 1 compliance while respecting strict budget and team constraints.

## Key Elements
* **Real-Time Payment Fraud Screening System**: Core software system processing authorizations and managing cases.
* **Payment Gateway / Acquirer**: External system sending authorization requests.
* **Fraud Analyst**: User reviewing suspicious transactions.
* **Card Networks & Fraud Intelligence Feeds**: External systems providing risk signals and blacklists.
* **Archival / Compliance Storage**: External AWS S3 and KMS services for 7-year auditability.

## Relationships
* Payment Gateway -> Fraud Screening System via HTTPS / gRPC for real-time scoring.
* Fraud Analyst -> Fraud Screening System via HTTPS (TLS 1.3) for case management.
* Fraud Screening System -> Archival Storage via AWS SDK (TLS) for WORM audit logs.
* Fraud Screening System -> AWS Compliance/Security Services via HTTPS for KMS envelope encryption.

## Technology Stack
* **AWS (`eu-west-1`)**: Cloud provider hosting managed services within a €25,000/month budget.
* **AWS S3 with Object Lock**: Provides tamper-evident, write-once-read-many (WORM) storage for 7-year audit retention.
* **AWS KMS**: Handles card data tokenization and envelope encryption to ensure analysts never see full card numbers.
* **gRPC / HTTPS**: Protocols ensuring decision latency below 50 ms at P99 under 3,000 req/sec.

## Rationale
This architecture offloads operational overhead of PCI-DSS compliance and auditability to AWS managed services, enabling a three-engineer team to maintain the system securely. Using high-performance protocols and managed AWS primitives ensures strict performance, availability, and strict compliance targets are met within budget.