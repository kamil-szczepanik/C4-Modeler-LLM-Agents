## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency, GDPR/HIPAA compliance, and EU MDR AI traceability.

## Key Elements
* Patients and Clinicians (Users)
* API Gateway / Ingress (Envoy, GCP HTTPS Load Balancer)
* Video Consultation Service (Mediasoup WebRTC SFU containers)
* AI Symptom Checker Container (Python, FastAPI, PyTorch)
* E-Prescription Integration Container (Node.js, FHIR adapters)
* Patient Consent & Profile Container (Go)
* Data Tier (Cloud SQL PostgreSQL, Memorystore Redis with CMEK)
* Google Cloud Pub/Sub, OpenTelemetry, Cloud Audit Logs

## Relationships
* Users -> API Gateway / Ingress: HTTPS / WebRTC
* Video Consultation Service -> Data Tier: SQL with CMEK over internal GCP network [TLS 1.3 via PgBouncer]
* AI Symptom Checker Container -> Data Tier: SQL with CMEK over internal GCP network [TLS 1.3 via PgBouncer]
* E-Prescription Integration Container -> Data Tier: SQL with CMEK over internal GCP network [TLS 1.3 via PgBouncer]
* Patient Consent & Profile Container -> Data Tier: SQL with CMEK over internal GCP network [TLS 1.3 via PgBouncer]

## Technology Stack
* GCP (`europe-west3`, `us-central1`): Target cloud infrastructure ensuring regional isolation.
* Cloud SQL PostgreSQL: Relational store utilizing Row-Level Security (RLS) and append-only WORM tables for auditability.
* Memorystore Redis: Low-latency cache with pub/sub for dynamic consent token validation.
* Terraform & Cloud KMS: Infrastructure as code and regional key management for strict CMEK enforcement.

## Rationale
This architecture guarantees strict regional data residency and compliance via isolated GCP regions and append-only storage. Memorystore caching and PgBouncer connection pooling maintain low-latency performance for users with unstable internet connections.