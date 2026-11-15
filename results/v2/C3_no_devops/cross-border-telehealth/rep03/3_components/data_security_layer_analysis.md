## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, privacy, and regulatory compliance (GDPR, HIPAA, and EU MDR) via GCP.

## Key Elements
* Patients and Licensed Clinicians (End Users)
* Pharmacies, National Health Authorities, and AI Inference Provider (External Systems)
* Web & Mobile Client Apps (Flutter / React Native)
* API Gateway (Google Cloud API Gateway / Apigee)
* Core Telehealth Service (Spring Boot / Java)
* AI Symptom Checker Service (FastAPI / Python)
* Interoperability & E-Prescription Service (Node.js)
* WebRTC SFU Media Relay (LiveKit on GKE)
* Data & Security Layer: Cloud SQL with PostgreSQL, Cloud Storage, GCP Cloud KMS, GCP Service Mesh with Istio, OPA Engine, WORM Bucket Lock, and Data Portability Exporter

## Relationships
* Client Apps -> API Gateway: HTTPS / REST and WSS for real-time messaging
* API Gateway -> Core Telehealth Service & AI Symptom Checker: gRPC / mTLS over GCP Service Mesh
* Core Telehealth Service -> Data & Security Layer: Encrypted PostgreSQL connections via Cloud KMS and gRPC over mTLS
* WebRTC SFU Media Relay -> Client Apps: WebRTC (UDP/TCP) for video/audio streams
* Interoperability Service -> External Pharmacies: HL7 FHIR (US) and national e-prescription standards (EU) over HTTPS

## Technology Stack
* Google Cloud Platform (GCP): Selected as cloud provider across `europe-west3` and `us-central1` for regional isolation.
* Cloud SQL (PostgreSQL): Used for relational data storage with Row-Level Security (RLS).
* GCP Cloud KMS & CMEK: Manages AES-256 encryption at rest with automatic 90-day key rotation.
* Open Policy Agent (OPA) & Istio: Enforces real-time consent (R-04) and service-to-service mTLS authorization.
* Cloud Storage WORM (Bucket Lock): Ensures tamper-proof audit logs for EU MDR traceability (R-07).

## Rationale
This architecture uses regional GCP deployment in `europe-west3` and `us-central1` to strictly enforce data residency mandates (GDPR/HIPAA). The integration of Istio, OPA, and Cloud KMS guarantees secure cross-border operations and traceable AI outputs while maintaining high availability.