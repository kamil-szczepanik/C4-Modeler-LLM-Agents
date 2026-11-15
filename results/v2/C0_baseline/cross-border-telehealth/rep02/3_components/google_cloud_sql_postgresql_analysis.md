## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system guarantees strict regional data residency and compliance using isolated GCP infrastructure and PostgreSQL.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Web / Mobile Client (React / React Native)
- API Gateway (Envoy / Cloud Endpoints)
- Core Telehealth Service (Node.js / NestJS)
- Google Cloud SQL (PostgreSQL) Container
- PostgreSQL RDBMS Engine with Row-Level Security (RLS)
- PgBouncer Connection Pooler (configured in session mode)
- CMEK (Customer-Managed Encryption Keys) Module via Google Cloud KMS
- Audit & Activity Logging Daemon (`pgAudit` with Google Cloud Logging / BigQuery)

## Relationships
- Core Telehealth Service -> PgBouncer Connection Pooler: Routes transactional queries and passes session context over [TCP/TLS]
- PgBouncer Connection Pooler -> PostgreSQL RDBMS Engine: Forwards pooled queries maintaining session state for RLS over [TCP/TLS]
- PostgreSQL RDBMS Engine -> Google Cloud KMS: Manages regional encryption keys using CMEK over [HTTPS]
- Audit & Activity Logging Daemon -> Google Cloud Logging/BigQuery: Streams audit trails for traceability over [HTTPS]

## Technology Stack
- Google Cloud SQL (PostgreSQL): Regional databases in `europe-west3` and `us-central1` to enforce data residency
- PgBouncer: Connection pooling with session-level isolation to support RLS safely
- Google Cloud KMS: Customer-Managed Encryption Keys (CMEK) for data-at-rest encryption
- `pgAudit`: Detailed audit logging for EU MDR and HIPAA compliance
- VPC Service Perimeter (VPC-SC): Network isolation with Cloud SQL Auth Proxy

## Rationale
Regional Cloud SQL instances paired with CMEK ensure strict adherence to EU and US data residency mandates. Furthermore, combining PostgreSQL Row-Level Security with PgBouncer session pooling guarantees that patient consent constraints are enforced directly at the data layer without performance degradation.