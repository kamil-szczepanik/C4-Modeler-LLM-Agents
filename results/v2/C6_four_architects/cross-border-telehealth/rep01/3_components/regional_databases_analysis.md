## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients on GCP. It enforces strict regional data residency and GDPR/HIPAA compliance via isolated components in `europe-west3` and `us-central1`.

## Key Elements
- Transactional Store (Cloud SQL PostgreSQL)
- Document & Audit Store (Cloud Firestore)
- Blob Storage (Cloud Storage)
- Data Encryption Manager (Cloud KMS)
- Database Migration & Schema Manager (Flyway / Cloud Build)
- Regional Replica Router (Cloud SQL Proxy / Built-in HA)
- Database Backup & Retention Manager (Cloud Backup and DR / Storage Lifecycle)

## Relationships
- Core Telehealth Backend -> Transactional Store: Read/Write patient data and consent policies [TCP / PostgreSQL Wire Protocol]
- AI Symptom Checker -> Document & Audit Store: Write cryptographically signed audit logs [gRPC]
- Transactional Store, Document & Audit Store, Blob Storage -> Data Encryption Manager: Encrypt/Decrypt regional data at rest [Cloud KMS API / gRPC]
- Interoperability Adapter -> Transactional Store: Read/Write FHIR/national e-prescription data [TCP / PostgreSQL Wire Protocol]
- Database Migration & Schema Manager -> Transactional Store: Apply localized schema migrations [TCP / PostgreSQL Wire Protocol]
- Core Telehealth Backend -> Regional Replica Router: Route read-heavy queries to regional replicas [TCP / PostgreSQL Wire Protocol]
- Regional Replica Router -> Transactional Store: Replicate transactional data within the same region [TCP]
- Database Backup & Retention Manager -> Transactional Store & Blob Storage: Execute regional snapshots and lifecycle archival [GCP Internal API]

## Technology Stack
- Cloud SQL PostgreSQL: Region-locked relational storage for patient records and e-prescriptions
- Cloud Firestore: Document storage capturing immutable AI symptom-checker inputs and model versions
- Cloud Storage: Encrypted object storage for consultation artifacts with CMEK
- Cloud KMS: Regional Customer-Managed Encryption Keys ensuring cryptographic isolation
- Cloud SQL Proxy / Built-in HA: Localized read-scaling and automatic failover

## Rationale
This architecture uses region-locked GCP services and KMS encryption to strictly satisfy EU/US data residency mandates. Component separation ensures traceability, compliance, and disaster recovery.