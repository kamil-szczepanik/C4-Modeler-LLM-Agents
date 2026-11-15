## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The architecture enforces strict regional data residency and compliance using Google Cloud Platform (GCP).

## Key Elements
- **People**: Patients, Licensed Clinicians
- **External Systems**: Regional Pharmacies, National Standards APIs, AI Symptom Checker
- **Containers**: API Gateway, Media Gateway / Edge Proxy, AI Symptom Checker, E-Prescription Service, Interoperability Adapter, Consent Enforcement Proxy, Audit Logging, Observability / Tracing, Configuration & Feature Flag Service, Data Migration / Archival Worker

## Relationships
- Patients and Clinicians interact with the **API Gateway** via HTTPS/WSS for client routing, authentication, and TLS termination.
- **Media Gateway** manages WebRTC video consultations with adaptive bitrate handling for unstable connections.
- **Consent Enforcement Proxy** intercepts cross-region requests between `europe-west3` and `us-central1` using gRPC/REST to validate explicit user consent tokens.
- **Interoperability Adapter** integrates with regional pharmacies and APIs using HL7 FHIR in the US and national standards in the EU.
- **Audit Logging** and **Observability / Tracing** containers collect OpenTelemetry metrics and structured JSON logs regionally.

## Technology Stack
- **Cloud Provider**: GCP (`europe-west3` for EU, `us-central1` for US) to enforce regional data boundaries.
- **Communication Protocols**: gRPC and REST for secure inter-container communication; WebRTC for real-time video consultations.
- **Observability**: OpenTelemetry for distributed tracing and regional structured JSON logging.
- **Storage**: Managed regional databases (Cloud SQL / Spanner) to maintain stateless application design and data residency.

## Rationale
Stateless microservices deployed across isolated regional GCP environments guarantee strict GDPR and HIPAA compliance while preventing cross-border data leakage. Dedicated edge proxies, interoperability adapters, and robust tracing ensure high availability under unstable connections and end-to-end auditability for medical compliance.