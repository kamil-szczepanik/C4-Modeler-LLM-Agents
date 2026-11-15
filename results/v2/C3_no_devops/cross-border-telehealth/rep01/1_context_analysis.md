## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. The system enforces strict regional data residency and compliance using a dual-region Google Cloud Platform architecture.

## Key Elements
- **Cross-Border Telehealth Platform**: Core system deployed across `europe-west3` and `us-central1`.
- **Patients (EU & US)** and **Licensed Clinicians**: Primary users interacting via HTTPS and WebSockets.
- **Pharmacies (EU & US)**: External partner systems receiving regional e-prescriptions.
- **External AI Inference Provider / LLM API**: Provides symptom-checker recommendations.
- **Identity Providers (IDPs)**: Regional Auth0 and GCP IAM services for authentication.
- **Billing & Insurance Providers**: External payment and claims systems.
- **Regulatory / Compliance Auditors**: External stakeholders accessing compliance logs.

## Relationships
- **Patients/Clinicians to Platform**: HTTPS / WebSockets for video consultations and AI triage.
- **Platform to Pharmacies**: HL7 FHIR (US) and national standards (EU) for e-prescriptions.
- **Platform to AI Inference Provider**: Secure API calls for symptom analysis and urgency recommendations.
- **Platform to Billing/Insurance**: Regional REST APIs with mTLS and data minimization.
- **Auditors to Platform**: Scoped OAuth tokens and mTLS for read-only audit log access.

## Technology Stack
- **Cloud Provider**: Google Cloud Platform (GCP) in regions `europe-west3` and `us-central1` for data residency.
- **Security & Encryption**: TLS 1.3 for data in transit; AES-256 with Customer-Managed Encryption Keys (CMEK) partitioned by region for data at rest.
- **Authentication**: OAuth 2.0, OIDC, JWT, and MFA via regional IDPs.
- **Interoperability**: HL7 FHIR for US healthcare data exchange and regional national standards for EU e-prescriptions.

## Rationale
This dual-region GCP architecture guarantees strict GDPR and HIPAA compliance by isolating EU and US health data within their respective geographic boundaries. Furthermore, regional API gateways, immutable cryptographic audit logging, and mTLS integration fulfill medical device traceability (EU MDR) and interoperability requirements without compromising data residency.