## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and resilience for low-bandwidth rural connections.

## Key Elements
- **Users:** Patients, Licensed Clinicians, Compliance & Audit Officers
- **Systems:** EU Telehealth System, US Telehealth System, Global Identity Provider (IdP)
- **External Services:** Third-Party National E-Prescription Gateways (EU), Pharmacy Networks (US), Video Relay/Codec Service, Clinician Accreditation Validator
- **Infrastructure:** Centralized Observability Plane, Global Traffic Management (Anycast DNS), Regional KMS

## Relationships
- **Patients & Clinicians** -> **EU/US Telehealth Systems**: HTTPS (Web/Mobile) and WebRTC for low-bandwidth video
- **EU/US Telehealth Systems** -> **Global IdP**: OIDC/OAuth 2.0 over HTTPS with MFA
- **EU/US Telehealth Systems** -> **National E-Prescription Gateways / US Pharmacy Networks**: mTLS REST / HL7 FHIR
- **Compliance & Audit Officers** -> **Regional Systems**: Restricted HTTPS for audit log access

## Technology Stack
- **Cloud Provider:** Google Cloud Platform (GCP) deployed in `europe-west3` and `us-central1`
- **Security & Encryption:** TLS 1.3, mTLS, Customer-Managed Encryption Keys (CMEK) via regional KMS
- **Authentication:** OAuth 2.0 / OpenID Connect via Global IdP
- **Interoperability:** HL7 FHIR (US) and national standards (EU)
- **Networking & Resilience:** Envoy proxy sidecars for network shaping (sub-300 kbit/s degradation)

## Rationale
Sovereign regional boundaries (`europe-west3` and `us-central1`) strictly enforce GDPR and HIPAA data residency mandates without cross-region data replication. Decoupled container architectures and resilient video codecs guarantee continuous, low-bandwidth operational availability for rural users.