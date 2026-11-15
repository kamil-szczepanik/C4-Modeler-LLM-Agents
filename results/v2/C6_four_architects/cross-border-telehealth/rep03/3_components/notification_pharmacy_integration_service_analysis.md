## Overview
[A secure, region-isolated Notification & Pharmacy Integration Service managing cross-border e-prescriptions and patient alerts on Google Cloud Platform. It enforces strict data residency to comply with GDPR and HIPAA regulations.]

## Key Elements
* Regional Integration Router Component (Go)
* EU/US Pharmacy Adapter Components (Go)
* Notification Dispatcher Component (Go)
* Outbox & Delivery Tracker Component (Go)
* Cloud Pub/Sub (Regional messaging)
* Cloud SQL PostgreSQL (Regional persistence)
* External Pharmacy Gateways (EU/US)
* External Notification Providers (Twilio, Firebase)
* Audit & Compliance Logger Sidecar (Fluentbit / Go)

## Relationships
* Cloud Pub/Sub -> Regional Integration Router: Delivers async events [Pub/Sub Pull/Push]
* Regional Integration Router -> EU/US Pharmacy Adapters & Notification Dispatcher: Dispatches tasks [In-Process Go Channels]
* EU/US Pharmacy Adapters -> External Pharmacy Gateways: Sends e-prescription data [HTTPS/REST (TLS 1.3)]
* Notification Dispatcher -> External Notification Providers: Sends alerts [HTTPS/REST (TLS 1.3)]
* Outbox & Delivery Tracker -> Cloud SQL PostgreSQL: Persists delivery state [pgx / SQL over TLS 1.3]
* Outbox & Delivery Tracker -> Audit & Compliance Logger Sidecar: Emits audit logs [Unix Domain Sockets]

## Technology Stack
* Go: Chosen for high concurrency and resilience in processing webhooks and integrations.
* Google Cloud Platform (europe-west3, us-central1): Chosen to enforce strict data residency boundaries.
* Cloud SQL PostgreSQL: Selected for transactional outbox persistence and delivery tracking.
* Cloud Pub/Sub: Used for reliable, region-isolated asynchronous event streaming.
* HTTPS/REST (TLS 1.3): Standard protocol for secure external communications with pharmacies and notification providers.
* Unix Domain Sockets: Used for secure, low-overhead local telemetry transfer to the audit sidecar.

## Rationale
[This component architecture guarantees strict regional data isolation between the EU and US to satisfy mandatory GDPR and HIPAA compliance. Furthermore, the transactional outbox pattern and regional deployments ensure reliable, decoupled delivery of e-prescriptions and alerts under high availability constraints.]