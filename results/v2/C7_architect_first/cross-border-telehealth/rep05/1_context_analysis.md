## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. The architecture enforces strict regional data residency and compliance using isolated GCP deployments.

## Key Elements
- **Users**: Patients (Mobile/Web clients) and Clinicians (Web clients).
- **Secondary Actors**: Regional Pharmacists.
- **Core Platform**: Dual-region Cross-Border Telehealth Platform (`europe-west3` and `us-central1`).
- **External Systems**: EU National E-Prescription Gateways, US Pharmacy Networks, Regional Identity Providers (OIDC/OAuth2).
- **Edge Layer**: GCP Global Load Balancer with Cloud Armor.

## Relationships
- **Clients to Edge**: Patients and Clinicians connect via TLS 1.3 to GCP Global Load Balancer with geo-routing.
- **Edge to Regions**: Global Load Balancer routes traffic to regional instances (`europe-west3` / `us-central1`).
- **Platform to E-Prescriptions**: Integrates with EU National Gateways and US Pharmacy Networks using REST and HL7 FHIR.
- **Cross-Region Federation**: Restricted metadata sharing via mTLS with regional service mesh attestation, requiring explicit patient consent (R-04).

## Technology Stack
- **Cloud Provider**: GCP (`europe-west3` for EU, `us-central1` for US) for strict regional isolation.
- **Edge Security**: GCP Cloud Armor and Global Load Balancer for geo-routing and DDoS protection.
- **Authentication**: OIDC/OAuth2 with FIDO2/WebAuthn for phishing-resistant MFA.
- **Interoperability**: HL7 FHIR (US) and national standards (EU) for e-prescriptions (R-08).
- **Video & Telemetry**: WebRTC supporting audio-first degradation below 300 kbit/s (R-06).
- **Audit & Compliance**: GCP Cloud Logging and immutable GCP Storage Buckets with Bucket Lock for AI traceability (R-07).
- **Supply Chain**: Cosign artifact signing for version-locked EU MDR compliance.

## Rationale
This architecture ensures strict GDPR and HIPAA compliance by physically siloing regional health data while enabling federated cross-border care via explicit consent. Independent regional pipelines and immutable logging fulfill EU MDR medical device traceability and high-availability requirements.