## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency, HIPAA, GDPR, and EU MDR compliance.

## Key Elements
* **Patients & Clinicians:** End-users accessing the platform via Web/Mobile clients.
* **Cross-Border Telehealth Platform:** Core GCP-hosted system split across `europe-west3` and `us-central1`.
* **AI Symptom Checker Engine:** Versioned AI/ML model for care urgency recommendations.
* **National Pharmacies (EU) & US Pharmacies:** External fulfillment systems via interoperability gateways.
* **Identity Providers:** External OAuth2/OIDC services for authentication.

## Relationships
* **Patients/Clinicians $\rightarrow$ Telehealth Platform:** HTTPS and WebRTC (with DTLS-SRTP) for consultations and symptom checking.
* **Telehealth Platform $\rightarrow$ AI Symptom Checker:** HTTPS APIs with immutable version pinning and input/output logging.
* **Telehealth Platform $\rightarrow$ Pharmacies:** Secure APIs utilizing mTLS, HL7 FHIR (US), and national standards (EU) for e-prescriptions.
* **Platform Services $\rightarrow$ GCP KMS:** Customer-Managed Encryption Keys (CMEK) with separate key rings per region.

## Technology Stack
* **Cloud Provider:** Google Cloud Platform (GCP) (`europe-west3` and `us-central1`) for jurisdictional data isolation.
* **Deployment & CI/CD:** GCP Cloud Build for region-isolated pipelines.
* **Observability:** GCP Cloud Monitoring and Logging with pre-ingestion PII/PHI masking and WORM storage.
* **Networking & Streaming:** WebRTC SFUs with adaptive bitrate for low-bandwidth rural connections.
* **Security & Auth:** OAuth2/OIDC, TLS 1.3, mTLS, and GCP KMS (CMEK).

## Rationale
This multi-region GCP architecture guarantees that EU health data remains in the EU and US data in the US, fulfilling GDPR and HIPAA constraints. Region-isolated deployments, rigorous cryptographic controls, and immutable AI logging ensure full compliance with EU MDR while supporting resilient, low-bandwidth consultations.