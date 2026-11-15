## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker across the EU and US. It enforces strict regional data residency, regulatory compliance, and high availability for unstable connections.

## Key Elements
- Patients and Licensed Clinicians
- Regional Pharmacies and National Standards APIs
- External AI Symptom Checker Container
- API Gateway and Media Gateway / Edge Proxy
- E-Prescription Service and Interoperability Adapter
- Consent Enforcement Proxy and Audit Logging
- Observability / Tracing (OpenTelemetry)
- Configuration & Feature Flag Service

## Relationships
- Patients/Clinicians -> API Gateway / Media Gateway: HTTPS/WSS, WebRTC
- API Gateway -> AI Symptom Checker Container: gRPC
- E-Prescription Service -> Regional Pharmacies: National Standards / HL7 FHIR
- Observability / Tracing -> API Gateway: Collects metrics and traces [OpenTelemetry]

## Technology Stack
- Google Cloud Platform (`europe-west3`, `us-central1`): Target cloud provider ensuring regional isolation
- OpenTelemetry (OTel): Vendor-neutral telemetry with regional collectors, attribute scrubbing, and tail-based sampling for GDPR/HIPAA compliance
- Managed Regional Databases (Cloud SQL / Spanner): Enforces regional data residency constraints
- WebRTC: Supports real-time video consultations in degraded network modes

## Rationale
The architecture strictly segregates regional data pipelines to satisfy GDPR and HIPAA compliance mandates. OpenTelemetry integration with sanitization and sampling ensures traceability of AI medical devices without compromising user-facing performance or privacy.