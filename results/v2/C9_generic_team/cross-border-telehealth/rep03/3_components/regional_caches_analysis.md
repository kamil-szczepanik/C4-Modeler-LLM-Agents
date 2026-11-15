## Overview
- Implements a cross-border telehealth platform delivering video consultations, e-prescriptions, and AI symptom checks across the EU and US.
- Enforces strict regional data residency, regulatory compliance, and resilience for unstable rural network conditions.

## Key Elements
- Patients and Licensed Clinicians (Users)
- API Gateway / Region Router (Google Cloud Platform, HTTPS, WebSockets)
- Offline-First Patient Mobile/Web App (REST, gRPC, Idempotency Keys)
- Core Business Logic & Video Consultation Containers (GCP Regional Containers, WebRTC)
- Regional Caches (GCP Memorystore)
- Traceability Logging Container (OpenTelemetry Collector Sidecars)
- FHIR/E-Prescription Adapter Containers (REST, FHIR, National Protocols)
- Event-Driven Integration Bus (GCP Pub/Sub)

## Relationships
- Offline-First Patient Mobile/Web App -> API Gateway / Region Router [HTTPS, gRPC, WebSockets]
- API Gateway / Region Router -> Core Business Logic & Video Consultation Containers [gRPC]
- Core Business Logic & Video Consultation Containers -> Regional Caches [GCP Memorystore, Cache-Aside Pattern]
- Core Business Logic & Video Consultation Containers -> Event-Driven Integration Bus [GCP Pub/Sub]
- FHIR/E-Prescription Adapter Containers -> US HL7 FHIR Providers & EU National E-Prescription Gateways [REST, FHIR, National Protocols]

## Technology Stack
- Google Cloud Platform (`europe-west3`, `us-central1`): Target cloud environment enforcing regional data isolation.
- GCP Memorystore: Regional caching layer utilizing Cache-Aside pattern, TTLs, and Redlock distributed locks.
- WebRTC: Real-time protocol for video consultations supporting degraded modes below 300 kbit/s.
- OpenTelemetry: Sidecars for distributed tracing and cache performance telemetry.
- GCP KMS: Application-level encryption for cryptographic data residency enforcement.

## Rationale
- Decouples stateless containers via regional GCP Memorystore instances to ensure low-latency data access while maintaining strict data residency boundaries.
- Employs resiliency patterns, idempotent processing, and encrypted regional isolation to satisfy medical compliance and rural availability constraints.