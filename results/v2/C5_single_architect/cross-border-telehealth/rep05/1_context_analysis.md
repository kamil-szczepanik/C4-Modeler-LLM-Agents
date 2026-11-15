## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It guarantees strict regional data residency, regulatory compliance, and resilient low-bandwidth connectivity.

## Key Elements
- **Patients (EU/US)**: End-users accessing services via mobile and web clients.
- **Clinicians**: Healthcare providers conducting consultations and issuing e-prescriptions.
- **Cross-Border Telehealth Platform**: Core system split into isolated regional containers (`europe-west3` and `us-central1`).
- **AI Symptom Checker**: Component providing traceable care urgency recommendations.
- **Identity & Consent Provider**: Third-party/federated service managing OAuth2/OIDC authentication and consent ledgers.
- **External Systems**: EU National E-Prescription Gateways, US Surescripts/Pharmacy Clearinghouses, and AI Model Registry.

## Relationships
- **Patient/Clinician to Platform**: HTTPS / WebRTC (STUN/TURN) for video consultations and API requests.
- **Platform to EU Gateways**: REST using national e-prescription standards.
- **Platform to US Clearinghouses**: REST / HL7 FHIR protocols.
- **Platform to AI Model Registry**: gRPC / REST for symptom analysis and model version logging.
- **Platform to Identity Provider**: OAuth2 / OIDC over HTTPS.

## Technology Stack
- **Google Cloud Platform (GCP)**: Cloud provider utilizing `europe-west3` and `us-central1` for strict geographical data isolation.
- **WebRTC**: Powers video consultations with fallback codecs for connections under 300 kbit/s.
- **HL7 FHIR & National Standards**: Ensures interoperability with US and EU pharmacy systems respectively.
- **GCP Identity-Aware Proxy (IAP)**: Enforces regional token validation and jurisdictional security.

## Rationale
This architecture strictly enforces data residency via regional GCP deployments to satisfy GDPR and HIPAA mandates. It maintains high availability and clinical accountability through robust degraded-mode streaming and immutable AI model logging.