## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It bridges fragmented healthcare systems while strictly enforcing regional data residency and compliance.

## Key Elements
- **Users**: Patients and licensed clinicians accessing the platform.
- **Regional Platforms**: Two isolated instances deployed in GCP (`europe-west3` and `us-central1`).
- **External Systems**: National e-Prescription Gateways (EU), Pharmacy Networks (US), and Third-Party AI Model Providers.
- **Identity Providers**: External OAuth2/OIDC, EU eIDAS, and US Login.gov.
- **Infrastructure Services**: GCP Cloud Logging, Cloud KMS, and WORM storage.

## Relationships
- **Users to Platforms**: HTTPS, WebRTC with adaptive bitrates, and TLS 1.3.
- **Platforms to External Gateways**: REST and HL7 FHIR over secure mTLS.
- **Platforms to AI Providers**: HTTPS with pre-processor PII/PHI stripping.
- **Inter-service & Cross-region**: mTLS with consent-gated APIs.

## Technology Stack
- **Cloud Provider**: GCP (`europe-west3` and `us-central1`) for regional data isolation.
- **Infrastructure & GitOps**: Terraform and ArgoCD for isolated CI/CD pipelines.
- **Security & Encryption**: GCP Cloud KMS for Customer-Managed Encryption Keys (CMEK) and TLS 1.3.
- **Observability**: GCP Cloud Logging, OpenTelemetry, and WORM storage for immutable audit logs.
- **Interoperability**: HL7 FHIR (US) and national standards (EU).

## Rationale
Region-isolated deployments on GCP natively satisfy GDPR and HIPAA data residency constraints. Decoupled regional architectures and WORM audit logging ensure EU MDR traceability and compliance without sacrificing low-bandwidth availability.