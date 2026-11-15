## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and high availability for rural users.

## Key Elements
- Patients, Clinicians, Regional Pharmacists
- Web & Mobile App (Flutter / TypeScript)
- API Gateway (Google Cloud API Gateway)
- Core Services Container (Spring Boot / Java)
- AI Symptom Checker Container (Python / FastAPI)
- Integration Service Container (Node.js / TypeScript)
- Video Media Server (LiveKit / WebRTC)
- Cloud Pub/Sub (Google Cloud Pub/Sub)
- Cloud SQL (PostgreSQL), Cloud Storage (Google Cloud Storage)
- External Systems: EU National E-Prescription Gateways, US Pharmacy Networks, Regional Identity Providers

## Relationships
- Patients and Clinicians interact with the Web & Mobile App via HTTPS and WebRTC (for real-time video consultations).
- Web & Mobile App communicates with the API Gateway via HTTPS/REST.
- API Gateway routes requests to Core Services, AI Symptom Checker, and Integration Service containers via gRPC/HTTPS.
- Core Services and Integration Service publish and consume asynchronous events via Google Cloud Pub/Sub using TLS 1.3.
- Integration Service dispatches e-prescriptions to EU National E-Prescription Gateways and US Pharmacy Networks via REST/SOAP.

## Technology Stack
- GCP (europe-west3, us-central1): Chosen for multi-region scalability and strict data residency control.
- Google Cloud Pub/Sub: Selected for regional asynchronous event dispatch and decoupled messaging.
- Cloud KMS: Used for Customer-Managed Encryption Keys (CMEK) to secure data at rest.
- LiveKit / WebRTC: Provides reliable video streaming supporting degraded modes for unstable connections.

## Rationale
This architecture guarantees GDPR and HIPAA compliance by isolating EU and US data processing within dedicated GCP regions. The event-driven messaging strategy using Google Cloud Pub/Sub ensures resilient, prioritized delivery for critical healthcare workflows despite intermittent rural connectivity.