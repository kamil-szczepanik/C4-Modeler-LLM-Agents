## Overview
A secure, cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency, regulatory compliance, and offline-resilient synchronization.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Compliance Officers / Auditors
- Web Frontend (PWA) with local SQLite caching
- Core Backend Services (Go / Spring Boot)
- AI Symptom Checker (Python / FastAPI)
- Data Storage: Cloud SQL (PostgreSQL), Google Cloud Storage (WORM buckets)
- Telemetry & Audit: Cloud Logging, BigQuery, Change Data Capture (Debezium / Cloud Pub/Sub)
- Cloud Infrastructure: GCP (`europe-west3`, `us-central1`) with Cloud KMS encryption

## Relationships
- Web Frontend -> Core Backend Services: Synchronizes state and handles mutations [HTTPS / GraphQL]
- Core Backend Services -> Cloud SQL (PostgreSQL): Reads and writes transactional FHIR health records [PostgreSQL Protocol / TLS 1.3]
- Core Backend Services -> Google Cloud Storage: Stores unstructured media and AI traceability inputs [HTTPS / GCP API]
- Core Backend Services -> Change Data Capture: Streams anonymized events [Pub/Sub Protocol]
- Compliance Officers -> BigQuery: Queries immutable audit logs and AI traceability data [SQL / IAM]

## Technology Stack
- **Cloud Provider**: GCP (`europe-west3` for EU, `us-central1` for US) to enforce strict geographical data segregation.
- **Relational Storage**: Cloud SQL for PostgreSQL with Row-Level Security for transactional FHIR records and consent states.
- **Object Storage**: Google Cloud Storage region-locked buckets with WORM policies for immutable AI traceability logs and media.
- **Audit & Analytics**: Cloud Logging and BigQuery for scalable, compliant audit querying without database write amplification.
- **Client State**: PWA with SQLite and CRDTs for offline-resilient sync in low-bandwidth rural areas.

## Rationale
This architecture ensures strict GDPR and HIPAA compliance by logically and physically isolating regional health data while providing immutable audit trails for AI medical device traceability. Furthermore, offline-capable PWA caching guarantees high availability and continuity of care for patients with unstable internet connections.