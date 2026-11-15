## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture enforces strict regional data residency, GDPR/HIPAA compliance, and traceable AI outputs.

## Key Elements
- **People**: Patients, Licensed Clinicians, Local Pharmacists, Compliance Auditors, Platform Administrators
- **External Systems**: National EU E-Prescription Gateways, US Pharmacy Systems, WebRTC Video Infrastructure
- **Clients/Gateways**: Web Application & Mobile Client Gateway (React / React Native), API Gateway (Node.js / Go)
- **Services**: AI Symptom Checker Service (Python / FastAPI, Vertex AI), WebRTC Video Session Orchestrator (WebRTC, STUN/TURN)
- **Database and Storage**: Google Cloud SQL PostgreSQL (Enterprise Plus), Google Cloud Storage (Regional WORM)
- **Infrastructure/Mesh**: Istio Service Mesh, Envoy proxy

## Relationships
- **Web Application & Mobile Client Gateway -> API Gateway**: Sends client requests over HTTPS / REST and WSS.
- **API Gateway -> Database and Storage**: Persists patient data, operational records, and audit logs via PostgreSQL Wire Protocol over TLS 1.3 and gRPC over mTLS (Istio).
- **AI Symptom Checker Service -> Database and Storage**: Writes immutable audit logs to WORM storage and invokes Vertex AI via gRPC over mTLS (Istio) and Cloud APIs.
- **API Gateway -> National EU E-Prescription Gateways / US Pharmacy Systems**: Transmits prescriptions using HL7 FHIR (US) and national standards (EU).

## Technology Stack
- **Compute & Cloud**: Google Cloud Platform (GCP) deployed in `europe-west3` and `us-central1` for region-locked data residency.
- **Database**: Google Cloud SQL PostgreSQL with Row-Level Security (RLS) driven by consent metadata and short-lived IAM database tokens.
- **Storage**: Google Cloud Storage with WORM Bucket Lock and Customer-Managed Encryption Keys (CMEK) via Cloud KMS.
- **Networking & Security**: Istio Service Mesh with Envoy sidecar proxies enforcing TLS 1.3.

## Rationale
Isolated GCP projects and regional database instances guarantee compliance with EU GDPR and US HIPAA by preventing cross-border data transfer without explicit consent. WORM storage and automated audit logging satisfy EU MDR traceability and accountability requirements.