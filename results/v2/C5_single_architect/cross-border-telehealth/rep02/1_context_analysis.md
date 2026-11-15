## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and AI symptom checks for patients in the EU and US. It guarantees strict regional data residency while ensuring regulatory compliance under GDPR, HIPAA, and EU MDR.

## Key Elements
- **Patients (EU/US)**: End-users accessing telehealth services via web or mobile applications.
- **Licensed Clinicians**: Healthcare providers conducting video consultations and issuing prescriptions.
- **Cross-Border Telehealth Platform**: Core system deployed in GCP (`europe-west3` and `us-central1`).
- **AI Symptom Checker Service**: Isolated cognitive service providing urgency recommendations.
- **National e-Prescription Gateways (EU) & Pharmacy Systems (US)**: External systems for dispatching prescriptions.
- **Third-party Video Infrastructure**: WebRTC-based service handling real-time consultations.

## Relationships
- **Patients & Clinicians -> Cross-Border Telehealth Platform**: HTTPS (Web/Mobile Apps) with TLS encryption.
- **Cross-Border Telehealth Platform -> Third-party Video Infrastructure**: WebRTC supporting degraded connections down to 300 kbit/s.
- **Cross-Border Telehealth Platform -> AI Symptom Checker Service**: gRPC over TLS for inference requests with immutable request logging.
- **Cross-Border Telehealth Platform -> National e-Prescription Gateways (EU) / Pharmacy Systems (US)**: Secure API gateways using TLS and mTLS (HL7 FHIR for US, national standards for EU).

## Technology Stack
- **Google Cloud Platform (GCP)**: Selected for regional deployment (`europe-west3` and `us-central1`) to enforce data residency constraints.
- **WebRTC**: Used for video consultations to guarantee availability and performance on unstable rural connections.
- **gRPC over TLS**: Implemented for low-latency communication with the AI Symptom Checker Service.
- **HL7 FHIR & National Standards**: Utilized for interoperability with US and EU pharmacy systems.
- **TLS/mTLS**: Enforced across all external and cross-boundary integrations to ensure GDPR and HIPAA compliance.

## Rationale
This architecture enforces geographical data separation between GCP regions to meet strict GDPR and HIPAA mandates. It utilizes adaptive streaming and robust interoperability standards to support vulnerable rural users and diverse regional healthcare systems.