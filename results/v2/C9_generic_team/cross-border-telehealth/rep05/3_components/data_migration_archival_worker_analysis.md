## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency while ensuring high availability and regulatory compliance.

## Key Elements
- Patients and Licensed Clinicians (Users)
- API Gateway (Google Cloud Platform)
- Media Gateway / Edge Proxy (WebRTC)
- AI Symptom Checker Container (gRPC)
- E-Prescription Service & Managed Regional Databases (Cloud SQL / Spanner)
- Data Migration / Archival Worker (Managed Regional Databases)
- Consent Enforcement Proxy & Audit Logging
- Interoperability Adapter (HL7 FHIR, National Standards)

## Relationships
- Patients and Clinicians interact via HTTPS/WSS through the API Gateway (Google Cloud Platform).
- Video consultations connect via WebRTC through the Media Gateway / Edge Proxy.
- The AI Symptom Checker container communicates via gRPC.
- Regional databases interact with the Data Migration / Archival Worker using Cloud Pub/Sub and regional storage.

## Technology Stack
- Google Cloud Platform (`europe-west3`, `us-central1`) for cloud infrastructure and managed services.
- Cloud SQL and Cloud Spanner for managed regional databases enforcing data residency.
- OpenTelemetry and Prometheus for observability and distributed tracing.
- HL7 FHIR and National Standards APIs for interoperability.

## Rationale
This architecture guarantees strict compliance with GDPR and HIPAA by isolating regional data within designated GCP regions. It maintains real-time availability for unstable internet connections while ensuring traceable AI recommendations and secure cross-border data handling.