## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It unifies care under a single provider while strictly enforcing regional data residency and compliance.

## Key Elements
* Patients (EU and US mobile/web clients)
* Licensed Clinicians
* Local Pharmacies (EU and US)
* Identity Providers (IdP)
* Cross-Border Telehealth Platform (with `europe-west3` and `us-central1` regional instances)
* AI Triage Engine
* GCP Global External HTTP(S) Load Balancers and Regional SFUs

## Relationships
* Patients and Clinicians interact with the Platform via HTTPS and WebRTC (DTLS-SRTP) using adaptive bitrate codecs.
* Platform connects to External Pharmacies via national e-prescription standards (EU) and HL7 FHIR APIs (US) using mTLS and payload-level digital signatures.
* Users authenticate via federated OAuth 2.0 / OIDC with Identity Providers.
* AI Triage Engine logs immutable inference records internally via Cloud Audit Logs.

## Technology Stack
* GCP (`europe-west3` and `us-central1`): Chosen for regional isolation and compliance (GDPR/HIPAA).
* WebRTC SFUs & Global Load Balancers: Ensures video availability in degraded network conditions (<300 kbit/s).
* TLS 1.3, mTLS, and AES-256: Enforces strict data encryption in transit and at rest.
* Terraform & Cloud Build: Implements dual-region immutable infrastructure.
* Vertex AI Model Monitoring & Cloud Audit Logs: Provides traceability and immutable audit trails for AI recommendations.

## Rationale
This architecture guarantees strict regional compliance (GDPR/HIPAA) by isolating data in separate GCP regions without direct cross-border replication. It simultaneously ensures high availability and resilience for rural users through edge caching and adaptive media routing.