## Overview
Cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. Ensures strict regional data residency and compliance with GDPR, HIPAA, and EU MDR.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Frontend Client Apps (Flutter)
- API Gateway / BFF (Envoy / gRPC-Web)
- AI Symptom Checker Container (Python / FastAPI)
- Video Consultation Service (WebRTC / SFU - Mediasoup)
- E-Prescription Integration Service (Node.js / Express)
- Consent & Policy Engine (Opa / Go)
- AI Diagnostic Service (External)
- Data Layer (PostgreSQL / Cloud SQL)

## Relationships
- Patients/Clinicians -> Frontend Client Apps [HTTPS / WSS]
- Frontend Client Apps -> API Gateway / BFF [gRPC-Web, mTLS]
- API Gateway / BFF -> AI Symptom Checker Container [gRPC, mTLS]
- AI Symptom Checker Container -> AI Diagnostic Service [gRPC, Regional Isolation]
- API Gateway / BFF -> Consent & Policy Engine [gRPC]
- AI Symptom Checker Container -> Local Secure Volume [Append-only I/O]

## Technology Stack
- GCP (regions: europe-west3, us-central1): Enforces strict regional data residency requirements.
- Google Kubernetes Engine (GKE): Container orchestration with HPA and network policies.
- Python / FastAPI: High-performance framework for the AI Symptom Checker.
- PostgreSQL / Cloud SQL: Secure relational data storage per region.
- OpenTelemetry & Fluent Bit: Distributed tracing and audit log shipping.

## Rationale
This architecture uses regional GCP deployments and strict network isolation to satisfy GDPR, HIPAA, and data residency mandates. Containerized microservices with local audit logging and fallback mechanisms ensure high availability, EU MDR traceability, and resilience for rural users.