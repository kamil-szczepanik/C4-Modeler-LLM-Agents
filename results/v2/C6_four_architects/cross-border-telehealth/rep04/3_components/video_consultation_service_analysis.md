## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and the US. The architecture enforces strict regional data residency and compliance using GCP regions `europe-west3` and `us-central1`.

## Key Elements
- **Users**: Patient, Clinician
- **External Systems**: External Pharmacies, Identity Providers, Regional Regulatory Systems, National Health and Insurance Systems
- **Containers**: Web Application (React), Mobile App (Flutter), Ingress Layer (Google Cloud Global HTTPS Load Balancer, Google Cloud Armor, Google Cloud DNS), API Gateway (Google Cloud API Gateway), Core Telehealth Service (Node.js / Go), Video Consultation Service (LiveKit), AI Symptom Checker Service (Python / FastAPI), Consent Management Service (Go), E-Prescription & Interoperability Gateway (Node.js / TypeScript, Java / Spring Boot FHIR Adapter), Audit & Compliance Logging Service (Go), Pub/Sub (Google Cloud Pub/Sub), Cloud SQL (Google Cloud SQL for PostgreSQL)
- **Video Consultation Service Components**: Signaling Component (Node.js/Go), Media Router / SFU Node (LiveKit Server), Session Controller Component (Go), Bandwidth Adaptator (Go), Encryption & Compliance Proxy (C++/Go)

## Relationships
- API Gateway -> Video Consultation Service: Routes requests securely [gRPC over mTLS]
- Signaling Component -> Session Controller Component: Validates session access [Internal gRPC]
- Signaling Component -> Media Router: Manages room allocation and transport [WebRTC / WebSocket]
- Signaling Component -> Cloud SQL: Persists metadata and states [PostgreSQL Wire Protocol with TLS]
- Bandwidth Adaptator -> Media Router: Dynamically adjusts simulcast layers [LiveKit Server SDK]
- Session Controller Component -> Pub/Sub: Publishes audit events [gRPC over TLS]
- Encryption & Compliance Proxy -> Pub/Sub: Broadcasts telemetry [Cloud Pub/Sub API over TLS]

## Technology Stack
- **Cloud Provider**: Google Cloud Platform (GCP) (`europe-west3` for EU, `us-central1` for US) to enforce data residency
- **Backend & Services**: Go, Node.js / TypeScript, Python / FastAPI, Java / Spring Boot for microservices
- **Real-Time Video**: LiveKit Server (SFU) with WebRTC for video consultations
- **Database**: Google Cloud SQL for PostgreSQL for relational data
- **Messaging**: Google Cloud Pub/Sub for asynchronous event streaming
- **Interoperability**: HL7 FHIR (US) and national standards (EU)

## Rationale
The architecture ensures strict GDPR and HIPAA compliance by isolating regional health data within designated GCP boundaries. LiveKit SFU combined with a dedicated Bandwidth Adaptator guarantees reliable video consultations in degraded rural network conditions.