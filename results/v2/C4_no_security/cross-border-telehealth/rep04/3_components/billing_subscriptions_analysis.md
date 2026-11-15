## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The Billing & Subscriptions component manages recurring revenue, regional taxes, and secure payment processing.]

## Key Elements
- Patients (EU & US) & Finance/Support Operations
- API Gateway (Cloud Endpoints / Envoy)
- Billing & Subscriptions Container (Go)
- Subscription Engine (Component)
- Payment Orchestrator (Component)
- Tax & Invoicing Adapter (Component)
- Invoice & Receipt Generator (Component)
- Webhook Handler (Component)
- External Systems: Stripe, GCP Secret Manager, Cloud Storage, GCP Pub/Sub

## Relationships
- API Gateway -> Subscription Engine via gRPC
- Payment Orchestrator -> Stripe via HTTPS (TLS 1.3)
- Stripe -> Webhook Handler via HTTPS / Webhooks (secured via GCP Secret Manager)
- Subscription Engine -> Invoice & Receipt Generator via gRPC / Async
- Invoice & Receipt Generator -> Cloud Storage via Cloud Storage API (region-locked)

## Technology Stack
- Go: Chosen for high concurrency and performance in core billing services.
- Stripe: Provides global payment gateway with regional key isolation.
- GCP Secret Manager: Secures regional API keys and webhook validation secrets.
- GCP Cloud Storage: Stores regional PDF invoices with data residency compliance.
- GCP Pub/Sub: Buffers asynchronous webhook events with Dead Letter Queue support.

## Rationale
[Isolating billing components and deploying them across multi-regions strictly enforces EU/US data residency constraints. Using independent regional gateways with circuit breakers and durable queues ensures resilient financial operations and compliance with local tax laws.]