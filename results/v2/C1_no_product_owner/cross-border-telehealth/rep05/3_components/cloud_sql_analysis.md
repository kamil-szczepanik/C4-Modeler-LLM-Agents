## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. It ensures strict regional data residency and regulatory compliance via dedicated Google Cloud regions.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- API Gateway (Go, Envoy)
- Consultation Service (Node.js, WebRTC) & SFU Media Relay (Mediasoup, C++)
- Clinical & Prescription Service (Java, Spring Boot)
- AI Symptom Checker (Python, FastAPI)
- Consent & Policy Engine (Go)
- Cloud SQL (PostgreSQL 15) with PgBouncer connection pooler
- Regional Message Broker (GCP Pub/Sub) and Immutable Audit Logging Service

## Relationships
- Clinical & Prescription Service -> PgBouncer: Queries clinical records [PostgreSQL Protocol over TLS 1.3]
- PgBouncer -> Primary DB Instance: Routes queries over local loopback [PostgreSQL Protocol / TLS 1.3]
- Cloud SQL -> Cloud KMS: Decrypts data at rest [Google Cloud API / IAM]
- Clinical & Prescription Service -> Cloud SQL: Reads and writes clinical data [PostgreSQL Protocol / KMS]
- Consent & Policy Engine -> Cloud SQL: Reads and writes consent records [PostgreSQL Protocol / KMS]

## Technology Stack
- Google Cloud Platform (GCP): Targeted for deployment in `europe-west3` and `us-central1` to enforce data residency.
- PostgreSQL 15 (Cloud SQL): Regional multi-zone HA database ensuring strict schema isolation and RLS for compliance.
- PgBouncer: Sidecar connection pooler managing high concurrency.
- pgAudit & Cloud KMS: Native auditing and CMEK encryption ensuring GDPR and HIPAA compliance.

## Rationale
This architecture guarantees strict regional data residency and regulatory compliance (GDPR/HIPAA) by isolating infrastructure within GCP regions. The use of managed databases, robust encryption, and schema-level separation ensures high availability, accountability, and secure clinical workflows.