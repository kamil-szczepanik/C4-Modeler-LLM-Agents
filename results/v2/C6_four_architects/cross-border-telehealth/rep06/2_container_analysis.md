## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency while ensuring compliance with GDPR, HIPAA, and EU MDR.

## Key Elements
- Patients and Clinicians (Web & Mobile Apps using React / React Native)
- Google Cloud API Gateway with Open Policy Agent (OPA)
- Core Telehealth Service (Go)
- AI Symptom Checker Service (Python / FastAPI)
- Video Streaming Service (mediasoup SFU on GCP Compute Engine with TURN/STUN relay)
- Integration Service (Node.js)
- Datastores (Cloud SQL PostgreSQL, Memorystore Redis, Google Cloud BigQuery / Cloud Storage)
- Regional Deployments (`europe-west3` and `us-central1`)

## Relationships
- Patients & Clinicians to API Gateway via HTTPS, WSS, and WebRTC/UDP
- API Gateway to Core Telehealth & AI Services via internal gRPC
- AI Symptom Checker to Audit Log Store via Google Cloud Pub/Sub
- Integration Service to external pharmacy networks via national standards and HL7 FHIR
- Cross-region access between gateways via federated mTLS over HTTPS

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Enforces regional isolation and data residency
- Go: Powers the Core Telehealth Service for reliable business logic execution
- Python / FastAPI: Runs inference for the AI Symptom Checker Service
- WebRTC / mediasoup & TURN/STUN: Handles video streaming and rural low-bandwidth connections (<300 kbit/s)
- Open Policy Agent (OPA): Evaluates dynamic, purpose-based patient consent policies
- Cloud SQL PostgreSQL & Memorystore Redis: Provides region-isolated transactional and cache storage
- Google Cloud BigQuery / Cloud Storage: Maintains immutable audit logs for AI traceability

## Rationale
Isolated regional deployments in GCP ensure patient data remains within its source jurisdiction to satisfy GDPR and HIPAA. Asynchronous messaging via Cloud Pub/Sub and resilient WebRTC streaming maintain high availability and performance even over unstable rural internet connections.