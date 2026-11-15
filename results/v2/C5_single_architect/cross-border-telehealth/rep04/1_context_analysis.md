## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and interoperability across international healthcare networks.

## Key Elements
- **Cross-Border Telehealth Platform**: Core system deployed on GCP (`europe-west3` and `us-central1`).
- **Patient**: End-user utilizing mobile and web clients.
- **Clinician**: Licensed medical professional conducting consultations and issuing prescriptions.
- **External Pharmacy Systems**: Receives e-prescriptions via regional protocols.
- **AI Model Provider / LLM API**: External service powering the symptom checker.
- **National Identity Providers**: External authentication systems using eIDAS and Login.gov.
- **National Health Registries**: Country-specific health data exchanges and US HIEs.

## Relationships
- **Patient -> Cross-Border Telehealth Platform (HTTPS/WebRTC)**: Video consultations, symptom checks, and consent management.
- **Clinician -> Cross-Border Telehealth Platform (HTTPS)**: Consultations and prescription authoring.
- **Cross-Border Telehealth Platform -> External Pharmacy Systems (REST/FHIR)**: E-prescription dispatch.
- **Cross-Border Telehealth Platform -> National Identity Providers (OIDC/SAML)**: User authentication and jurisdictional verification.
- **Cross-Border Telehealth Platform -> National Health Registries (REST/FHIR)**: Patient history and audit compliance.

## Technology Stack
- **GCP (`europe-west3`, `us-central1`)**: Multi-region cloud infrastructure ensuring data residency constraints are met.
- **WebRTC**: Low-bandwidth video consultations supporting degraded modes below 300 kbit/s.
- **HL7 FHIR & National EU Standards**: Interoperability protocols for US health data and EU e-prescriptions.
- **OIDC/SAML**: Authentication protocols for cross-border trust federations (e.g., eIDAS).

## Rationale
This architecture guarantees strict regional data isolation to satisfy GDPR and HIPAA mandates while utilizing federated identity and standard interoperability protocols. The multi-region GCP deployment combined with robust WebRTC and FHIR integration ensures high availability, traceability for EU MDR, and reliable performance in low-bandwidth rural areas.