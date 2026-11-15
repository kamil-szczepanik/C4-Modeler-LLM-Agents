## Overview
A multi-region cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The system enforces strict regional data residency and regulatory compliance under GDPR, HIPAA, and EU MDR.

## Key Elements
- **Patients**: Users accessing care, managing consent, and utilizing the AI symptom checker.
- **Licensed Clinicians**: Healthcare providers delivering video consultations and issuing cross-border e-prescriptions.
- **Compliance Officers**: Overseeing audit trails, AI traceability, and data residency.
- **Cross-Border Telehealth Platform**: Core GCP-hosted software system split across `europe-west3` and `us-central1`.
- **Video Infrastructure Provider**: Third-party WebRTC SFU handling low-bandwidth consultations.
- **AI Inference Engine**: External LLM service providing urgency recommendations.
- **Regional Pharmacy Gateways**: External HL7 FHIR APIs (US) and national gateways (EU).
- **Identity & Consent Providers**: Regional OIDC/OAuth2 authentication and consent management services.

## Relationships
- Patients & Clinicians to Cross-Border Telehealth Platform via HTTPS and WebSockets for application access and consultations.
- Cross-Border Telehealth Platform to Video Infrastructure Provider via HTTPS and WebSockets (WSS) for real-time video streaming.
- Cross-Border Telehealth Platform to AI Inference Engine via HTTPS (REST/gRPC) for symptom evaluation and urgencies.
- Cross-Border Telehealth Platform to Regional Pharmacy Gateways via HTTPS (HL7 FHIR / National APIs) for e-prescription delivery.
- Cross-Border Telehealth Platform to Identity Providers via OIDC/OAuth2 with FIDO2/WebAuthn for MFA.

## Technology Stack
- **Cloud Provider**: GCP (`europe-west3` for EU, `us-central1` for US) for strict regional isolation.
- **Data Protection**: Customer-Managed Encryption Keys (CMEK) and TLS 1.3 for encryption at rest and in transit.
- **Authentication**: OAuth2, OIDC, and FIDO2/WebAuthn for zero-trust multi-factor authentication.
- **Interoperability**: HL7 FHIR REST APIs for US pharmacies and national gateway standards for EU pharmacies.
- **Observability**: OpenTelemetry for distributed tracing and immutable logging of AI inputs/versions.
- **Infrastructure**: Terraform with Policy-as-Code (OPA) for IaC compliance and drift detection.

## Rationale
The architecture uses isolated GCP regions (`europe-west3` and `us-central1`) combined with mTLS and cryptographically verified consent tokens to strictly satisfy GDPR, HIPAA, and regional data residency constraints. Distributed tracing, immutable logging, and cryptographically signed AI outputs ensure full traceability for EU MDR compliance and secure cross-border healthcare delivery.