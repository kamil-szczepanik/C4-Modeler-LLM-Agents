## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The system enforces strict regional data residency, regulatory compliance, and resilience for low-bandwidth users.

## Key Elements
* **Software System**: Cross-Border Telehealth Platform
* **Regional Instances**: EU Instance (GCP europe-west3), US Instance (GCP us-central1)
* **External Actors**: Patients (EU/US), Licensed Clinicians, Compliance/Audit Authorities
* **External Systems**: EU National E-Prescription Gateways, US Pharmacy Systems, Identity Providers (OAuth2/OIDC)
* **Containers & Components**: AI Symptom Checker, Adaptive Edge Media Relays (TURN/SFU), Regional Service Meshes (Istio)

## Relationships
* Patients and Clinicians interact with regional platform instances via HTTPS and WebRTC (SRTP/DTLS-SRTP).
* Regional instances communicate via encrypted, consent-gated gRPC/HTTPS using signed JWT tokens.
* EU Instance integrates with EU National E-Prescription Gateways via REST/SOAP.
* US Instance integrates with US Pharmacy Systems via HL7 FHIR and NCPDP.

## Technology Stack
* **Cloud Provider**: GCP (`europe-west3` and `us-central1`) for sovereign regional separation.
* **Service Mesh**: Istio for mTLS, egress filtering, and traffic encryption.
* **Security & Encryption**: Cloud KMS (Customer-Managed Encryption Keys - CMEK) and WORM logs.
* **Protocols**: HTTPS, WebRTC, gRPC, OAuth2/OIDC, HL7 FHIR.

## Rationale
The regional GCP split with sovereign instances ensures strict compliance with GDPR and HIPAA data residency mandates. Integrated adaptive media relays and WORM audit logs guarantee low-bandwidth accessibility and regulatory accountability.