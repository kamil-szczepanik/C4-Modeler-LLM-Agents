## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and AI symptom checking for patients across the EU and US. It enforces strict regional data residency while ensuring regulatory compliance, interoperability, and low-bandwidth availability.

## Key Elements
* **Patients & Clinicians:** End-users accessing the platform via Mobile and Web Applications.
* **EU Platform Instance:** GCP `europe-west3` container hosting European patient services, consent management, and regional AI symptom checker.
* **US Platform Instance:** GCP `us-central1` container hosting US patient services, consent management, and regional AI symptom checker.
* **AI Symptom Checker:** Microservice component capturing inputs, outputs, and model versions for MDR traceability.
* **National E-Prescription Networks (EU):** External systems utilizing country-specific standards (e.g., eHDSI/NCPeH).
* **Pharmacy Systems (US):** External systems utilizing HL7 FHIR.
* **Identity Providers & Gateways:** External OAuth2/OIDC IdPs, Payment Gateways, and SMS Notification Gateways.

## Relationships
* **Patients/Clinicians to Regional Platforms:** HTTPS (REST) for application logic and WebRTC for video consultations.
* **Regional Platforms to AI Symptom Checker:** Internal gRPC for urgency recommendations and telemetry logging.
* **US Platform to Pharmacy Systems:** HL7 FHIR over HTTPS (REST).
* **EU Platform to E-Prescription Networks:** National standards (e.g., eHDSI/NCPeH) over Mutual TLS (mTLS).
* **Regional Platforms to IdPs & Gateways:** OAuth2/OIDC, HTTPS REST, and SMPP/APNs for notifications.

## Technology Stack
* **Cloud Provider:** Google Cloud Platform (GCP) (`europe-west3` and `us-central1`) for isolated regional data residency.
* **Communication Protocols:** WebRTC with adaptive bitrate codecs for low-bandwidth video (under 300 kbit/s).
* **Integration Protocols:** HL7 FHIR (US) and mTLS/REST (EU) for secure e-prescriptions.
* **Internal APIs:** gRPC for low-latency, strongly typed microservice communication.

## Rationale
Dual regional deployments on GCP completely satisfy strict GDPR, HIPAA, and data residency constraints without cross-border leaks. Using WebRTC with adaptive streaming and localized AI inference guarantees high availability and regulatory compliance for international telehealth operations.