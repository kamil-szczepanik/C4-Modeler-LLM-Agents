## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency and regulatory compliance on GCP.

## Key Elements
- Patients and Clinicians (EU and US)
- Cross-Border Telehealth Platform (Regional instances in `europe-west3` and `us-central1`)
- API Gateway (Envoy)
- Video Consultation Service (MediaSoup WebRTC SFU)
- AI Symptom Checker Container (Python/FastAPI)
- E-Prescription Integration Service
- Consent & Audit Ledger
- Regional Data Store (Google Cloud Spanner / PostgreSQL)
- Async Event Bus (Google Cloud Pub/Sub)
- External Pharmacy Gateways, Identity Providers (IdP), and Payment Gateways (Stripe)

## Relationships
- Patients/Clinicians to API Gateway: HTTPS, WebRTC, OIDC/OAuth2
- API Gateway to Internal Containers: gRPC over internal VPC
- Services to Cloud Pub/Sub: gRPC / TLS
- AI Symptom Checker to Data Store: SQL over TLS
- Platform to Pharmacy Gateways: mTLS, REST, SOAP, HL7 FHIR
- Platform to Payment Gateways: HTTPS, REST with webhooks

## Technology Stack
- Cloud Platform: GCP (`europe-west3` for EU, `us-central1` for US) to enforce data residency
- API Gateway: Envoy for TLS termination, routing, and rate limiting
- Video Streaming: MediaSoup (WebRTC SFU) for handling connections below 300 kbit/s
- Backend Services: Python (FastAPI) for the AI symptom checker container
- Database: Google Cloud Spanner / PostgreSQL with encryption for regional data storage
- Messaging: Google Cloud Pub/Sub for asynchronous event decoupling

## Rationale
The dual regional deployment on GCP strictly fulfills GDPR, HIPAA, and data residency constraints by isolating EU and US data. Containerizing the AI symptom checker and video SFU ensures regional regulatory traceability and high availability under unstable internet connections.