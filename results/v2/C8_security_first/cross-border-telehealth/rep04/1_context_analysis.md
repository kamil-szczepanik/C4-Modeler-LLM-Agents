## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and high availability even for rural users.

## Key Elements
* **Users:** Patients (EU/US), Licensed Clinicians, and Regulatory Auditors.
* **Core System:** Cross-Border Telehealth Platform.
* **Containers/Services:** Regional API Gateways, WebRTC/SFU Media Nodes, AI Symptom Checker, OpenTelemetry Collectors, and GKE Regional Clusters.
* **External Systems:** EU National E-Prescription Gateways, US Healthcare Networks/Pharmacies, Federated Identity Providers (IdP), and AI Model Providers.

## Relationships
* **Patients & Clinicians -> API Gateway:** HTTPS / TLS 1.3 for application traffic and consent management.
* **Patients & Clinicians -> SFU Media Nodes:** WebRTC / DTLS-SRTP for video consultations (<300 kbit/s degraded mode).
* **API Gateway -> EU National E-Prescription Gateways:** REST / SOAP APIs for national e-prescriptions.
* **API Gateway -> US Healthcare Networks:** HL7 FHIR APIs over HTTPS.
* **API Gateway -> IdP:** OAuth 2.0 / OIDC for federated authentication.

## Technology Stack
* **Cloud Provider:** Google Cloud Platform (GCP) across `europe-west3` and `us-central1` for geographical isolation.
* **Storage & Security:** Cloud KMS with regional Customer-Managed Encryption Keys (CMEK) and GCP Organization Policies for GDPR/HIPAA compliance.
* **Networking & Media:** WebRTC, DTLS-SRTP, and Selective Forwarding Units (SFUs) for encrypted, low-bandwidth video.
* **Interoperability & Observability:** HL7 FHIR, REST/SOAP, OpenTelemetry, and Cloud Audit Logs for traceability and monitoring.

## Rationale
This architecture uses multi-region GCP deployment to strictly enforce EU and US data residency mandates while satisfying GDPR and HIPAA requirements. Regional SFUs, API gateways, and OpenTelemetry ensure resilient, observable care delivery for rural patients with unstable connections.