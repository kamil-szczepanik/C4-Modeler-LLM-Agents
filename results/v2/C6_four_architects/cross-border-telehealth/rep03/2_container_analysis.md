## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency while ensuring HIPAA and GDPR compliance.

## Key Elements
- Patients and Clinicians (Users)
- API Gateway / BFF (Go / Envoy)
- Video Consultation Service (Node.js / WebRTC SFU / Mediasoup)
- TURN/STUN Relay Server (Coturn)
- Clinical Core & E-Prescription Service (Java / Spring Boot)
- AI Symptom Checker Service (Python / FastAPI)
- Consent & Identity Management Service (Java / Spring Security)
- Notification & Pharmacy Integration Service (Go)
- Audit & Compliance Logger Sidecar (Fluentbit / Go)
- Data Storage (Cloud SQL PostgreSQL, Cloud Storage, Cloud Pub/Sub)
- External Systems: External Pharmacy Gateways, Identity Providers, Stripe Payment Gateways

## Relationships
- Patient/Clinician Apps -> API Gateway / BFF: HTTPS / WSS (JSON/gRPC)
- API Gateway -> Internal Containers: gRPC over mTLS (Istio Service Mesh)
- Video Consultation Service -> TURN/STUN Server: UDP/TCP (WebRTC)
- Notification Service -> External Pharmacy Gateways: HTTPS/REST (TLS 1.3)
- All Services -> Regional Cloud SQL / Cloud Storage: PostgreSQL Wire Protocol / HTTPS with CMEK

## Technology Stack
- Cloud Provider: GCP (`europe-west3` and `us-central1`) for isolated regional data residency
- Container Orchestration: Google Kubernetes Engine (GKE) with Istio Service Mesh for zero-trust mTLS
- Video & Networking: Mediasoup SFU and Coturn for low-bandwidth (<300 kbit/s) resilience
- Backend & APIs: Go, Java (Spring Boot), Python (FastAPI), with gRPC and REST protocols
- Data & Messaging: Cloud SQL (PostgreSQL), Cloud Storage, and Cloud Pub/Sub for asynchronous event bus

## Rationale
Isolated regional GKE clusters ensure health data never crosses borders without explicit consent, satisfying GDPR and HIPAA constraints. Dedicated WebRTC and SFU components guarantee reliable video consultations even on unstable rural internet connections.