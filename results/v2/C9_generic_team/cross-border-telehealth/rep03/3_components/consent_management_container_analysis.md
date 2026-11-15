## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency and compliance under GDPR and HIPAA.

## Key Elements
- Consent Management Container (Policy evaluation middleware)
- Open Policy Agent (OPA) Evaluation Core
- GCP Memorystore (Regional caching layer)
- GCP Pub/Sub (Push-based policy distribution bus)
- OpenTelemetry Collector Sidecars (Distributed tracing and log shipping)
- API Gateway / Region Router

## Relationships
- API Gateway / Region Router -> Consent Management Container: Forwards requests for authorization evaluation via internal REST/gRPC
- Consent Management Container -> GCP Memorystore: Reads cached active consent tokens via Redis protocol
- GCP Pub/Sub -> Consent Management Container: Distributes compiled OPA policy bundles via push subscription
- Consent Management Container -> OpenTelemetry Collector Sidecar: Emits structured audit logs asynchronously via local socket

## Technology Stack
- Open Policy Agent (OPA): Evaluates dynamic, versioned access control and privacy policies
- GCP Memorystore: Provides low-latency regional caching for active consent tokens
- GCP Pub/Sub: Enables asynchronous, reliable distribution of policy bundles to regional instances
- OpenTelemetry: Captures distributed traces and structured audit logs for compliance accountability
- GCP Regional Containers (`europe-west3`, `us-central1`): Hosts isolated regional microservices ensuring strict data residency

## Rationale
This architecture enforces strict regional isolation and compliance through localized OPA policy engines and database sharding. Caching and sub-50ms timeouts ensure high availability and low latency for users in rural areas with unstable connections.