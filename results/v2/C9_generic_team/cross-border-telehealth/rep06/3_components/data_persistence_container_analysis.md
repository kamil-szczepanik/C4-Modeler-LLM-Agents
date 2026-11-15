## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system ensures strict data residency, regulatory compliance, and high availability over unstable connections.

## Key Elements
- Patients and Licensed Clinicians
- API Gateway / Edge Proxy Container (GCP Cloud Load Balancing / Envoy)
- Data Persistence Container (Cloud SQL / Cloud Spanner in GCP)
- Audit & Traceability Logging Container (GCP Pub/Sub / Cloud Logging)
- Identity & Access Management (IAM) Container (OAuth2 / OpenID Connect / JWTs)
- Integration & Translation Container (Node.js / GCP Cloud Run)

## Relationships
- Patients & Clinicians -> API Gateway / Edge Proxy Container: Accesses telehealth services [HTTPS / WebRTC]
- API Gateway -> Data Persistence Container: Queries and persists patient health records [gRPC over mTLS]
- Data Persistence Container -> GCP Cloud KMS: Encrypts data at rest with regionally segregated customer-managed keys [Internal GCP APIs]
- Data Persistence Container -> GCP Cloud Storage: Archives historical medical records to cold storage [Internal GCP APIs]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing `europe-west3` and `us-central1` regions for strict data residency.
- Cloud SQL / Cloud Spanner: Regional managed databases with Database Router pattern and Table partitioning for regional isolation.
- GCP Cloud KMS: Customer-managed encryption keys (CMEK) segregated per region for GDPR/HIPAA compliance.
- OpenTelemetry: Distributed tracing propagation spanning gRPC context down to SQL query comment tags.
- Flyway / Liquibase: CI/CD automated schema migration tools enforcing expand-and-contract zero-downtime deployments.

## Rationale
This architecture guarantees strict regional data partitioning and encryption-at-rest to satisfy GDPR and HIPAA mandates. It incorporates outbox patterns, connection pooling, and optimistic concurrency control to ensure resilience and data integrity for users with unstable internet connections.