## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency, GDPR/HIPAA compliance, and EU MDR traceability.

## Key Elements
- Patients, Clinicians, Regional Pharmacists
- Web & Mobile App (Flutter/TypeScript)
- API Gateway (Google Cloud API Gateway)
- Core Services Container (Spring Boot / Java)
- AI Symptom Checker Container (Python / FastAPI)
- Integration Service Container (Node.js / TypeScript)
- Video Media Server (LiveKit / WebRTC)
- Data Tier: Cloud SQL (PostgreSQL) and Cloud Storage
- Messaging: Cloud Pub/Sub
- Target Cloud: GCP (`europe-west3` and `us-central1`)

## Relationships
- Web/Mobile Apps to API Gateway via HTTPS/WebSockets
- API Gateway to Core Services via gRPC over mTLS
- Core Services to AI Symptom Checker via gRPC over mTLS
- Core Services to Integration Service via Cloud Pub/Sub (regionally isolated topics)
- Clients to Video Media Server via WebRTC (signaled via API Gateway)
- External integrations: HL7 FHIR for US, national standards for EU e-prescriptions

## Technology Stack
- Flutter/TypeScript for client apps for cross-platform support
- Spring Boot/Java for core business logic and consent management
- Python/FastAPI for AI symptom checker inference and logging
- LiveKit/WebRTC for low-bandwidth resilient video consultations
- Cloud SQL (PostgreSQL) & Cloud Storage for encrypted, region-isolated data persistence
- Google Cloud Pub/Sub for asynchronous e-prescription dispatch

## Rationale
Regional GCP isolation combined with VPC Service Controls strictly enforces EU and US data residency mandates. Asynchronous messaging and WebRTC optimization ensure high availability and graceful degradation for rural users with unstable internet connections.