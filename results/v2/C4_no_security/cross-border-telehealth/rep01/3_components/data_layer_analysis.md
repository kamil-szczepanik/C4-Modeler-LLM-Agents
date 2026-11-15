## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The architecture enforces strict regional data residency and GDPR/HIPAA compliance using Google Cloud Platform.

## Key Elements
- Patients (EU and US) and Licensed Clinicians
- Patient Portal (React, Flutter, IndexedDB)
- API Gateway / Region Router (Cloud Endpoints, Envoy)
- Core Telehealth Service, AI Gateway, Interoperability Adapter, Audit & Compliance Reporting Service (GKE, Node.js, Go, Python)
- WebRTC SFU Media Server (LiveKit, Janus)
- Data Layer Containers: Cloud SQL PostgreSQL, Firestore (Regional), Cloud Storage, Cloud KMS

## Relationships
- Patient Portal -> Sync & State Broker (Firestore): Real-time sync over HTTPS/WebSockets (regional endpoints)
- Core Telehealth Service -> Transactional Database (Cloud SQL): SQL over TLS 1.3
- AI Gateway -> Audit & Traceability Store: SQL over TLS 1.3 (write-once)
- Core Telehealth Service -> Encryption Key Manager (Cloud KMS): Envelope encryption via Cloud KMS API

## Technology Stack
- Google Cloud Platform (europe-west3 and us-central1): Enforces strict regional data residency requirements (R-05).
- Cloud SQL for PostgreSQL: Stores structured patient profiles, encrypted PHI, and consent states with row-level security.
- Firestore (Regional): Acts as a real-time sync and caching broker for intermittent connections (R-06).
- Cloud Storage: Encrypted with CMEK for consultation recordings and clinical documents with regional locks.
- Cloud KMS: Manages regional Customer-Managed Encryption Keys for cryptographic isolation and data purging.

## Rationale
This architecture guarantees strict regulatory compliance by physically isolating EU and US health data within designated regional GCP deployments. It ensures high availability and accountability for rural and intermittent connections while maintaining traceable AI symptom recommendations and robust audit logging.