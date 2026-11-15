## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and the US. It ensures strict data residency, regulatory compliance, and resilience for rural users via isolated regional deployments on GCP.

## Key Elements
- Patients and Clinicians (Primary Users)
- Global Traffic Director / API Gateway
- Regional Deployment Units (`europe-west3` for EU, `us-central1` for US)
- API Gateway / Ingress Controller Containers
- Consent Enforcement Middleware/Proxy Containers
- Stateless Core Application Containers
- Video Streaming Gateway Containers with Local Storage/Caching Agents
- AI Inference & Audit Proxy Containers
- FHIR Translation Adapter Container (US) and National E-Prescription Adapter Container (EU)
- Local Async Event Bus / Queue Containers
- Configuration and Secrets Management Sidecars
- Observability & Telemetry Exporter Sidecars with PII/PHI Stripping

## Relationships
- Patients/Clinicians connect to Regional API Gateways via HTTPS and WebRTC (TURN/STUN).
- Core Application Containers route traffic through Consent Enforcement Middleware via gRPC/REST.
- Video Streaming Gateway utilizes adaptive bitrate streaming over WebRTC for unstable connections (<300 kbit/s).
- US Core connects to external pharmacies via HL7 FHIR; EU Core connects via national e-prescription standards.
- AI Inference & Audit Proxy synchronously logs inputs, model versions, and outputs before returning urgency recommendations.
- Local Async Event Bus buffers telemetry locally during network drops and syncs to Regional Audit Subsystems upon reconnection.

## Technology Stack
- **Cloud Provider:** Google Cloud Platform (GCP) across `europe-west3` and `us-central1` to enforce strict regional data residency.
- **Streaming Protocol:** WebRTC over TURN/STUN for resilient, low-bandwidth video consultations.
- **Interoperability Standards:** HL7 FHIR (US) and national e-prescription APIs (EU).
- **Messaging/Buffering:** Lightweight MQTT / local message broker for async event queuing during unstable rural connections.
- **Security & Networking:** mTLS for internal container communications and strict network isolation policies.

## Rationale
This architecture guarantees strict regulatory compliance (GDPR and HIPAA) by isolating data processing within regional GCP boundaries and enforcing explicit consent via dedicated middleware. Furthermore, the stateless container design coupled with adaptive streaming and local event buffering ensures high availability and traceability even for rural users with unstable internet connections.