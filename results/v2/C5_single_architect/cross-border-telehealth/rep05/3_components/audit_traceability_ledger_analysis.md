## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. The architecture enforces strict regional data residency, HIPAA/GDPR compliance, and EU MDR auditability.

## Key Elements
- **Users**: Patients (EU and US), Licensed Clinicians, Authorized Auditors
- **External Systems**: Identity & Consent Provider, EU National E-Prescription Gateways, US Surescripts/Pharmacy Clearinghouses, AI Model Registry
- **Containers**: API Gateway, Core Telehealth Service, Video Media Server (WebRTC SFU), AI Inference Wrapper, Integration Service, Audit & Traceability Ledger, Datastores (Cloud SQL PostgreSQL)
- **Components (Audit & Traceability Ledger)**: Ingest Router, Compliance & Residency Enforcer, Ledger Storage Adapter, Audit Query API

## Relationships
- AI Inference Wrapper -> Ingest Router: Publishes audit events via gRPC over Cloud Pub/Sub
- Compliance & Residency Enforcer -> BigQuery: Writes region-locked audit records via BigQuery Storage API (HTTPS/gRPC)
- Authorized Auditors -> Audit Query API: Queries compliance logs via gRPC over mTLS (HTTPS)
- Video Media Server -> Patients: Streams consultations via WebRTC with adaptive bitrate (< 300 kbit/s degraded mode)
- Integration Service -> EU Gateways / US Surescripts: Transmits e-prescriptions using national EU standards and HL7 FHIR

## Technology Stack
- **Cloud Provider**: Google Cloud Platform (GCP regions `europe-west3` and `us-central1`) for regional data isolation
- **Orchestration**: Google Kubernetes Engine (GKE) for container hosting
- **Backend Languages**: Go for core services, Python for AI workloads on Vertex AI
- **Messaging & Storage**: Cloud Pub/Sub for asynchronous ingestion, BigQuery with WORM policies for immutable audit ledgers, Cloud SQL PostgreSQL for transactional data

## Rationale
This architecture guarantees strict regional data residency by isolating workloads and data across dedicated GCP regions. Furthermore, the specialized Audit & Traceability Ledger ensures verifiable EU MDR and HIPAA compliance through immutable logging and strict access controls.