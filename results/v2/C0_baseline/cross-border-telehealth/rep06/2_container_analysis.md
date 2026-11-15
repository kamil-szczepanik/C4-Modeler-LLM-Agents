## Overview
A cross-border telehealth platform delivering video consultations, e-prescriptions, and AI symptom checking for EU and US patients. Built on GCP to guarantee regional data residency, regulatory compliance, and resilience for rural users.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Pharmacy Partners and Platform Administrators / Compliance Officers
- Client Applications: Patient Mobile/Web App (Flutter/React), Clinician Portal (React)
- Backend Services (Python/Go on GKE): API Gateway (Envoy/Kong), Core Telehealth Service, Interoperability & E-Prescription Adapter, Consent & Privacy Management Container, AI Orchestrator & Audit Service
- Media Relays: LiveKit/WebRTC Media Relays (TURN/STEF)
- Infrastructure: Isolated GKE clusters (`europe-west3`, `us-central1`), Istio Service Mesh, Cloud SQL (PostgreSQL), Cloud Spanner, Cloud KMS

## Relationships
- Patient App to API Gateway via HTTPS/WSS (OAuth2/OIDC, mTLS)
- Clinician Portal to API Gateway via HTTPS/WSS
- Interoperability Adapter to EU National E-Prescription Gateways and US Pharmacy Networks via REST/HL7 FHIR
- AI Orchestrator to External AI Inference Service via gRPC with local PII prompt sanitization
- Inter-Cluster Mesh (Istio) for secure gRPC/mTLS handshakes between `europe-west3` and `us-central1` with cryptographic consent tokens

## Technology Stack
- **Compute & Orchestration:** Google Kubernetes Engine (GKE) deployed in isolated regional clusters for strict data residency
- **Networking & Mesh:** Istio for federated service mesh and mTLS; Envoy/Kong API Gateway
- **Streaming & Telehealth:** LiveKit/WebRTC with SRTP/DTLS for adaptive sub-300 kbit/s video
- **Storage & Databases:** Cloud SQL (PostgreSQL) and Cloud Spanner for regionally-scoped data
- **Security & Compliance:** Cloud KMS with Customer-Managed Encryption Keys (CMEK) and WORM storage/BigQuery for immutable audit logs

## Rationale
Isolated regional GKE clusters and single-region databases strictly enforce GDPR, HIPAA, and EU data residency constraints (R-05). Adaptive WebRTC media relays and local caching ensure continuous availability for rural users on unstable connections (R-06).