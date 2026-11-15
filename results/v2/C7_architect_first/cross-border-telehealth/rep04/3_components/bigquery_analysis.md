## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The system ensures strict data residency, privacy compliance, and EU MDR traceability across regional environments.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- Compliance Authorities and Clinical Operations Managers
- Google Cloud Platform (GCP) target cloud in `europe-west3` (EU) and `us-central1` (US)
- API Gateway (Cloud Run / Envoy) and Core Telehealth Backend (Node.js / NestJS)
- AI Symptom Service (Python / FastAPI) and Video Media Server (LiveKit / WebRTC)
- Cloud SQL (PostgreSQL), Cloud Pub/Sub, and Google Cloud BigQuery
- Regional Datasets (EU/US), BigQuery Write API, and Authorized Views

## Relationships
- AI Symptom Service -> Cloud Pub/Sub: Streams unmasked symptom inputs and model versions [gRPC / Pub/Sub API]
- Cloud Pub/Sub -> EU/US Analytics Datasets: Batch-loads audit logs via BigQuery Storage Write API [gRPC]
- AI Symptom Service / Compliance Portal -> Analytical Views: Queries aggregated AI metrics and audit reports [BigQuery SQL API]
- BigQuery Reservation API -> EU/US Analytics Datasets: Allocates and isolates compute capacity [Management API]

## Technology Stack
- Google Cloud BigQuery: Chosen for regional datasets to enforce strict EU/US data residency compliance.
- Cloud Pub/Sub: Used as a batching buffer for telemetry to prevent ingest throttling and smooth out traffic spikes.
- BigQuery Authorized Views: Selected to safely expose aggregated metrics to internal teams and auditors without exposing raw PHI.
- Cloud KMS: Implements Customer-Managed Encryption Keys (CMEK) with regional key segregation.

## Rationale
This architecture uses regional GCP infrastructure, strict IAM boundaries, and automated pseudonymization to satisfy GDPR, HIPAA, and EU MDR constraints. Separating regional storage and batching telemetry through Pub/Sub ensures compliance, availability, and scalable audit traceability.