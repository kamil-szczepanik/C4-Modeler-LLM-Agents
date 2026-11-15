## Overview
The Billing / Payment Container manages multi-currency transactions, regional tax calculations, and secure payment processing for patients and finance staff. It enforces strict regional data residency and PCI-DSS compliance across EU and US deployments.

## Key Elements
- Patients (EU & US)
- Finance/Billing Operations Staff
- Billing API Controller (Node.js / NestJS)
- Payment Orchestrator Service
- Ledger & Invoice Engine
- PCI-DSS Tokenization Adapter
- Tax & Currency Engine
- Checkout Recovery Service
- External Payment Gateways (Stripe/Adyen)
- Google Cloud SQL (PostgreSQL)
- GCP Cloud Storage WORM buckets
- GCP Pub/Sub

## Relationships
- API Gateway -> Billing API Controller [gRPC over mTLS]
- Payment Orchestrator Service -> External Payment Gateways [REST over HTTPS]
- Ledger & Invoice Engine -> Google Cloud SQL [SQL over TLS]
- External Payment Gateways -> Billing API Controller [REST over HTTPS with HMAC signature verification]
- Billing API Controller -> Tax & Currency Engine [Internal Function Call]
- Payment Orchestrator Service -> Checkout Recovery Service [Internal Event]

## Technology Stack
- Node.js / NestJS: Chosen for scalable, asynchronous handling of billing logic and API endpoints.
- GCP Kubernetes Engine (GKE): Enables active-active multi-region deployment across `europe-west3` and `us-central1`.
- GCP Pub/Sub: Buffers webhooks to guarantee idempotency and prevent failures during traffic spikes.
- GCP Secret Manager: Secures runtime injection of API keys and database credentials without hardcoding.
- GCP Cloud Storage WORM: Stores immutable audit logs and regional invoices for HIPAA and GDPR compliance.

## Rationale
This architecture isolates sensitive financial workflows and payment tokenization to maintain strict PCI-DSS scope separation from core health records. Multi-region GCP deployment guarantees that EU and US financial logs adhere to regional data residency laws.