## Overview
The Data Storage container provides region-locked primary relational databases, object storage, and immutable audit logs for the cross-border telehealth platform. It enforces strict HIPAA and GDPR compliance while maintaining isolated health data per region.

## Key Elements
- Regional Relational DB (Cloud SQL for PostgreSQL): Stores user profiles, appointments, and granular consent records.
- Regional Object Store (Google Cloud Storage): Stores e-prescription documents and encrypted consultation media.
- Audit & Traceability Store (Cloud Bigtable): Maintains append-only immutable logs for AI symptom-checker recommendations.

## Relationships
- Core Telehealth Service -> Regional Relational DB: Read/Write patient data and consent via PostgreSQL wire protocol (TCP/5432).
- AI Orchestrator -> Audit & Traceability Store: Append-only writes for AI traceability logs via Bigtable API (gRPC).
- E-Prescription Integrator -> Regional Object Store: Secure storage and retrieval of e-prescription artifacts via HTTPS (REST API/GCP SDK).

## Technology Stack
- Cloud SQL for PostgreSQL: Provides relational data management with CMEK encryption-at-rest for HIPAA/GDPR compliance.
- Google Cloud Storage: Delivers region-partitioned object storage for documents and media.
- Cloud Bigtable: Delivers scalable, append-only storage for immutable audit logging.

## Rationale
This component architecture enforces data residency by isolating storage instances within `europe-west3` and `us-central1`. Furthermore, it ensures medical device traceability (EU MDR) through WORM-secured audit logs.