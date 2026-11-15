## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency while ensuring regulatory compliance, high availability, and interoperability.

## Key Elements
- **Clients**: Web App & Mobile App (Flutter/React)
- **Edge Routing**: GCP API Gateway
- **Core Services**: Core Telehealth Backend (Go/Spring Boot), AI Symptom Checker Service (Python/FastAPI)
- **Streaming**: Video Streaming Server (WebRTC/SFU - Mediasoup)
- **Integration**: EU E-Prescriptions Adapter (Java/Spring Boot), US Healthcare Interoperability Service (Node.js/FHIR SDK)
- **Infrastructure**: GKE Autopilot, Anthos Service Mesh (Istio), GCP Cloud SQL (PostgreSQL), Cloud Storage (WORM buckets), Cloud KMS, GCP Secret Manager

## Relationships
- **Clients to API Gateway**: HTTPS and WebSockets
- **API Gateway to Core Backend**: mTLS via Anthos Service Mesh (Istio), validating user consent tokens
- **Core Backend to AI Service / Adapters**: mTLS internal service-to-service communication
- **Adapters to External Systems**: Egress-filtered HTTPS to national e-prescription gateways (EU) and HL7 FHIR endpoints (US)
- **Video Streaming to Clients**: WebRTC adaptive bitrate streams

## Technology Stack
- **GCP (`europe-west3`, `us-central1`)**: Cloud provider and regional data partitioning
- **GKE Autopilot & Istio**: Container orchestration and zero-trust mTLS service mesh
- **WebRTC (Mediasoup)**: Video streaming with <300 kbit/s degraded mode support
- **Cloud SQL & Cloud KMS**: Regional transactional persistence with CMEK encryption
- **OpenTelemetry & WORM Buckets**: Traceability and compliance logging for EU MDR (R-07)

## Rationale
This architecture isolates data regionally to satisfy strict GDPR and HIPAA mandates while utilizing GKE and Istio for robust security and observability. Decoupled integration adapters and adaptive streaming ensure low-bandwidth resilience and seamless cross-border interoperability.