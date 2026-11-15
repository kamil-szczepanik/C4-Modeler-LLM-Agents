## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, GDPR and HIPAA compliance, and reliable performance over unstable connections.

## Key Elements
- **Patients & Clinicians:** End-users accessing telehealth services via web or mobile clients.
- **API Gateway & Data Localization Router:** GCP-hosted edge entry point utilizing geo-DNS and TLS SNI parsing.
- **Regional Databases:** GCP-managed databases deployed in `europe-west3` and `us-central1`.
- **Inference Service & ACL:** Python/gRPC AI symptom checker and anti-corruption layer for HL7 FHIR and EU standards.
- **Offline Sync Container:** Local storage and queue manager for low-bandwidth resilience.

## Relationships
- **Patients/Clinicians -> API Gateway:** Secure access via HTTPS and WebSockets.
- **API Gateway -> Data Localization Router:** Requests intercepted via geo-DNS and stateless middleware.
- **Data Localization Router -> Regional Databases:** Enforces strict data residency and persistence using TLS.
- **Data Localization Router -> Inference Service:** Routes anonymized inputs to the AI symptom checker via gRPC.

## Technology Stack
- **Cloud Infrastructure:** Google Cloud Platform (GCP) across `europe-west3` and `us-central1` for regional compliance.
- **Routing & Proxy:** Geo-DNS with TLS SNI parsing and stateless interceptor middleware for fail-closed security.
- **Resilience & Audit:** Local encrypted write-ahead disk logs and circuit breakers for offline sync and zero-loss accountability.
- **Interoperability:** HL7 FHIR for US data structures and national standards for EU e-prescriptions.

## Rationale
Geo-DNS routing and a stateless interceptor pattern ensure strict regional data residency required by GDPR and HIPAA. Local write-ahead buffers, strict idempotency keys, and circuit breakers guarantee high availability and audit traceability despite rural, unstable internet connections.