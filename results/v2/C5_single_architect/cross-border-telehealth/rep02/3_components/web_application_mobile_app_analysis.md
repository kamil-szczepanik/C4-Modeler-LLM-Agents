## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict regional data residency, regulatory compliance (GDPR/HIPAA/MDR), and resilience for rural areas.

## Key Elements
- Patients (EU/US) & Licensed Clinicians
- Web Application & Mobile App (React, Flutter)
- API Gateway (Google Cloud API Gateway / Envoy)
- Core Telehealth Service (Go / Spring Boot)
- AI Symptom Checker Orchestrator (Python / FastAPI)
- E-Prescription Integration Service (Node.js / Java)
- Media Relay & Signaling Service (WebRTC / LiveKit)
- Cloud SQL PostgreSQL (PostgreSQL) & Memorystore Redis (Redis)

## Relationships
- Patients & Clinicians -> Web Application & Mobile App: Access telehealth services via HTTPS and WSS
- Web Application & Mobile App -> API Gateway: Application traffic and signaling via HTTPS and WSS (WebSockets)
- API Gateway -> Core Services: Internal routing via gRPC and HTTPS
- E-Prescription Integration Service -> National Gateways/Pharmacies: Transmits prescriptions using HL7 FHIR (US) and national standards (EU)

## Technology Stack
- GCP (europe-west3, us-central1): Chosen for regional isolation enforcing data residency constraints
- Flutter / React: Cross-platform client framework for web and mobile
- LiveKit / WebRTC: Adaptive bitrate streaming for low-bandwidth video consultations (<300 kbit/s)
- PostgreSQL / Redis: Regional data storage and caching ensuring HIPAA/GDPR compliance

## Rationale
The multi-region GCP architecture strictly separates EU and US data to satisfy GDPR and HIPAA requirements while maintaining low-latency routing. Adaptive WebRTC streaming and offline-first client caching guarantee high availability and usability for patients in rural areas with unstable internet connections.