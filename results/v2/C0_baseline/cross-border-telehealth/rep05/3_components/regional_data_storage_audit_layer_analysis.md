## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The Regional Data Storage & Audit Layer ensures strict data residency, immutable compliance auditing, and low-latency transactions.

## Key Elements
* Transactional Database (Cloud SQL for PostgreSQL)
* Audit & Traceability Engine (BigQuery)
* Data Sync & Residency Enforcer (Cloud Dataflow / Pub/Sub)
* Data Access Layer (gRPC API)
* Target Cloud Regions: `europe-west3` (EU) and `us-central1` (US)

## Relationships
* Core Telehealth Service -> Transactional Database (Cloud SQL): Persists patient records, consents, and session states via gRPC/JDBC over VPC Service Controls
* AI Symptom Checker Service -> Audit & Traceability Engine (BigQuery): Appends immutable AI recommendation logs via BigQuery Storage Write API over VPC Service Controls
* E-Prescription Integrator -> Transactional Database (Cloud SQL): Persists prescription audit logs via gRPC/JDBC over VPC Service Controls
* Compliance Officers -> Data Access Layer (gRPC API): Queries audit trails and patient data via secure internal gRPC read API

## Technology Stack
* Cloud SQL for PostgreSQL: Enforces Row-Level Security and JSONB indexing for regional transactional data and FHIR resources
* BigQuery: Partitioned and clustered for high-performance compliance reporting and immutable AI audit trails
* Cloud KMS: Provides region-segregated Customer-Managed Encryption Keys (CMEK) for data at rest
* Cloud Dataflow & Pub/Sub: Manages asynchronous regional data replication and strict residency enforcement

## Rationale
This architecture guarantees strict regulatory compliance (GDPR and HIPAA) by isolating data within regional boundaries while maintaining high-performance transactions and immutable auditability. Separating transactional storage from analytical audit logging ensures rapid compliance reporting without impacting core telehealth service latency.