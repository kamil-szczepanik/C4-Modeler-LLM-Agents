## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces regional data residency while ensuring GDPR, HIPAA, and EU MDR compliance.

## Key Elements
- **People:** Patients, Licensed Clinicians, Platform Administrators, Pharmacy/Compliance Auditors
- **Clients:** Web Application & Mobile Apps (Flutter/React)
- **Gateways & Routing:** Regional API Gateways (`europe-west3`, `us-central1`)
- **Core Services:** Core Telehealth Service (Go/Spring Boot), Video Mediation Service (Twilio/WebRTC), E-Prescription Integrator (Node.js), AI Orchestrator & Audit Logger (Python)
- **Messaging & State:** Google Cloud Pub/Sub, Cloud SQL for PostgreSQL, Memorystore for Redis
- **External Systems:** Local Pharmacies, EU National E-Prescription Networks, Third-Party Video Provider, AI Symptom Checker Model Registry, Identity Verification, Regional Payment Gateways

## Relationships
- **Clients to API Gateways:** HTTPS and WSS protocols
- **API Gateways to Core Services:** gRPC over mTLS within GCP VPC Service Control perimeters
- **Core Services to Messaging:** Asynchronous event publishing via Google Cloud Pub/Sub
- **Services to External Systems:** Secure REST/SOAP APIs integrating with HL7 FHIR (US) and EU national e-prescription standards

## Technology Stack
- **Cloud Provider:** Google GCP (`europe-west3` for EU, `us-central1` for US) to enforce regional data residency (R-05)
- **Frontend:** Flutter and React for multi-platform client applications
- **Backend Services:** Go and Spring Boot for Core Telehealth; Python for AI Orchestrator; Node.js for E-Prescription Integrator
- **Real-Time Communication:** Twilio/WebRTC wrapper supporting low-bandwidth degradation down to 300 kbit/s (R-06)
- **Data & Messaging:** Cloud SQL for PostgreSQL, Memorystore for Redis, and Google Cloud Pub/Sub with Cloud KMS payload encryption
- **Security & Compliance:** TLS 1.3, mTLS, Binary Authorization for AI models, and Cloud Storage WORM Object Lock for immutable audit logs (R-07)

## Rationale
This architecture isolates data regionally to satisfy strict GDPR and HIPAA mandates while utilizing decoupled microservices for high availability. Asynchronous messaging and WebRTC adaptation ensure resilience for rural users with unstable internet connections.