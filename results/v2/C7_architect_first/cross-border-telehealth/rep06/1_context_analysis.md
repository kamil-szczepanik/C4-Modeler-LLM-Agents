## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It guarantees strict regional data residency, HIPAA/GDPR compliance, and EU MDR traceability.

## Key Elements
- Patients and Licensed Clinicians (Mobile/Web clients)
- EU Telehealth System (`europe-west3`) and US Telehealth System (`us-central1`)
- AI Symptom Checker Subsystem
- External EU National E-Prescription Gateways and US Pharmacy Networks
- Third-Party Video Infrastructure (WebRTC)
- Zero-Trust Consent Gateways

## Relationships
- Patients/Clinicians to Platforms: HTTPS (REST/GraphQL) and WebRTC (secure SRTP/DTLS)
- Internal Services: mTLS for service-to-service communication
- Platform to External Pharmacies/Gateways: REST/FHIR over mTLS
- Cross-Region Access: Cryptographically isolated Consent Gateway proxies with OAuth 2.0 and signed consent scopes

## Technology Stack
- Cloud Provider: GCP (`europe-west3` and `us-central1`) with VPC Service Controls for isolation
- Encryption: TLS 1.3, Cloud KMS with Customer-Managed Encryption Keys (CMEK)
- Authentication: OAuth 2.0 / OIDC with MFA and ABAC
- Interoperability: HL7 FHIR (US) and national e-prescription standards (EU)
- Infrastructure/Logging: Terraform/OpenTofu, GCP Cloud Logging with bucket-lock for immutable audit trails

## Rationale
This architecture isolates regional deployments to strictly enforce GDPR and HIPAA data residency constraints. Zero-trust consent gateways and immutable logging ensure legal compliance, EU MDR traceability, and secure telehealth delivery over global networks.