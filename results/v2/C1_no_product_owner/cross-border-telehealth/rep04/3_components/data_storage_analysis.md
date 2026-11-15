## Overview
The Data Storage container provides secure, region-locked persistence for the Cross-Border Telehealth Platform in GCP regions `europe-west3` and `us-central1`. It ensures strict adherence to GDPR, HIPAA, and EU MDR compliance via regional isolation and cryptographic audit logging.

## Key Elements
- Relational Database Component (Cloud SQL PostgreSQL)
- Object Storage Component (Google Cloud Storage)
- Audit & Traceability Ledger Component
- DataAccess Router (Internal Library/Sidecar)
- HL7/FHIR Mapping Schema layer

## Relationships
- Video Consultation Service -> Data Storage: Persists session data [gRPC/SQL via mTLS/TLS 1.3]
- AI Symptom Checker -> Data Storage: Persists symptom analysis logs and inputs [gRPC/SQL via mTLS/TLS 1.3]
- Consent Management Service -> Data Storage: Persists consent records [gRPC/SQL via mTLS/TLS 1.3]
- Data Storage -> Cloud Audit Logs: Streams audit and access logs [Cloud Logging API]

## Technology Stack
- Cloud SQL PostgreSQL: Stores transactional data, metadata, and audit logs with row-level security (RLS)
- Google Cloud Storage: Stores unstructured blobs and consultation recordings with regional bucket locks
- Customer-Managed Encryption Keys (CMEK): Enforces data-at-rest encryption across regions
- Google Cloud IAM Database Authentication: Eliminates static credentials using short-lived tokens

## Rationale
This architecture ensures regional compliance by restricting EU health data to `europe-west3` and US data to `us-central1` without cross-region replication leaks. Furthermore, it guarantees medical accountability and tamper-proof traceability for AI symptom-checker outputs under EU MDR through append-only ledgers and cryptographic hashing.