## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency and compliance using Google Cloud Platform.

## Key Elements
- Patients (EU and US)
- Licensed Clinicians
- Cross-Border Telehealth Platform (GCP hosted in europe-west3 and us-central1)
- External Pharmacies (EU national e-prescription networks and US pharmacy systems)
- Regional Payment Gateways (Stripe/regional processors)
- Health Authorities & Auditors (FDA, EMA, national ministries)
- Identity Providers (eIDAS for EU, OAuth2/OIDC for US)

## Relationships
- Patients & Clinicians -> Cross-Border Telehealth Platform via HTTPS and WebRTC (SRTP/DTLS-SRTP)
- Cross-Border Telehealth Platform -> External Pharmacies via REST and HL7 FHIR
- Cross-Border Telehealth Platform -> Regional Payment Gateways via HTTPS REST API
- Health Authorities & Auditors -> Cross-Border Telehealth Platform via zero-trust read-only audit proxies over HTTPS

## Technology Stack
- Google Cloud Platform (GCP): Deployed in `europe-west3` and `us-central1` for data residency compliance
- WebRTC / SRTP: For video consultations with low-bandwidth adaptation (<300 kbit/s)
- HL7 FHIR & REST: For US pharmacy interoperability and external integrations
- WORM Storage: For immutable regional AI symptom-checker audit logging (R-07)
- OAuth2 / OIDC / eIDAS: For federated authentication and consent-driven access control (R-04)
- GCP Cloud CDN: For global edge caching of static client assets

## Rationale
This architecture isolates data regionally in GCP to strictly satisfy GDPR and HIPAA mandates while supporting cross-border care. It ensures high availability and accountability for rural users and regulated medical AI tools through robust edge routing and immutable regional logging.