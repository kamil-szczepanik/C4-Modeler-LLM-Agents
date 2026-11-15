## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for a mid-size payment processor in AWS (eu-west-1) and provides case management for fraud analysts. It satisfies PCI-DSS Level 1 compliance while maintaining sub-50ms latency at 3,000 TPS within a €25,000 monthly budget.

## Key Elements
* **Real-Time Payment Fraud Screening System** (Software System)
* **Payment Gateway / Acquirer** (External System)
* **Fraud Analyst** (Person)
* **Card Networks & Tokenization Vault** (External System)
* **Core-Banking / Ledger System** (External System)
* **Model Training Environment** (External System)

## Relationships
* Payment Gateway -> Fraud System via **gRPC over HTTP/2** for real-time scoring
* Fraud Analyst -> Fraud System via **HTTPS** with **MFA and RBAC**
* Fraud System -> Tokenization Vault via **mTLS / HTTPS** for token resolution
* Fraud System -> Core-Banking System via **HTTPS / REST** for transaction disposition
* Model Training Environment -> Fraud System via secure model artifact ingestion using **AWS Signer / KMS** cryptographic verification

## Technology Stack
* **AWS Fargate / ECS or Serverless Containers**: Selected for managed infrastructure, minimizing operational overhead for a 3-engineer team within the €25k budget.
* **AWS S3 Object Lock**: Utilized for Write-Once-Read-Many (WORM) storage to enforce tamper-evident, 7-year auditability (R-06).
* **AWS KMS / Signer**: Implemented for cryptographic signature verification of hot-reloaded model artifacts and data encryption.
* **gRPC / HTTP/2**: Chosen for machine-to-machine communication to guarantee P99 latency below 50ms at 3,000 TPS.

## Rationale
This architecture leverages managed AWS services to fit the operational capacity of a 3-engineer team and the €25,000 monthly budget. Strict trust boundaries, cryptographic controls, and WORM storage ensure PCI-DSS Level 1 compliance and auditable 7-year retention.