## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict data residency, compliance, and adaptive performance for low-bandwidth users.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Platform Administrators / Compliance Officers
- External Pharmacies (EU & US)
- Web Frontend (PWA) built with Next.js/React
- API Gateway using Envoy and Cloud Load Balancing
- Core Backend services using Go/Spring Boot
- AI Symptom Checker using Python/FastAPI
- Integration / Interoperability Service using Node.js/Java
- Media Relaying Service using LiveKit (SFU/MCU)
- Data Storage using Cloud SQL (PostgreSQL) and Cloud Storage
- Google Kubernetes Engine (GKE) clusters in `europe-west3` and `us-central1`

## Relationships
- Web Frontend to API Gateway via HTTPS/WSS (WebRTC/WebSockets)
- API Gateway to Core Backend via REST/gRPC
- Core Backend to AI Symptom Checker via gRPC
- Core Backend to Integration Service via gRPC
- Integration Service to External Pharmacies via HL7 FHIR (US) and national e-prescription adapters (EU)
- Client apps to Media Relaying Service via WebRTC

## Technology Stack
- Next.js/React: Delivers a lightweight PWA for unstable rural connections
- Envoy / Cloud Load Balancing: Manages secure ingress traffic
- Go/Spring Boot: Powers robust core backend business logic
- Python/FastAPI: Executes AI symptom checker microservices
- LiveKit: Provides adaptive bitrate WebRTC media streaming for low-bandwidth resilience
- PostgreSQL / Cloud SQL: Secures regionalized health records per strict data residency rules
- Google Kubernetes Engine (GKE): Orchestrates containerized workloads across GCP regions

## Rationale
Regional GKE container deployment in `europe-west3` and `us-central1` strictly enforces GDPR and HIPAA data residency constraints. Modular integration adapters and adaptive WebRTC streaming ensure cross-border scalability and high availability in low-bandwidth environments.