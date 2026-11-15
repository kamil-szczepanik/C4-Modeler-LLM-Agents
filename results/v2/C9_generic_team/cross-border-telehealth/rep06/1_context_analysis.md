## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The architecture enforces strict regional data residency, regulatory compliance, and resilience for unstable network connections.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Global Control Plane (Auth, Tenant Config, Feature Flags)
- Regional Perimeters (`europe-west3`, `us-central1`)
- Client Application (React/React Native with local caching and offline queueing)
- API Gateway & Protocol Negotiator (WebRTC/gRPC)
- Core Domain Services (Video, E-Prescription, AI Symptom Checker, Consent Management)
- Anti-Corruption Layer (ACL) & Regional Adapters
- Immutable Write-Ahead Audit Logging Service
- External Health Integrations (HL7 FHIR for US, national e-prescription standards for EU)

## Relationships
- Patients/Clinicians interact with API Gateways via HTTPS/TLS 1.3 and WebRTC (RTP/SRTP).
- API Gateways route requests to Regional Perimeter services using gRPC and REST.
- Regional Adapters translate payloads using the Anti-Corruption Layer (ACL) to interact with External Health Integrations (HL7 FHIR, EU national APIs).
- AI Symptom Checker and Consent Services write immutable logs to regional audit stores prior to transaction completion.
- Global Control Plane pushes configuration and feature flags to regional perimeters via secure gRPC streams.

## Technology Stack
- **Cloud Provider:** Google Cloud Platform (GCP) across `europe-west3` and `us-central1` for strict data residency (R-05).
- **Communication Protocols:** WebRTC with adaptive bitrate streaming and fallback audio-only/text modes for unstable connections (R-06).
- **Data & Logging:** Regionally isolated databases with Write-Ahead Audit Logging for EU MDR and HIPAA traceability (R-07).
- **Integration Standards:** HL7 FHIR for US systems and national APIs for EU e-prescriptions via regional adapters (R-08).

## Rationale
This architecture uses decoupled regional perimeters and bulkheads to strictly enforce GDPR and HIPAA data residency while isolating resource-intensive workloads. Client-side resilience and protocol negotiation ensure continuous availability for rural users on unstable connections.