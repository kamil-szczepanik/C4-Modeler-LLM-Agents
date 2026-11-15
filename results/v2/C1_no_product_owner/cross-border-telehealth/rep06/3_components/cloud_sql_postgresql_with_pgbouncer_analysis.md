## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and high availability across unstable internet connections.

## Key Elements
* Patients (EU and US) and Licensed Clinicians
* React Web Application & React Native Mobile App
* GCP Cloud Endpoints / Envoy API Gateway
* Core Services Container (Node.js / NestJS)
* AI Symptom Checker Container (Python / FastAPI)
* Video Media Server (LiveKit / WebRTC SFU)
* Cloud SQL (PostgreSQL with PgBouncer): PgBouncer, PostgreSQL Database Engine, Audit & Traceability Subsystem (`pgaudit`), Regional Schema Partition Manager (PostgreSQL Schemas & RLS)
* GCP BigQuery

## Relationships
* Core Services Container -> PgBouncer: Forwards SQL queries [PostgreSQL Wire Protocol over SSL/TLS with mTLS]
* PgBouncer -> PostgreSQL Database Engine: Relays pooled queries [TCP / Unix Domain Sockets]
* Core Services Container -> Regional Schema Partition Manager: Executes context-aware queries enforcing region isolation [SQL via PgBouncer]
* Core Services Container -> Cloud SQL: Reads and writes transactional data [SSL/TLS-encrypted PostgreSQL connections]

## Technology Stack
* Google Cloud SQL for PostgreSQL 15+: Core transactional RDBMS ensuring strict ACID guarantees and region isolation.
* PgBouncer: Manages high-concurrency Node.js connections using transaction pooling.
* PostgreSQL native audit extensions (`pgaudit`): Satisfies HIPAA audit logging and EU MDR traceability.
* Terraform: Infrastructure-as-Code for provisioning regional instances across `europe-west3` and `us-central1`.
* Google Secret Manager & Cloud KMS: Manages dynamic credentials, automated rotation, and Customer-Managed Encryption Keys.

## Rationale
This architecture enforces data residency and compliance via regional partitioning in GCP (`europe-west3` and `us-central1`) combined with PostgreSQL Row-Level Security. Transaction pooling and encrypted mTLS connections secure high-concurrency telehealth workloads while maintaining strict auditability.