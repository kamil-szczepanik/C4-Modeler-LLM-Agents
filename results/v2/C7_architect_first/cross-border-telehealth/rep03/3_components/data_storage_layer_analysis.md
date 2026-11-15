## Overview
A secure, region-isolated Data Storage Layer built on GCP ensures strict compliance with GDPR and HIPAA for cross-border telehealth operations. It provides persistent storage, consent tracking, and traceable AI logs across European and US deployments.

## Key Elements
- EU Data Store: Deployed in `europe-west3` (`eu-postgresql` and `eu-bucket`)
- US Data Store: Deployed in `us-central1` (`us-postgresql` and `us-bucket`)
- Clinical Database (`Cloud SQL PostgreSQL`): Stores structured PHI/PII and e-prescriptions using Row-Level Security
- Consent & Audit Engine (`PostgreSQL Schema/Triggers`): Maintains immutable audit logs and granular consent states
- Blob Storage Repository (`Cloud Storage`): Handles unstructured media and raw AI payloads via regional buckets
- Data Access Proxy (`Envoy / Sidecar`): Intercepts traffic to inject regional context and validate client certificates
- PgBouncer: Manages connection pooling for high availability during peak hours

## Relationships
- Consultation Service -> Data Storage Layer: Reads and writes consultation data [SSL-enforced TCP/Postgres via mTLS]
- AI Symptom Checker Service -> Data Storage Layer: Reads and writes symptom check data and model versions [SSL-enforced TCP/Postgres]
- E-Prescription & Interoperability Service -> Data Storage Layer: Reads and writes prescription data [SSL-enforced TCP/Postgres]
- Data Access Proxy -> Cloud SQL PostgreSQL: Routes regional traffic and injects session context [Local TCP]

## Technology Stack
- Cloud SQL PostgreSQL: Selected for relational data management with native Row-Level Security (RLS) support.
- Cloud Storage: Chosen for secure, region-isolated unstructured media and audit log retention.
- Cloud KMS: Implemented for Customer-Managed Encryption Keys (CMEK) to enforce regional data encryption.
- Envoy / Sidecar & mTLS: Utilized for secure zero-trust service-to-database communication and client certificate verification.
- PgBouncer: Deployed for connection pooling and overload protection during traffic bursts.

## Rationale
This architecture physically separates EU and US health data into distinct GCP regions to guarantee GDPR and HIPAA compliance. Dedicated security controls, immutable audit logging, and localized backups ensure regulatory traceability without sacrificing system availability or performance.