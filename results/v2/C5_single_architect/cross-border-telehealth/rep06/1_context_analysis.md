## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict regional data residency, regulatory compliance, and low-bandwidth availability.

## Key Elements
* **Patients & Clinicians**: External users interacting with the platform.
* **Cross-Border Telehealth Platform**: Core system deployed across GCP `europe-west3` and `us-central1`.
* **National Pharmacy Networks (EU) & US Pharmacy Systems**: External systems for e-prescriptions.
* **AI Model Provider / LLM API**: External service for symptom checking.
* **Third-Party Identity Providers & Payment Gateways**: External systems for authentication and billing.

## Relationships
* **Patient/Clinician -> Platform**: HTTPS and WebSockets with adaptive bitrate streaming for low bandwidth.
* **Platform -> AI Model Provider**: Secure HTTPS REST APIs with immutable logging.
* **Platform -> Pharmacy Systems**: TLS-encrypted REST and HL7 FHIR APIs segregated by region.
* **Platform -> Payment Gateways**: HTTPS webhooks for cross-border billing.

## Technology Stack
* **GCP (`europe-west3`, `us-central1`)**: Cloud provider chosen for regional data residency enforcement.
* **WebSockets / HTTPS**: Protocols for real-time video consultations and API communication.
* **HL7 FHIR & National EU Standards**: Interoperability standards for e-prescriptions.
* **Stripe / Adyen**: Payment processing integration via webhooks.

## Rationale
This regionally isolated GCP architecture strictly enforces GDPR and HIPAA data residency constraints while supporting low-bandwidth video streaming and immutable audit logging for AI diagnostics.