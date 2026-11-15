## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency and compliance using isolated cloud infrastructure.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- API Gateway & Consent Container (Envoy / Google Cloud Endpoints, Open Policy Agent)
- Core Telehealth Backend (Node.js/Go)
- Video Consultation Service (WebRTC / Janus Media Server on GCE MIGs)
- AI Symptom Checker (Python / FastAPI)
- Interoperability Adapter (Java / Spring Boot)
- Asynchronous Event Broker (GCP Pub/Sub)
- Dedicated Audit & Logging Container (Fluentbit / OpenTelemetry)
- Regional Databases (Cloud SQL PostgreSQL, Cloud Storage, Cloud Firestore)
- External Systems: National Pharmacies, National EHR Gateways, Payment Gateways (Stripe), Notification Providers (Twilio/Firebase)

## Relationships
- Patients/Clinicians to API Gateway via HTTPS/WSS
- Video Clients to Janus Media Server via WebRTC (UDP/TCP)
- API Gateway to Consent Container and Core Backend via gRPC over mTLS
- Core Backend to GCP Pub/Sub for asynchronous event distribution
- Interoperability Adapter to National Gateways and Pharmacies via mTLS over HTTPS
- Backends and AI containers to Audit Container via gRPC

## Technology Stack
- Google Cloud Platform (GCP): Multi-region deployment in `europe-west3` and `us-central1` for data residency.
- GCP VPC Service Perimeter (VPC-SC): Network-level isolation between regions.
- Google Cloud Run & GKE Autopilot: Stateless container orchestration for APIs, AI, and adapters.
- Google Compute Engine (GCE) Managed Instance Groups: Stateful media streaming for WebRTC.
- GCP Pub/Sub: Asynchronous event messaging and system decoupling.
- Cloud SQL PostgreSQL & Cloud Storage: Region-locked transactional storage with WORM immutability.

## Rationale
Isolated regional container clusters and VPC-SC enforce strict GDPR and HIPAA data residency constraints. Decoupled microservices, scalable WebRTC media servers, and asynchronous messaging ensure low-bandwidth resilience and high availability for rural users.