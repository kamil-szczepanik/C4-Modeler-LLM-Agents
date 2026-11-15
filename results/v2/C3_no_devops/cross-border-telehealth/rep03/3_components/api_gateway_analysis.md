## Overview
A secure, cross-border telehealth platform delivering video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The architecture enforces strict regional data residency, regulatory compliance, and resilience for rural users.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Web & Mobile Client Apps (Flutter / React Native)
- API Gateway: Google Cloud API Gateway / Apigee (Geo-Routing & Context Filter, OAuth2/JWT Validator, Rate Limiting & Resiliency Component, Localization & Header Injector Component, Gateway Audit & Telemetry Component, WAF module)
- Core Telehealth Service (Spring Boot / Java)
- AI Symptom Checker Service (FastAPI / Python)
- Interoperability & E-Prescription Service (Node.js)
- WebRTC SFU Media Relay (LiveKit on GKE)
- Data & Security Layer: Cloud SQL (PostgreSQL), Cloud Storage, GCP Cloud KMS, GCP Service Mesh (Istio)

## Relationships
- Web & Mobile Client Apps -> API Gateway: Sends API requests and queries [HTTPS and GraphQL over TLS 1.3]
- Geo-Routing & Context Filter -> Core Telehealth Service: Routes requests regionally [gRPC with mTLS via Istio]
- Geo-Routing & Context Filter -> AI Symptom Checker Service: Routes symptom check requests [gRPC with mTLS via Istio, with injected telemetry headers]
- Localization & Header Injector -> Interoperability & E-Prescription Service: Routes interoperability requests [gRPC with mTLS via Istio]

## Technology Stack
- Google Cloud Platform (GCP) across `europe-west3` and `us-central1` for region-locked data residency.
- Google Cloud API Gateway / Apigee with Envoy-based proxy for edge routing, WAF, and traffic management.
- Spring Boot (Java), FastAPI (Python), and Node.js for microservices containers.
- LiveKit on GKE for WebRTC SFU media relay supporting low-bandwidth video consultations.
- Cloud SQL (PostgreSQL), Cloud Storage, and GCP Cloud KMS for encrypted data persistence.

## Rationale
The multi-region GCP architecture strictly separates EU and US data to satisfy GDPR and HIPAA compliance mandates. Edge geo-routing, gRPC microservices, and robust resilience mechanisms ensure low-latency performance and high availability for rural patients on unstable connections.