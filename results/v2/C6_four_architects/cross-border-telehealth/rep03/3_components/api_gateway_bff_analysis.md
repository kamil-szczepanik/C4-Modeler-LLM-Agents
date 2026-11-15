## Overview
[A secure, region-isolated Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients.]
[Enforces strict GDPR and HIPAA data residency constraints through localized GCP regional deployments.]

## Key Elements
- Patients and Clinicians (External Users)
- API Gateway / BFF (Go / Envoy)
- Video Consultation Service (Node.js / WebRTC SFU / Mediasoup)
- Clinical Core & E-Prescription Service (Java / Spring Boot)
- AI Symptom Checker Service (Python / FastAPI)
- Consent & Identity Management Service (Java / Spring Security)
- Notification & Pharmacy Integration Service (Go)
- Audit & Compliance Logger Sidecar (Fluentbit / Go)
- Cloud SQL PostgreSQL, Cloud Storage, Cloud Pub/Sub (Data Storage)
- Stripe Payment Gateways, Identity Providers (IdP), External Pharmacy Gateways (External Systems)

## Relationships
- Patients and Clinicians -> API Gateway / BFF: Sends API requests and connects via client apps [HTTPS / WSS (JSON/gRPC)]
- API Gateway / BFF -> Video Consultation Service: Routes consultation requests [gRPC over mTLS]
- API Gateway / BFF -> Clinical Core & E-Prescription Service: Routes clinical requests [gRPC over mTLS]
- API Gateway / BFF -> AI Symptom Checker Service: Routes AI symptom check requests [gRPC over mTLS]
- API Gateway / BFF -> Consent & Identity Management Service: Routes identity and consent requests [gRPC over mTLS]
- API Gateway / BFF -> Notification & Pharmacy Integration Service: Routes notification and pharmacy requests [gRPC over mTLS]
- API Gateway / BFF -> Stripe Payment Gateways: Processes payments [HTTPS / REST]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing regions `europe-west3` and `us-central1` for data residency.
- Go and Envoy: Used for the API Gateway, BFF, and edge routing to ensure high throughput and low latency.
- Java and Spring Boot: Chosen for the Clinical Core and Consent Management services for enterprise-grade security and reliability.
- Node.js with WebRTC SFU (Mediasoup): Implements scalable real-time video consultations supporting degraded network modes.
- Python and FastAPI: Powers the AI Symptom Checker service for high-performance ML model serving and traceability.
- Cloud SQL PostgreSQL: Relational database configured regionally to strictly isolate EU and US patient health data.

## Rationale
[Regional isolation via GCP guarantees that EU health data remains in europe-west3 and US data in us-central1, ensuring strict GDPR and HIPAA compliance.]
[Decoupled BFFs, rate-limiting proxies, and gRPC communication maintain high availability and performance even for rural patients with unstable connections.]