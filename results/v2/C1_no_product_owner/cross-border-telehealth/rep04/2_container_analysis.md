## Overview
[Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients.]

## Key Elements
- Patients and Licensed Clinicians (Users)
- API Gateway (Cloud Endpoints / Envoy)
- Video Consultation Service (WebRTC SFU via LiveKit)
- AI Symptom Checker (Python / FastAPI)
- Interoperability Adapter (Node.js)
- Consent Management Service (Go / gRPC)
- Data Storage (Cloud SQL PostgreSQL + Cloud Storage)
- Regional GKE Clusters (`europe-west3`, `us-central1`)

## Relationships
- Clients to API Gateway via HTTPS/REST and WebSockets/WebRTC
- Containers to Containers via gRPC over mTLS
- Interoperability Adapter to National Gateways & FHIR via HTTPS/REST
- Global Management Plane via Istio service mesh

## Technology Stack
- GCP GKE: Isolated regional clusters for data residency compliance
- LiveKit: WebRTC SFU supporting degraded bandwidth under 300 kbit/s
- Python / FastAPI: Hosts AI symptom checker with model version logging
- Node.js: Interoperability adapter for HL7 FHIR and EU e-prescriptions
- Go: Consent management service for granular data sharing
- GCP Cloud SQL & Cloud Storage: Region-locked persistence with CMEK encryption

## Rationale
[Isolated regional clusters on GCP enforce strict GDPR and HIPAA data residency constraints. Zero-trust networking and inline consent checks guarantee secure cross-border compliance.]