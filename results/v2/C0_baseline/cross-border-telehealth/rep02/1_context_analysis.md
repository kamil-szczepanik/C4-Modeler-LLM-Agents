## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. It ensures strict data residency, regulatory compliance, and low-bandwidth resilience across borders.

## Key Elements
- Patients (EU & US)
- Licensed Clinicians
- Pharmacy Partners (EU & US)
- Compliance / Regulatory Officers
- Cross-Border Telehealth Platform (EU instance in `europe-west3`)
- Cross-Border Telehealth Platform (US instance in `us-central1`)
- Third-Party WebRTC SFU
- EU National E-Prescription Gateways and US Pharmacy Networks
- AI Model Registry / Inference Service

## Relationships
- Patients and clinicians interact with regional platform containers via HTTPS (TLS 1.3) and WebRTC (E2EE media streams).
- Regional platforms connect to EU/US national e-prescription gateways via REST/HL7 FHIR over mTLS.
- Platforms integrate with third-party WebRTC SFU using active-active edge routing and circuit-breaker patterns for low-bandwidth resilience.
- Regional instances interface with AI Inference Services via secure HTTPS/REST for triage recommendations.

## Technology Stack
- **Cloud Provider:** Google Cloud Platform (GCP) across `europe-west3` and `us-central1` for strict regional data silos.
- **Infrastructure & Deployment:** Terraform and ArgoCD for immutable GitOps-driven deployments.
- **Communication Protocols:** WebRTC with E2EE, mTLS for service-to-service communication, and OAuth2/OIDC for federated identity.
- **Interoperability Standards:** HL7 FHIR for US operations and national e-prescription standards for EU countries.
- **Observability:** OpenTelemetry collectors with PHI scrubbing.

## Rationale
Isolating regional deployments into separate GCP projects guarantees GDPR and HIPAA compliance while enforcing strict data residency. Active-active edge routing and WebRTC optimizations ensure high availability and low-bandwidth resilience for rural users.