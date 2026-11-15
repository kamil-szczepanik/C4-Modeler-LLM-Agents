## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict regional data residency, GDPR/HIPAA compliance, and EU MDR traceability on Google Cloud Platform.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- Clinician Portal (React / TypeScript SPA)
- Auth & Jurisdiction Context Manager
- Consultation Workspace
- AI Triage & Audit Widget
- Offline Draft Manager (IndexedDB)
- E-Prescription & Record Manager
- API Gateway (GCP Cloud Endpoints)
- Core Telehealth Service (Go)
- AI Symptom Service (Python / FastAPI)
- Third-Party Video SDK

## Relationships
- Clinician Portal accesses API Gateway via HTTPS/REST and gRPC-Web
- Consultation Workspace integrates Third-Party Video SDK via WebRTC
- Consultation Workspace utilizes Offline Draft Manager via IndexedDB for local persistence
- AI Triage & Audit Widget communicates with API Gateway via HTTPS/JSON for audit logging

## Technology Stack
- React / TypeScript: Frontend framework for the Clinician Portal SPA
- Google Cloud Platform: Target cloud provider across `europe-west3` and `us-central1`
- GCP Cloud Storage and Cloud CDN: Multi-region static asset delivery
- IndexedDB: Local browser storage for offline draft persistence
- WebRTC: Real-time protocol for video consultations
- OpenTelemetry JS: Client-side telemetry and monitoring

## Rationale
The architecture isolates regional state and enforces strict data residency in compliance with GDPR and HIPAA mandates. Multi-region GCP deployment combined with local offline capabilities ensures high availability for users in rural areas with unstable connections.