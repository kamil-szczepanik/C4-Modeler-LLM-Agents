## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients on GCP. The Node.js/Go Billing & Localization Container manages cross-border multi-currency transactions, regional taxation, and localization workflows.

## Key Elements
- API Router / Handler Module (Go)
- Localization & Tax Engine (Node.js)
- Payment Gateway Integration Adapter (Go)
- Billing Audit & Reconciliation Exporter (Go)
- Kong API Gateway/BFF
- GCP Cloud SQL (PostgreSQL)
- GCP Cloud Pub/Sub
- GCP Secret Manager
- External Payment Providers (Stripe, SEPA)

## Relationships
- Kong API Gateway/BFF -> API Router / Handler Module: Processes billing and localization workflows [gRPC / Anthos Service Mesh (mTLS)]
- Localization & Tax Engine -> Payment Gateway Integration Adapter: Forwards calculated totals for transaction execution [Internal Function Call / Channel]
- Payment Gateway Integration Adapter -> External Payment Providers: Processes secure charges [HTTPS / REST with TLS 1.3]
- Payment Gateway Integration Adapter -> Billing Audit & Reconciliation Exporter: Publishes transaction success/failure events [GCP Cloud Pub/Sub]
- Billing Audit & Reconciliation Exporter -> GCP Cloud SQL (PostgreSQL): Persists reconciled ledger data with CMEK [PostgreSQL Protocol]

## Technology Stack
- Go: High-throughput API routing, payment adapters, and asynchronous event processing
- Node.js: Localization and regional tax rule evaluation
- GCP Cloud SQL (PostgreSQL): Region-pinned relational data persistence with CMEK encryption
- GCP Cloud Pub/Sub: Asynchronous event messaging for billing audit logs
- GCP Secret Manager: Dynamic runtime injection of API keys and webhook secrets

## Rationale
This architecture ensures strict GDPR and HIPAA compliance through region-pinned data residency and tokenized PCI-DSS scope reduction. Asynchronous payment handling with idempotent keys guarantees resilience for rural users with unstable connections.