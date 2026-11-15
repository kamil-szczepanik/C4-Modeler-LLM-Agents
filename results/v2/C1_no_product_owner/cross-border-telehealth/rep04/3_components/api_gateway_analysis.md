## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency, privacy, and medical traceability compliance on Google Cloud Platform.

## Key Elements
- Patients and Licensed Clinicians (Users)
- GCP External HTTP(S) Load Balancer & TLS Termination Edge Policy Component
- Auth & Consent Enforcement Component (Envoy Ext-Authz)
- Traffic Routing & Mesh Proxy Component (Envoy Sidecar/Gateway)
- Regional GKE Clusters (`europe-west3` and `us-central1`)
- Consent Management Service, Video Consultation Service, and AI Symptom Checker

## Relationships
- Patients & Clinicians -> GCP External HTTP(S) Load Balancer: Connects for API requests and video sessions [HTTPS/TLS 1.3 and WebSockets/WebRTC]
- Auth & Consent Enforcement Component -> Consent Management Service: Validates purpose-limitation consent [gRPC]
- Traffic Routing & Mesh Proxy Component -> Regional GKE Services: Forwards internal requests [gRPC / strict mTLS]

## Technology Stack
- GCP External HTTP(S) Load Balancer: Handles global geo-routing and edge WAF protection.
- Envoy Proxy & GCP Service Mesh: Manages edge routing, circuit breaking, and SPIFFE/SPIRE strict mTLS.
- OpenTelemetry: Captures distributed tracing for low-bandwidth rural connections.
- OAuth2 / JWT: Secures authentication with token binding to prevent cross-region reuse.

## Rationale
This architecture ensures strict regional data segregation between EU and US compliance domains while maintaining secure, fault-tolerant access for rural users. Native GCP cloud components and Envoy service mesh controls guarantee low latency, robust observability, and strict adherence to GDPR and HIPAA standards.