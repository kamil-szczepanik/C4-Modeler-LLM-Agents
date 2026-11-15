## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. The architecture enforces strict regional isolation on Google Cloud Platform to comply with GDPR and HIPAA data residency requirements.

## Key Elements
- Patients and Clinicians (External Users)
- GCP Global HTTPS Load Balancer with Geo-routing
- Envoy API Gateway
- Backend Service & Consent & Policy Service (Open Policy Agent)
- AI Symptom Checker Service (FastAPI)
- SFU Media Relay (LiveKit / Mediasoup)
- Integration Adapter Container
- Cloud SQL for PostgreSQL & Memorystore for Redis
- GCP Cloud Storage with Object Retention (WORM)
- External Regional Pharmacy Networks, HIEs, and AI Model Providers

## Relationships
- Patients/Clinicians to GCP Global HTTPS Load Balancer via HTTPS
- Load Balancer to regional Envoy API Gateway via HTTPS/REST
- Internal containers to containers via gRPC over Istio mTLS
- SFU Media Relay to Clients via UDP (ICE/STUN/TURN)
- Integration Adapter to external HIEs/Pharmacies via mTLS/HTTPS
- AI Symptom Checker to Cloud Storage via GCP IAM

## Technology Stack
- Cloud Provider: GCP (`europe-west3` and `us-central1`) for regional data isolation
- Orchestration: Google Kubernetes Engine (GKE) with Istio Service Mesh for secure internal traffic
- Ingress/Security: Envoy Proxy and Google Cloud Armor for edge routing and TLS termination
- Databases: Cloud SQL for PostgreSQL (relational data/FHIR/consent) and Memorystore for Redis (sessions/WebRTC)
- Storage: GCP Cloud Storage with WORM object retention for immutable AI audit logs
- Media: LiveKit or Mediasoup SFU for adaptive WebRTC video streaming

## Rationale
The regionally isolated GKE container topology guarantees that EU and US health data never cross borders without explicit consent. Utilizing dedicated security, storage, and interoperability adapters ensures full compliance with GDPR, HIPAA, and EU MDR while supporting resilient low-bandwidth video consultations.