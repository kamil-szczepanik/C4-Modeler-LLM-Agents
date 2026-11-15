## Overview
This system provides real-time fraud screening for card-not-present payment authorizations to approve, decline, or flag suspicious transactions. It maintains PCI-DSS Level 1 compliance while supporting low-latency decision-making and human case management.

## Key Elements
* **Payment Merchants / End Consumers**: External users initiating transactions.
* **Fraud Analysts & Risk/Compliance Officers**: Internal personnel reviewing flagged cases and ensuring regulatory compliance.
* **Risk / Data Scientists**: Internal users updating fraud rules and ML models.
* **Real-Time Payment Fraud Screening System**: Core AWS-hosted system processing authorizations and case reviews.
* **Payment Gateway / Acquirer**: External system submitting authorization requests.
* **Card Networks / Tokenization Vault**: External provider supplying tokenized card data.
* **Identity Provider (IdP)**: External system managing OAuth2/SAML authentication.

## Relationships
* **Payment Gateway -> Real-Time Payment Fraud Screening System**: HTTPS / gRPC for real-time authorization requests.
* **Fraud Analysts -> Real-Time Payment Fraud Screening System**: HTTPS via TLS 1.3 for the Case Management UI.
* **Real-Time Payment Fraud Screening System -> Tokenization Vault / IdP**: HTTPS via mTLS for token resolution and authentication.
* **Risk / Data Scientists -> Real-Time Payment Fraud Screening System**: HTTPS / AWS IAM for secure model and rule artifact deployment.

## Technology Stack
* **AWS**: Cloud provider hosting containerized workloads within budget constraints.
* **AWS ECS**: Container orchestration for running scalable screening services.
* **ONNX Runtime / TorchScript**: Embedded model runtimes for low-latency ML inference.
* **AWS S3 Object Lock**: WORM-configured storage ensuring tamper-evident, 7-year audit logging.
* **Redis**: In-memory caching for feature stores using AWS KMS encryption.

## Rationale
The architecture prioritizes sub-50ms P99 latency at 3,000 TPS by embedding lightweight inference runtimes and utilizing optimized AWS container infrastructure. Security controls like tokenization and WORM storage ensure PCI-DSS Level 1 compliance and immutable auditing within budget and team limits.