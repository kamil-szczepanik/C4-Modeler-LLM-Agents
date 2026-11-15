## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, HIPAA, GDPR, and EU MDR compliance on Google Cloud Platform.

## Key Elements
- Patients and Clinicians (End Users)
- API Gateway / Ingress Controller Containers (Google Cloud Platform Ingress / Envoy)
- Stateless Core Application Containers (GCP Microservices)
- Video Streaming Gateway Containers (WebRTC, TURN/STUN)
- AI Inference & Audit Proxy Containers (Python / gRPC)
- FHIR Translation Adapter Container (US) and National E-Prescription Adapter Container (EU)
- Consent Enforcement Middleware/Proxy Containers

## Relationships
- Patients and Clinicians -> API Gateway / Ingress Controller Containers: Connect via HTTPS and WebRTC (TURN/STUN)
- Global Traffic Director / API Gateway -> API Gateway / Ingress Controller Containers: Routes regional traffic via mTLS
- API Gateway / Ingress Controller Containers -> Stateless Core Application Containers: Forwards validated requests via internal gRPC/HTTP
- API Gateway / Ingress Controller Containers -> AI Inference & Audit Proxy Containers: Routes symptom checker payloads via gRPC

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider across `europe-west3` and `us-central1` regions ensuring data residency.
- Envoy Proxy / GCP Ingress: Manages ingress routing, token-bucket rate limiting, TLS termination, and schema validation.
- WebRTC and TURN/STUN: Powers real-time video consultations supporting degraded rural connections.
- OpenTelemetry: Captures distributed tracing headers (W3C Trace Context) and telemetry with PII/PHI stripping.
- RFC 7807 Problem Details: Standardizes error response schemas across all gateway error paths.

## Rationale
This architecture guarantees strict regional data residency by isolating EU and US workloads while ensuring high availability for rural users via optimized gateways. Envoy-based rate limiting, schema validation, and rigorous security hardening protect core microservices and maintain compliance with healthcare standards.