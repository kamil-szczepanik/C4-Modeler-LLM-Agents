## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency while ensuring high availability for rural users and compliance with GDPR, HIPAA, and EU MDR.

## Key Elements
* Patients (EU/US) & Licensed Clinicians
* Pharmacies & Compliance Officers / AI Safety Monitors
* Platform Administrators & Regional Identity Providers
* Web & Mobile Client Apps (Flutter/React Native)
* API Gateway (GCP Cloud Endpoints / Envoy)
* Core Telehealth Service (Go / gRPC)
* AI Symptom Checker Service (Python / FastAPI on Cloud Run)
* Video Session Manager (Node.js)
* E-Prescription Integrator (Java / Spring Boot)
* Regional Data Storage & Audit Layer (Cloud SQL, BigQuery)

## Relationships
* Patients and Clinicians interact with Web & Mobile Client Apps via HTTPS and WebSockets.
* Web & Mobile Client Apps communicate with the API Gateway via HTTPS/gRPC.
* API Gateway routes requests to internal containers using geo-DNS and validates tokens from Regional Identity Providers.
* Core Telehealth Service, AI Symptom Checker, and E-Prescription Integrator communicate internally via mTLS-secured gRPC.
* E-Prescription Integrator connects to Regional Pharmacy Networks using HL7 FHIR and national EU formats.
* Services persist transactional data and audit logs to Regional Data Storage & Audit Layer via VPC Service Controls.

## Technology Stack
* GCP (`europe-west3` and `us-central1`): Target cloud provider ensuring regional separation.
* Flutter / React Native: Client apps enabling offline-first caching for rural availability.
* Go, Python (FastAPI), Node.js, Java (Spring Boot): Backend services chosen for performance, ML integration, and enterprise integration.
* Cloud SQL (PostgreSQL) & BigQuery: Regional persistence and immutable audit logging for MDR traceability.
* GCP Cloud KMS & Secret Manager: Enforces CMEK encryption and secret rotation per region.

## Rationale
The architecture separates EU and US data persistence within GCP to satisfy GDPR and HIPAA residency mandates. Isolated container deployments and resilient edge controls ensure compliance, auditability, and continuous availability for rural users.