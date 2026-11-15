## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It guarantees strict regional data isolation to comply with GDPR, HIPAA, and EU MDR regulations.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Core Telehealth Service (Go / Spring Boot)
- AI Orchestrator & Audit Logger (Python)
- Cloud SQL for PostgreSQL (PostgreSQL database with Core Data, Consent Ledger, and AI Audit Log schemas)
- Memorystore for Redis (Redis caching layer)
- Google Cloud IAM and Cloud KMS (Security and Key Management)

## Relationships
- Core Telehealth Service -> Cloud SQL for PostgreSQL: Reads and writes relational data via TLS/PostgreSQL Protocol using PgBouncer connection pooling
- AI Orchestrator & Audit Logger -> Cloud SQL for PostgreSQL: Writes audit logs and symptom-checker inputs via PostgreSQL Protocol using IAM authentication
- Core Telehealth Service -> Memorystore for Redis: Caches user profiles and session states via Redis Protocol with mTLS

## Technology Stack
- Google Cloud Platform (europe-west3, us-central1): Chosen for regional data residency enforcement
- Cloud SQL for PostgreSQL: Chosen for native multi-zone High Availability, regional read replicas, and relational data integrity
- Cloud KMS: Used for Customer-Managed Encryption Keys (CMEK) to enforce regional data protection
- Google Cloud IAM: Used for database authentication and principle-of-least-privilege access control

## Rationale
Isolating regional Cloud SQL instances in `europe-west3` and `us-central1` ensures EU patient health data never leaves the EU, satisfying GDPR, HIPAA, and EU MDR constraints. Built-in HA, read replicas, and Redis caching deliver low-latency performance for critical telehealth workflows under strict security controls.