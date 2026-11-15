## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It runs on GCP with strict regional isolation to ensure GDPR and HIPAA compliance.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- API Gateway (Cloud Run / Envoy)
- Core Telehealth Backend (Node.js / NestJS) containing `ConsentManager`, `AuditLogger`, `FhirAdapter`, and `PatientPortalAPI` components
- AI Symptom Service (Python / FastAPI)
- Video Media Server (LiveKit / WebRTC)
- Interoperability Worker (Go)
- Cloud SQL (PostgreSQL), BigQuery, and Google Cloud Pub/Sub
- Cloud KMS

## Relationships
- API Gateway -> Core Telehealth Backend: Routes regional core requests via gRPC over VPC
- PatientPortalAPI -> ConsentManager: Validates purpose-based consent via in-process TypeScript calls
- ConsentManager -> Cloud SQL: Stores cryptographic consent tokens using Prisma ORM over regional VPC
- AuditLogger -> Cloud KMS: Encrypts audit payloads before transport via GCP KMS API
- AuditLogger -> Cloud Pub/Sub: Dispatches audit events asynchronously using Pub/Sub SDK

## Technology Stack
- Node.js / NestJS: Modular TypeScript backend framework for clear separation of regulatory boundaries
- Python / FastAPI: High-performance ML serving for the AI symptom checker
- LiveKit / WebRTC: Real-time video communication supporting degraded network modes
- Google Cloud Platform (Cloud Run, Cloud SQL, BigQuery, Pub/Sub, KMS): Managed cloud infrastructure providing strict multi-region data residency (`europe-west3` and `us-central1`)
- Terraform: Infrastructure-as-Code enforcing isolated regional deployment pipelines

## Rationale
This architecture uses modular NestJS components combined with regional GCP isolation and envelope encryption to strictly enforce HIPAA and GDPR data residency constraints. Local fallback buffers and WebRTC optimization ensure high availability and continuous care for users on unstable rural internet connections.