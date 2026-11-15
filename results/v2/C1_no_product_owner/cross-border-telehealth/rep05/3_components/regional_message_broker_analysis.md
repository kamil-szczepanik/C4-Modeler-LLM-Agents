## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, GDPR/HIPAA compliance, and robust messaging for backend microservices.

## Key Elements
* Event Ingestion Gateway (Envoy Proxy sidecar)
* Regional Topic Router (GCP Pub/Sub Topics with region-scoped IAM policies)
* Dead-Letter & Retry Controller (GCP Pub/Sub Dead-Letter Topics with Cloud Monitoring)
* Consultation Service (Node.js, WebRTC)
* Clinical & Prescription Service (Java, Spring Boot)
* Immutable Audit Logging Service

## Relationships
* Consultation Service -> Event Ingestion Gateway: Publishes regional telemetry and chat events [gRPC over mTLS]
* Clinical & Prescription Service -> Event Ingestion Gateway: Publishes prescription events [gRPC over mTLS]
* Event Ingestion Gateway -> Regional Topic Router: Routes validated messages [Pub/Sub API]
* Regional Topic Router -> Dead-Letter & Retry Controller: Routes unacknowledged messages after max retries [Pub/Sub API]

## Technology Stack
* GCP Pub/Sub: Regionally isolated message brokering ensuring strict regional data residency (europe-west3 and us-central1).
* Envoy Proxy: Handles event ingestion and terminates gRPC over mTLS connections.
* GCP Cloud KMS: Implements application-layer envelope encryption restricted to regional keys for HIPAA/GDPR data protection.
* SPIFFE/SPIRE: Provides dynamic workload identity validation during the mTLS handshake.
* Terraform: Enforces Infrastructure as Code and regional deployment parity.

## Rationale
This architecture isolates messaging to backend services while eliminating direct client subscriptions to prevent scalability and security risks. Regionally scoped GCP Pub/Sub topics, strict IAM roles, and application-layer envelope encryption guarantee compliance with data residency and privacy mandates.