## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, GDPR/HIPAA compliance, and robust performance over unstable connections using GCP.

## Key Elements
- Patients and Licensed Clinicians (Users)
- API Gateway & Media Gateway / Edge Proxy (Google Cloud Platform, HTTPS/WSS, WebRTC)
- E-Prescription Service (Managed Regional Databases: Cloud SQL / Spanner)
- Interoperability Adapter & Anti-Corruption Layer (HL7 FHIR, National Standards)
- AI Symptom Checker Container (gRPC) & Consent Enforcement Proxy
- Audit Logging (Structured JSON Logs, Regional Storage) & Observability (OpenTelemetry)

## Relationships
- Patients/Clinicians connect to API Gateway and Media Gateway via HTTPS/WSS and WebRTC.
- E-Prescription Service communicates with regional databases and Interoperability Adapters using gRPC and REST.
- Interoperability Adapters interface with Regional Pharmacies and National Standards APIs.
- Audit Logging and Observability containers collect telemetry across all regional services.

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider across `europe-west3` and `us-central1` for data residency.
- Cloud SQL / Spanner: Managed regional databases ensuring isolated data storage per jurisdiction.
- WebRTC: Protocol for peer-to-peer video consultations operating in degraded network modes.
- HL7 FHIR and National Standards APIs: Interoperability protocols for US and EU e-prescriptions.
- Google Cloud Storage: Regional object storage implementing the Claim Check Pattern.

## Rationale
This architecture uses regional isolation (Bulkhead and CQRS patterns) to guarantee GDPR and HIPAA compliance while maintaining data residency boundaries. Resiliency patterns like Circuit Breakers and Transactional Outboxes ensure high availability for rural users over unstable connections.