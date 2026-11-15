## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency while ensuring secure, compliant cross-border medical operations.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Web/Mobile Client Application (Flutter / React)
- Cloud Load Balancing & Envoy API Gateway (Envoy & GCP Cloud Load Balancing)
- Core Telehealth & Consent Container (Go)
- AI Symptom Checker Container (Python / FastAPI)
- Prescription Integration Container (Go)
- External Systems: National E-Prescription Networks (EU), US Pharmacy Systems, WebRTC SFU Media Relay, Break-Glass Identity Provider (IdP), Immutable Storage
- GCP Infrastructure: GCP Pub/Sub, GCP Memorystore (Redis), GCP Cloud KMS, GCP Certificate Authority Service

## Relationships
- Prescription Integration Container -> National E-Prescription Networks (EU): Transmits e-prescriptions via mTLS and HTTPS (HL7 FHIR / EU standards)
- Prescription Integration Container -> US Pharmacy Systems: Transmits pharmacy requests via mTLS and HTTPS (HL7 FHIR)
- Web/Mobile Client Application -> Envoy API Gateway: Routes requests via HTTPS and WSS
- Prescription Integration Container -> GCP Pub/Sub: Manages asynchronous message queuing for retry handling
- Prescription Integration Container -> GCP Memorystore (Redis): Tracks idempotency keys via Redis protocol

## Technology Stack
- Go: Language for backend services and the Prescription Integration Container to ensure high concurrency and performance.
- Python / FastAPI: Framework for the AI symptom checker container supporting traceable medical device outputs.
- GCP Pub/Sub & Memorystore: Messaging and caching technologies providing asynchronous retry handling and idempotency persistence.
- mTLS & OAuth 2.0 (RFC 8693): Security protocols enforcing cryptographic token exchange and authenticated network transport.

## Rationale
The regional deployment model across `europe-west3` and `us-central1` strictly satisfies GDPR and HIPAA data residency mandates. Asynchronous queuing, circuit breakers, and idempotency ledgers ensure high availability and prevent duplicate prescription dispatches during unstable network conditions.