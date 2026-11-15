## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients on GCP. It ensures strict regional data residency, regulatory compliance, and high availability.

## Key Elements
* Patients (EU & US) and Licensed Clinicians
* Pharmacies (EU & US) and Compliance Officers
* Web & Mobile Client Containers (Flutter / React Native)
* API Gateway (Cloud Endpoints / Apigee)
* Core Telehealth Backend (Node.js / Go in GKE)
* Patient Consent & Preference Service (Go in GKE)
* Video Streaming Gateway (WebRTC SFU / MediaSoup on GCE/GKE)
* AI Inference Wrapper Service (Python / FastAPI)
* PostgreSQL Audit Ledger (Cloud SQL PostgreSQL + `pgaudit`)
* Object Versioning & Retention Manager (Cloud Storage with Object Lock)
* Partitioned Data Access Layer (PostgreSQL Table Partitioning)
* PITR Snapshot Scheduler and Automated Cross-Zone Replication Manager

## Relationships
* Client Containers -> API Gateway: HTTPS / REST and WSS for real-time messaging
* API Gateway -> Core Telehealth Backend & Services: gRPC / REST over internal VPC
* Core Telehealth Backend -> Video Streaming Gateway: WebRTC media streams and SIP/RTP
* Backend & AI Services -> Cloud SQL / Cloud Storage: TLS 1.3 with PgBouncer connection pooling and mTLS
* PITR Snapshot Scheduler -> Cloud SQL & Cloud Storage: Internal GCP APIs for automated backups

## Technology Stack
* GCP (`europe-west3`, `us-central1`): Target cloud provider enforcing regional data residency
* GKE & Cloud Endpoints/Apigee: Container orchestration and API management
* Node.js / Go / Python (FastAPI): Backend runtime and AI inference services
* WebRTC SFU (MediaSoup): Resilient video consultation streaming for low-bandwidth rural areas
* Cloud SQL (PostgreSQL) with `pgaudit`: Relational database with tamper-evident logging
* Cloud Storage with Object Lock (WORM): Immutable storage for AI model versions and session audits
* Cloud KMS (CMEK): Automated 90-day key rotation with region-isolated keys

## Rationale
The architecture combines regional isolation in GCP with CMEK encryption to satisfy GDPR and HIPAA mandates. PostgreSQL table partitioning, audit logging, and Cloud Storage WORM compliance ensure high availability, fast consent verification, and strict EU MDR AI traceability.