## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The architecture enforces strict regional data residency and compliance via Google Cloud Platform.

## Key Elements
- Patients and Licensed Clinicians (Users)
- US HL7 FHIR Providers, EU National E-Prescription Gateways, Regional Pharmacy Networks (External Systems)
- API Gateway / Region Router [GCP / HTTPS / WebSockets]
- Offline-First Patient Mobile/Web App [REST / gRPC with Idempotency Keys]
- Consent Management Container [Authorization Middleware]
- Core Business Logic & Video Consultation Containers [GCP Regional Containers / WebRTC]
- Traceability Logging Container [OpenTelemetry Collector Sidecars]
- FHIR / E-Prescription Adapter Containers [REST / FHIR / National Protocols]
- Event-Driven Integration Bus [GCP Pub/Sub with Regional Topics]
- Regional Caches [GCP Memorystore] and Object Stores [GCP Cloud Storage]

## Relationships
- Patients & Clinicians -> API Gateway / Region Router: Accesses telehealth services [HTTPS / WebSockets]
- Core Business Logic & Video Consultation Containers -> Event-Driven Integration Bus: Publishes and consumes regional events [GCP Pub/Sub]
- Event-Driven Integration Bus -> Regional Object Store: Offloads large payloads using the Claim Check pattern [GCP Cloud Storage]
- FHIR/E-Prescription Adapter Containers -> External Systems: Transmits health data [HL7 FHIR / National Protocols]

## Technology Stack
- GCP Cloud Platform (europe-west3, us-central1): Ensures complete regional data isolation and residency compliance.
- GCP Pub/Sub: Powers the Event-Driven Integration Bus with regional topics, DLQs, and flow control.
- Protocol Buffers / JSON Schema: Enforces strict message schema validation at publisher boundaries.
- OpenTelemetry / W3C Trace Context: Propagates distributed traces across asynchronous event boundaries.
- GCP Cloud Storage: Implements the Claim Check pattern for secure large-payload handling.

## Rationale
This architecture uses regional GCP infrastructure and Pub/Sub isolation to guarantee GDPR and HIPAA compliance while keeping health data strictly within its origin region. The asynchronous event-driven design, combined with offline-first capabilities and the Claim Check pattern, ensures high availability and resilience for rural users with unstable connections.