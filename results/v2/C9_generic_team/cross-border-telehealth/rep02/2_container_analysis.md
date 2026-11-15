## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an MDR-compliant AI symptom checker for patients in the EU and US. It enforces strict regional data residency using isolated cloud infrastructure in GCP.

## Key Elements
- **Users**: Patients and Licensed Clinicians
- **Client Edge**: Offline Sync/Queue Container, API Gateway
- **Regional Core Containers (europe-west3, us-central1)**: Data Localization Router, Session Management, Anti-Corruption Layer (ACL), Inference Service, Asynchronous Task Worker, Cryptographic Vault
- **External Systems**: EU/US Pharmacies, AI Model Registry, External IdP, Payment Gateways

## Relationships
- Patients/Clinicians to API Gateway via HTTPS/WebSockets for video and data
- Inference Service to AI Model Registry via gRPC for model versioning
- ACL Container to Pharmacies/Gateways via REST/HL7 FHIR and national standards
- Data Localization Router to Regional Databases via TLS for isolated persistence

## Technology Stack
- **Cloud Provider**: GCP (`europe-west3` for EU, `us-central1` for US) to enforce data residency constraints.
- **Interoperability**: HL7 FHIR (US) and national e-prescription standards (EU) managed via an ACL container.
- **AI & Traceability**: Isolated Inference Service with immutable audit logging for MDR compliance.
- **Resilience**: Client-side offline sync queues and asynchronous task workers to handle unstable rural connections.

## Rationale
Isolated regional container clusters and localized cryptographic vaults guarantee GDPR and HIPAA compliance. Decoupled asynchronous workers and offline sync queues ensure high availability and graceful degradation for unstable rural networks.