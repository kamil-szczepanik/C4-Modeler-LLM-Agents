## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict regional data residency, regulatory compliance, and interoperability across dual GCP environments.]

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- GeoDNS (Anycast)
- API Gateway / Edge Proxy
- Web/Mobile Client App
- Core Telehealth Service
- AI Symptom Checker Service
- Consent & Policy Engine
- Interoperability / Integration Service
- Audit & Compliance Logger Container
- Video Streaming / SFU (LiveKit/Mediasoup)
- GCP Cloud SQL (PostgreSQL) and GCP Cloud Storage
- GCP Pub/Sub
- External Systems: National Pharmacies, National EHR Gateways, Payment Gateways (Stripe), Notification Providers (Twilio/Firebase)

## Relationships
- Patients/Clinicians to API Gateway via HTTPS, WebSockets, and WebRTC (UDP/TCP)
- Client to Video SFU via WebRTC
- Interoperability Service to US Pharmacies/EHRs via HL7 FHIR over REST/TLS
- Interoperability Service to EU Pharmacies/EHRs via National e-Prescription APIs over REST/TLS
- Containers to Pub/Sub via gRPC
- Containers to Regional Databases and Cloud Storage via HTTPS/REST (TLS 1.3)
- Platform to Payment and Notification Providers via HTTPS/REST

## Technology Stack
- Cloud Provider: GCP (`europe-west3` for EU, `us-central1` for US) to enforce regional data isolation
- Routing: GeoDNS for regional entry points
- Real-Time Media: WebRTC and SFU (LiveKit/Mediasoup) for low-bandwidth degradation (<300 kbit/s)
- Messaging: GCP Pub/Sub for asynchronous event-driven architecture
- Storage: GCP Cloud SQL (PostgreSQL) and GCP Cloud Storage with Customer-Managed Encryption Keys (CMEK)
- Interoperability: HL7 FHIR (US) and National e-Prescription APIs (EU)

## Rationale
- Dual-region GCP deployments with strict network separation guarantee GDPR and HIPAA compliance while keeping health data within its required jurisdiction.
- Decoupled microservices, regional databases, and specialized SFU media streaming ensure high availability, traceability for EU MDR, and robust performance for rural users.