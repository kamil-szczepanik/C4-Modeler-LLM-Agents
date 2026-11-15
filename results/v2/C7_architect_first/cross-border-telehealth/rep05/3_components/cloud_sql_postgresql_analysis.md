## Overview
[Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. Ensures strict regional data isolation, regulatory compliance, and high availability for patients and clinicians.]

## Key Elements
*   Patients, Clinicians, Regional Pharmacists
*   EU National E-Prescription Gateways, US Pharmacy Networks, Regional Identity Providers
*   Web & Mobile App (Flutter / TypeScript)
*   API Gateway (Google Cloud API Gateway)
*   Core Services Container (Spring Boot / Java)
*   AI Symptom Checker Container (Python / FastAPI)
*   Integration Service Container (Node.js / TypeScript)
*   Video Media Server (LiveKit / WebRTC)
*   Cloud SQL (PostgreSQL) (PostgreSQL) with physically isolated instances in `europe-west3` and `us-central1`
*   Cloud Storage (Google Cloud Storage) with WORM configuration
*   Cloud Pub/Sub (Google Cloud Pub/Sub)

## Relationships
*   Core Services Container -> Cloud SQL (PostgreSQL): Reads and writes relational data via JDBC/SSL and PostgreSQL Wire Protocol
*   Core Services Container -> Connection Pooling Component: Manages database sessions via TCP/SSL
*   Audit & Compliance Logging Component -> Cloud Storage: Archives compliance logs and pgaudit outputs via Cloud Storage API
*   Web & Mobile App -> API Gateway: Routes client requests via HTTPS/REST and WebSockets

## Technology Stack
*   Google Cloud Platform (GCP): Target cloud provider utilizing `europe-west3` and `us-central1` for strict data residency.
*   Cloud SQL (PostgreSQL): Managed relational database providing synchronous High Availability (HA) and regional isolation.
*   Cloud KMS: Provides Customer-Managed Encryption Keys (CMEK) for regional data and audit log protection.
*   pgaudit & Cloud Storage: Enforces accountability and traceability for AI symptom checker outputs and PHI access.

## Rationale
[Physically isolated Cloud SQL instances per region enforce mandatory GDPR and HIPAA data residency constraints. Synchronous High Availability and Cloud SQL Auth Proxy guarantee sub-second clinician response times and zero data loss during failovers.]