## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. It operates under a single provider while strictly enforcing regional data residency and compliance.

## Key Elements
* Patients (EU/US) and Licensed Clinicians
* Cross-Border Telehealth Platform (Logically isolated regional instances: `europe-west3` and `us-central1` on GCP)
* Global Control Plane
* National e-Prescription Gateways (EU) and Pharmacy Systems (US) via HL7 FHIR
* Identity Providers (OAuth2/OIDC)
* AI Model Registry (locally deployed per region)
* Immutable Audit Logging Service

## Relationships
* Patients / Clinicians to Platform: HTTPS / WebRTC (with adaptive bitrate fallback)
* Platform to Identity Providers: OIDC / OAuth2 with MFA
* Platform to EU National Gateways / US Pharmacy Systems: HTTPS / HL7 FHIR
* Inter-region and External APIs: Mutual TLS (mTLS) with Customer-Managed Encryption Keys (CMEK)

## Technology Stack
* Google Cloud Platform (GCP): Chosen for regional control (`europe-west3`, `us-central1`) to satisfy GDPR and HIPAA data residency constraints.
* WebRTC: Powers video consultations with adaptive bitrate for rural, low-bandwidth connections (<300 kbit/s).
* HL7 FHIR & National Standards: Enables interoperability with US pharmacies and EU e-prescription gateways.
* Terraform & OPA/Gatekeeper: Enforces infrastructure-as-code and policy-as-code regional boundaries.
* JSON Web Tokens (JWT): Delivers cryptographically bound, short-lived tokens containing patient consent and jurisdiction claims.

## Rationale
This regionally isolated multi-region architecture ensures health data stays within its origin jurisdiction to comply with GDPR and HIPAA. Furthermore, localized AI model registries and cryptographically signed audit logs fulfill EU MDR traceability requirements while maintaining resilience for unstable rural connections.