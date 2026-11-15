## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud prior to approval and provides a web interface for fraud analysts to review suspicious transactions. It ensures sub-50ms latency, PCI-DSS compliance, and a 7-year tamper-evident audit trail within AWS `eu-west-1`.

## Key Elements
* **Payment Switch / Core Processing**: External system sending transaction streams and receiving decisions (`approve`, `decline`, `review`).
* **Merchant / Payment Gateway**: External users initiating payment authorizations via API.
* **Fraud Analysts**: Internal users accessing the system via Web UI for case management.
* **Identity Provider (IdP)**: External system providing OAuth2/OIDC authentication for analysts.
* **Model Training Environment (ML Pipeline)**: Decoupled environment pushing updated scoring models via S3.
* **Fraud Screening Core**: Container handling real-time authorization scoring.
* **Case Management Service**: Container managing analyst reviews.
* **Audit & Compliance Archive**: AWS S3 with Object Lock for 7-year tamper-evident storage.

## Relationships
* **Merchant/Payment Gateway to Fraud Screening Core**: REST/gRPC over TLS for authorization requests.
* **Payment Switch to Fraud Screening Core**: gRPC/HTTP over TLS for transaction processing and decision routing.
* **Fraud Analysts to Case Management Service**: HTTPS/TLS for web-based case review.
* **Case Management Service to Identity Provider (IdP)**: OAuth2/OIDC over HTTPS for analyst authentication.
* **Fraud Screening Core to Audit Archive**: AWS SDK/IAM for writing tamper-evident decision logs to AWS S3.
* **ML Pipeline to Fraud Screening Core**: S3 bucket synchronization for zero-downtime model updates.

## Technology Stack
* **Cloud Provider**: AWS (`eu-west-1`) for regional infrastructure and compliance tooling.
* **Communication Protocols**: gRPC and HTTPS over TLS to meet the P99 latency requirement below 50 ms.
* **Storage & Audit**: AWS S3 with Object Lock (Compliance Mode) for low-cost, tamper-evident 7-year audit retention.
* **Authentication**: OAuth2/OIDC for secure analyst access.
* **Model Management**: S3-based artifact distribution for atomic, zero-downtime model updates.

## Rationale
This architecture leverages managed AWS services to maintain PCI-DSS Level 1 compliance and a 7-year tamper-evident audit trail within a 25,000 EUR monthly budget. Using gRPC and TLS over AWS infrastructure guarantees high throughput and low-latency performance required for real-time fraud screening by a three-engineer team.