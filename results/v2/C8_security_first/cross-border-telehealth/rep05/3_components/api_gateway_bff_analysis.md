## Overview
Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict regional data residency, regulatory compliance, and resilience for unstable network connections.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Frontend Client Apps (Flutter)
- API Gateway / BFF (Envoy / gRPC-Web)
- Video Consultation Service (WebRTC / SFU - Mediasoup)
- AI Symptom Checker Container (Python / FastAPI)
- E-Prescription Integration Service (Node.js / Express)
- Consent & Policy Engine (Opa / Go)
- Data Layer (PostgreSQL / Cloud SQL)
- Regional Redis Rate-Limiting Clusters

## Relationships
- Frontend Client Apps -> API Gateway / BFF: Routes client requests via gRPC-Web and HTTPS [gRPC-Web, HTTPS]
- API Gateway / BFF -> Video Consultation Service: Routes video traffic and consultation requests [gRPC, mTLS]
- API Gateway / BFF -> AI Symptom Checker Container: Routes symptom checker payloads [gRPC, mTLS]
- API Gateway / BFF -> E-Prescription Integration Service: Routes prescription requests [gRPC, mTLS]
- API Gateway / BFF -> Consent & Policy Engine: Requests policy validation via external authorization [gRPC, mTLS]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing `europe-west3` and `us-central1` regions for regional data isolation.
- Envoy Proxy / gRPC-Web: Powers the API Gateway/BFF with Lua/Wasm filters for geo-routing, rate limiting, and telemetry.
- Anthos Service Mesh & Config Management: Enforces zero-trust mTLS security perimeters and autonomous regional lifecycles.
- OpenTelemetry & Prometheus: Captures distributed tracing, tail latency, and filter performance metrics.

## Rationale
Autonomous regional deployments on GCP ensure EU health data remains in `europe-west3` and US data in `us-central1`, satisfying GDPR and HIPAA constraints. Envoy-based geo-routing, compression filters, and local Redis rate limiting protect backend services and maintain low-bandwidth availability for rural users.