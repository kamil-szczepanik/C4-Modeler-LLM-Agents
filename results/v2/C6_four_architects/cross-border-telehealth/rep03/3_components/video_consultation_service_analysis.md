## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and AI symptom checking for patients across the EU and US. The system enforces strict regional data residency, HIPAA/GDPR compliance, and high availability in low-bandwidth rural areas.

## Key Elements
* Patients and Clinicians (Users)
* API Gateway / BFF (Go / Envoy)
* Video Consultation Service (Node.js / Mediasoup) with internal components: Signaling, SFU Router, Adaptive Transcoder, Session Policy Enforcer, Compliance Audit Interceptor, TURN/STUN Orchestrator, Media Quality Monitor, Room State Manager, and Media Encryption Enforcer
* TURN/STUN Relay Server (Coturn)
* Clinical Core & E-Prescription Service (Java / Spring Boot)
* AI Symptom Checker Service (Python / FastAPI)
* Consent & Identity Management Service (Java / Spring Security)
* Notification & Pharmacy Integration Service (Go)
* Audit & Compliance Logger Sidecar (Fluentbit / Go)
* Data Storage: Cloud SQL PostgreSQL, Cloud Storage, Cloud Pub/Sub

## Relationships
* API Gateway / BFF -> Video Consultation Service: Routes consultation requests [gRPC over mTLS]
* Video Consultation Service -> TURN/STUN Relay Server: Relays encrypted SRTP media streams [UDP/TCP via TURN]
* Video Consultation Service -> Clinical Core & E-Prescription Service: Verifies appointment authorization [gRPC over mTLS]
* Compliance Audit Interceptor -> Audit & Compliance Logger Sidecar: Streams session telemetry [gRPC]
* Signaling Component -> Room State Manager Component: Reads/writes active session states [TCP/Redis]

## Technology Stack
* GCP (europe-west3, us-central1): Chosen to natively enforce strict regional data residency constraints.
* Node.js & Mediasoup: Selected for real-time WebRTC video streaming and adaptive transcoding.
* Go & Envoy: Utilized for high-performance API routing and backend-for-frontend services.
* Java & Spring Boot: Deployed for core clinical workflows requiring enterprise security and reliability.
* Python & FastAPI: Powers the AI symptom checker to integrate seamlessly with ML ecosystems.
* PostgreSQL & Cloud Pub/Sub: Provides reliable relational data storage and asynchronous messaging.

## Rationale
The architecture strictly segregates EU and US data processing to comply with GDPR and HIPAA mandates while utilizing cloud-native regional deployments. Adaptive transcoding and robust SFU routing guarantee resilient video consultations for rural patients on unstable connections.