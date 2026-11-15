## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. It ensures strict regional data residency, regulatory compliance, and high availability over unstable networks.

## Key Elements
- **Patients & Clinicians**: External users accessing the platform via web and mobile applications.
- **Cross-Border Telehealth Platform**: Main software system deployed on GCP across `europe-west3` (EU) and `us-central1` (US).
- **Identity Providers (IdP)**: External OAuth2/OIDC systems for regional user authentication.
- **Payment Gateway**: External service (e.g., Stripe) for processing consultation payments.
- **External Pharmacy Systems**: National EU e-prescription gateways and US pharmacy networks.
- **AI Symptom Checker**: Integrated AI engine for urgency recommendations with strict version logging.

## Relationships
- Patients/Clinicians -> Cross-Border Telehealth Platform via HTTPS and WebRTC (Video consultations).
- Cross-Border Telehealth Platform -> Identity Providers via HTTPS (OIDC authentication).
- Cross-Border Telehealth Platform -> Payment Gateway via HTTPS/REST (Billing).
- Cross-Border Telehealth Platform -> External Pharmacy Systems via HTTPS (HL7 FHIR for US, national standards for EU).
- Cross-Border Telehealth Platform -> AI Symptom Checker via gRPC/HTTPS.

## Technology Stack
- **Google Cloud Platform (GCP)**: Chosen for robust regional deployment capabilities (`europe-west3`, `us-central1`).
- **WebRTC**: Ensures real-time video consultations, supporting degraded bandwidth modes below 300 kbit/s.
- **HL7 FHIR & REST**: Enables healthcare interoperability and secure pharmacy integrations in the US and EU.
- **OAuth2/OIDC**: Secures authentication across regional boundaries.

## Rationale
This architecture enforces strict regional data residency (EU data in `europe-west3`, US data in `us-central1`) to meet GDPR and HIPAA requirements. It maintains high availability and traceability for medical-grade AI outputs while supporting regional interoperability standards.