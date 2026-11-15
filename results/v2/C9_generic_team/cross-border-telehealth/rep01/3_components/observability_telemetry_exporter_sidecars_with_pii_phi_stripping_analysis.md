## Overview
• The system is a Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US.
• It ensures strict data residency, privacy, and traceability compliance via regional GCP deployments and secure telemetry pipelines.

## Key Elements
• Patients and Clinicians (Users)
• API Gateway / Ingress Controller Containers (Google Cloud Platform Ingress / Envoy)
• Consent Enforcement Middleware/Proxy Containers
• Stateless Core Application Containers
• Video Streaming Gateway Containers (WebRTC, TURN/STUN)
• AI Inference & Audit Proxy Containers (Python / gRPC)
• FHIR Translation Adapter (US) and National E-Prescription Adapter (EU)
• Observability & Telemetry Exporter Sidecars with PII/PHI Stripping (OpenTelemetry / Custom Exporter)

## Relationships
• Patients and Clinicians interact with API Gateway via HTTPS / WebRTC.
• Core application containers communicate with regional backends using gRPC / REST over GCP internal networks.
• Telemetry sidecars export sanitized logs and metrics to regional OpenTelemetry backends in `europe-west3` and `us-central1`.

## Technology Stack
• Google Cloud Platform (GCP): Target cloud provider ensuring isolated regional processing in `europe-west3` and `us-central1`.
• OpenTelemetry (OTel) Collector framework: Used for telemetry collection, PII/PHI stripping, and local file buffering.
• WebRTC and TURN/STUN: Protocols powering real-time video consultations under unstable connections.
• HL7 FHIR and National E-Prescription APIs: Interoperability standards for US and EU prescription routing.

## Rationale
• Regional GCP isolation and strict telemetry stripping enforce GDPR and HIPAA compliance while keeping health data local.
• Local buffering and fail-closed sanitization protect application availability and security during unstable rural network conditions.