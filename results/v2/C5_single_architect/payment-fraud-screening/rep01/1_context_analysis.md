## Overview
A real-time payment fraud screening system evaluates card-not-present payment authorizations and provides case management for fraud analysts. It ensures PCI-DSS compliance, <50ms P99 latency at 3,000 TPS, and tamper-evident 7-year auditability on AWS eu-west-1.

## Key Elements
- **Real-Time Payment Fraud Screening System**: Core software system boundary.
- **Payment Gateway / Acquirer**: External system sending authorization requests.
- **Payment Analysts**: Users performing manual case reviews.
- **Card Networks / Issuers**: External systems providing chargeback feedback.
- **Tokenization / Vault Provider**: External service handling cardholder data.
- **Compliance Auditors**: Users accessing 7-year audit logs.

## Relationships
- **Payment Gateway -> Fraud Screening System**: gRPC over HTTP/2 for real-time scoring.
- **Fraud Screening System -> Tokenization Provider**: HTTPS with mutual TLS for token resolution.
- **Analysts -> Fraud Screening System**: HTTPS (TLS 1.3) via Web UI for case management.
- **Fraud Screening System -> Card Networks**: HTTPS for asynchronous chargeback ingestion.

## Technology Stack
- **AWS**: Cloud provider in eu-west-1 utilizing managed services within a 25,000 EUR/month budget to support a three-engineer team.
- **gRPC over HTTP/2**: Protocol for low-latency authorization requests meeting the 50ms P99 requirement.
- **HTTPS/TLS 1.3**: Protocol for secure Web UI access and external integrations.
- **Managed Tokenization Vault**: External service ensuring PCI-DSS Level 1 compliance by preventing analysts from viewing raw card numbers.

## Rationale
This architecture leverages managed AWS services and decoupled tokenization to maintain strict PCI-DSS Level 1 compliance and a 50ms latency budget. It operates efficiently within a fixed budget and small team by utilizing high-performance gRPC protocols and cloud-native scaling.