## Overview
[Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker across the EU and US. The billing and regional monetization architecture ensures localized transactions, tax compliance, and strict data residency.]

## Key Elements
- Patients
- Finance/Admin Staff
- Transaction Router Component (Spring Boot on GKE)
- Tax & Invoicing Engine Component (Spring Boot on GKE)
- Refund & Dispute Handler Component (Spring Boot on GKE)
- Billing Audit Logger Component (Spring Boot on GKE)
- Ledger & Persistence Layer (PostgreSQL on GKE)
- Cloud Pub/Sub
- Cloud Logging & BigQuery
- Regional Payment Gateways (Stripe, SEPA, regional credit cards)
- Google Secret Manager
- Google Cloud KMS (CMEK)

## Relationships
- Cloud Load Balancing / API Gateway -> Transaction Router: Routes payment and billing requests [gRPC over mTLS]
- Transaction Router -> Regional Payment Gateways: Executes charges and reversals [HTTPS]
- Transaction Router -> Tax & Invoicing Engine: Requests regional tax calculations [In-process / gRPC]
- Transaction Router -> Cloud Pub/Sub: Publishes payment and refund events [gRPC]
- Tax & Invoicing Engine -> Cloud Pub/Sub: Consumes billing events and publishes invoice events [gRPC]
- Billing Audit Logger -> Cloud Logging & BigQuery: Writes tamper-proof audit trails [HTTPS]

## Technology Stack
- Spring Boot on GKE: Core runtime for microservices due to enterprise maturity
- Google Cloud Pub/Sub: Asynchronous event messaging for decoupling and reliability
- PostgreSQL on GKE: Regionally isolated relational data storage
- Google Cloud KMS (CMEK) & Secret Manager: Cryptographic key management and dynamic credential retrieval
- OpenTelemetry & Resilience4j: Distributed tracing and circuit breaking for fault tolerance

## Rationale
[This architecture enforces regional data residency and PII redaction to satisfy strict GDPR and HIPAA mandates. Event-driven decoupling with dead-letter queues guarantees financial consistency and resilience against regional outages.]