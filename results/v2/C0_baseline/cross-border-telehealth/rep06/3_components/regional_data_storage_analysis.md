## Overview
[Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients while strictly enforcing regional data residency and compliance.]

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- EU National E-Prescription Gateways and US Pharmacy Networks
- API Gateway (Envoy / Kong)
- Core Telehealth Service and Interoperability & E-Prescription Adapter (Python / Go on GKE)
- Consent & Privacy Management Container (Python / Go on GKE)
- AI Orchestrator & Audit Service (Python / Go on GKE)
- Regional Data Storage Container (Cloud Spanner / Cloud SQL PostgreSQL, Cloud KMS, WORM Storage)
- Internal Storage Components: Transaction Database, Sync & Conflict Resolution Engine, Audit & WORM Ledger, Key Management Module, Data Access Proxy

## Relationships
- Core Telehealth Service -> Data Access Proxy: Queries regional data with context propagation [gRPC]
- Data Access Proxy -> Transaction Database: Executes tenant-isolated, row-level secured queries [SQL]
- Data Access Proxy -> Audit & WORM Ledger: Asynchronously streams read/write access logs [Pub/Sub / gRPC]
- Core Telehealth Service -> Sync & Conflict Resolution Engine: Synchronizes offline payloads [gRPC]
- Sync & Conflict Resolution Engine -> Transaction Database: Persists synchronized records [SQL]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing regions `europe-west3` and `us-central1`.
- Cloud Spanner / Cloud SQL (PostgreSQL): Regional transaction databases ensuring ACID compliance and data residency.
- Cloud KMS: Regional Customer-Managed Encryption Keys (CMEK) ensuring cryptographic data isolation between EU and US.
- Cloud Storage with Object Retention / BigQuery: WORM ledger storage providing immutable, tamper-proof audit logs.
- Go / Envoy: Language and proxy foundation for the high-performance Data Access Proxy and Sync Engine.

## Rationale
[This architecture enforces GDPR and HIPAA compliance by isolating EU and US data regionally via Cloud KMS and Cloud Spanner. It supports rural intermittent connectivity through a dedicated sync engine while ensuring traceablity for AI recommendations and patient consent via WORM ledgers and row-level security.]