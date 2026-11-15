## Overview
[A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. Its core purpose is delivering compliant healthcare services while strictly enforcing regional data residency and handling unstable rural network connections.]

## Key Elements
- Patients and Licensed Clinicians (Users)
- API Gateway / Region Router
- Offline-First Patient Mobile/Web App
- Consent Management Container
- Core Business Logic & Video Consultation Containers
- Traceability Logging Container
- FHIR/E-Prescription Adapter Containers
- Event-Driven Integration Bus (GCP Pub/Sub)
- Regional Caches (GCP Memorystore)
- US HL7 FHIR Providers, EU National E-Prescription Gateways, Regional Pharmacy Networks (External Systems)

## Relationships
- Patients and Clinicians interact with the API Gateway / Region Router via HTTPS/WebSockets.
- API Gateway routes traffic to regional containers in `europe-west3` and `us-central1`.
- Offline-First Patient App synchronizes state using REST/gRPC APIs with idempotency keys.
- Consent Management Container enforces authorization middleware across all API routes.
- FHIR/E-Prescription Adapters integrate with external US HL7 FHIR Providers and EU National Gateways.
- Regional message brokers handle asynchronous handoffs via GCP Pub/Sub per region.

## Technology Stack
- **Cloud Provider:** Google Cloud Platform (GCP) across regions `europe-west3` and `us-central1` for strict regional data residency.
- **Messaging:** GCP Pub/Sub for regional event-driven integration and decoupling.
- **Caching/Session Storage:** GCP Memorystore for stateless container scaling and temporary sync payloads.
- **Observability:** OpenTelemetry collector sidecars for localized distributed tracing and audit logging.
- **API & Protocol:** REST/gRPC with TLS for secure communication and fallback audio/video protocols.

## Rationale
[This architecture satisfies strict GDPR, HIPAA, and EU MDR compliance mandates by strictly isolating data processing and storage within designated GCP regional boundaries. Additionally, the offline-first design, stateless containers, and event-driven integration bus ensure high availability and resilient telehealth operations over unstable rural connections.]