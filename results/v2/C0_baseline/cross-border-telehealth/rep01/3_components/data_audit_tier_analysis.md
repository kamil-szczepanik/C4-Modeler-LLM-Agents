## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. It ensures strict regulatory compliance (GDPR/HIPAA), data residency, and auditability.

## Key Elements
- Patients and Clinicians
- Compliance Officers
- API Gateway (Cloud Endpoints / Apigee)
- Regional Application Services (Google Kubernetes Engine)
- Video Consultation Service (Twilio / WebRTC Media Server)
- AI Symptom Checker (Vertex AI endpoints)
- Policy & Consent Engine (Open Policy Agent)
- Interoperability Adapter
- Data & Audit Tier (Cloud SQL for PostgreSQL, Cloud Storage WORM, BigQuery)

## Relationships
- Regional Application Services -> Cloud SQL for PostgreSQL: Read/write transactions via PostgreSQL Wire Protocol / TLS 1.3
- AI Symptom Checker -> Cloud Storage / BigQuery: Stream immutable logs via Cloud Pub/Sub
- Policy & Consent Engine -> Cloud SQL for PostgreSQL: Validates and logs access grants via gRPC
- Compliance Officer -> Cloud Storage / BigQuery: Queries immutable access and AI traceability logs via Cloud Identity-Aware Proxy (IAP) over HTTPS

## Technology Stack
- GCP (regions: europe-west3, us-central1): Chosen for multi-region deployment and compliance tooling.
- Cloud SQL for PostgreSQL: ACID compliance and row-level security for tenant data isolation.
- Cloud Storage WORM & BigQuery: Immutable audit storage and traceability for AI outputs (EU MDR/R-07).
- Cloud KMS (CMEK): Region-isolated key management for data residency and cryptographic erasure.
- Cloud Pub/Sub: Asynchronous, reliable event streaming with dead-letter queues.

## Rationale
This architecture guarantees strict regional data isolation and GDPR/HIPAA compliance by utilizing region-specific GCP infrastructure and CMEK encryption. Immutable audit ledgers and WORM storage ensure full traceability for AI medical device outputs and access transparency.