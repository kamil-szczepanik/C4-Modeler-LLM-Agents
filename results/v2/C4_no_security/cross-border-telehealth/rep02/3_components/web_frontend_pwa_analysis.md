## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. It ensures strict data residency, regulatory compliance (GDPR/HIPAA/EU MDR), and high availability for rural areas.

## Key Elements
- Patients (EU & US) & Licensed Clinicians
- Web Frontend (PWA) (Next.js / React)
- API Gateway (Envoy & Cloud Load Balancing)
- Media Relaying Service (LiveKit SFU/MCU)
- Core Backend services (Go / Spring Boot)
- AI Symptom Checker (Python / FastAPI)
- Data Storage (Cloud SQL PostgreSQL & Cloud Storage)

## Relationships
- Patients & Clinicians -> Web Frontend (PWA): Accesses telehealth and video consultations [HTTPS / WSS]
- Web Frontend (PWA) -> API Gateway: Sends API requests and WebSocket traffic [HTTPS / WSS]
- Web Frontend (PWA) -> Media Relaying Service: Streams video and audio for consultations [WebRTC]
- API Gateway -> Core Backend services: Routes internal microservice requests [gRPC / HTTPS]
- Core Backend services -> Data Storage: Persists transactional health records [PostgreSQL Protocol / TLS]

## Technology Stack
- Next.js / React: Delivers a Progressive Web App (PWA) with offline-first capabilities for low-bandwidth rural connections.
- Google Cloud Platform (GCP): Hosts infrastructure across `europe-west3` and `us-central1` to enforce data residency.
- LiveKit: Manages real-time video and audio streaming with adaptive simulcast.
- IndexedDB & Service Workers: Enables local caching and offline payload queuing.

## Rationale
The architecture enforces strict regional isolation to comply with GDPR and HIPAA mandates. The PWA and adaptive WebRTC streaming ensure reliable care in unstable rural environments.