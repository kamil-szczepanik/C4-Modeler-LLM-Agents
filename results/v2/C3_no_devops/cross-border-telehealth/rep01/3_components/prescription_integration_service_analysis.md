## Overview
The Prescription Integration Service is a regional Node.js component of the Cross-Border Telehealth Platform responsible for reliably translating, dispatching, and tracking e-prescriptions to international pharmacies. It ensures secure, compliant, and fault-tolerant delivery of medical prescriptions for patients across the EU and US.

## Key Elements
* Prescription API Controller (Node.js/Express)
* Translation & Mapping Engine (Node.js)
* Outbound Dispatcher & Adapter Worker (Node.js with BullMQ and `opossum` Circuit Breaker)
* Status Webhook Handler (Node.js/Express)
* Regional Dead-Letter Queue (DLQ backed by Cloud SQL)
* Cloud Pub/Sub
* Pharmacies (EU & US)

## Relationships
* Core Telehealth Service -> Prescription API Controller: Dispatches prescription commands via gRPC with OAuth 2.0 token propagation and mTLS
* Outbound Dispatcher -> Pharmacies (EU & US): Transmits mapped payloads over HTTPS with mTLS and TLS 1.3
* Status Webhook Handler -> Cloud Pub/Sub: Publishes delivery state change events using HMAC/cert-validated webhooks
* Outbound Dispatcher -> Regional DLQ (Cloud SQL): Persists failed payloads encrypted with Cloud KMS CMEK
* Outbound Dispatcher -> Audit & Compliance Reporting Service (BigQuery): Dispatches immutable audit events for security tracking

## Technology Stack
* Node.js / Express: Core runtime for asynchronous handling of external pharmacy network calls
* BullMQ: Manages outbound queueing, retries, and regional state storage
* Opossum: Implements circuit breaker and fallback policies for unstable pharmacy endpoints
* Cloud KMS CMEK: Encrypts sensitive PII/PHI payloads at rest in the DLQ and state store
* GCP Cloud Pub/Sub: Enables asynchronous event streaming for status updates and failure logging

## Rationale
This architecture uses an asynchronous, event-driven pattern with robust circuit-breaking and translation engines to handle unreliable external pharmacy networks. Regional deployment and strict encryption ensure compliance with GDPR, HIPAA, and data residency constraints while maintaining clinical workflow continuity.