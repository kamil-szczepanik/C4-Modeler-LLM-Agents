## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and resilience for unstable rural connections.

## Key Elements
- Patients and Clinicians (Users)
- Web/Mobile Client SPA/PWA (Flutter/React)
- Google Cloud API Gateway (Entry point)
- Data Residency & Consent Router (Go)
- Core Services Backend (Go/Spring Boot)
- AI Symptom Checker Service (Python/FastAPI)
- Video Streaming Server (LiveKit WebRTC SFU on GKE)
- Interoperability Adapter (Node.js/TypeScript)
- Cloud SQL PostgreSQL (Regional Data Storage)
- External Systems: Pharmacy Systems, LLM API, National ID Providers, Health Registries

## Relationships
- Patients/Clinicians to API Gateway via HTTPS/WSS
- API Gateway to Data Residency & Consent Router via gRPC
- Core Services to Cloud SQL via TCP/SQL
- Video Streaming Server to Clients via WebRTC over UDP/TCP
- AI Symptom Checker to External LLM API via HTTPS

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Enforces regional data isolation.
- Go: Used for Consent Router and Core Services for low latency and minimal footprint.
- Python/FastAPI: Powers the AI Symptom Checker for ML library compatibility.
- LiveKit (WebRTC SFU): Supports adaptive video streaming below 300 kbit/s.
- TypeScript: Powers Interoperability Adapter for FHIR/JSON manipulation.
- Cloud SQL PostgreSQL: Stores partitioned regional transactional data.

## Rationale
Isolated regional GCP deployments and a dedicated Consent Router strictly enforce EU GDPR and US HIPAA data residency boundaries. Specialized WebRTC and interoperability adapters ensure low-bandwidth resilience and seamless cross-border regional health data integration.