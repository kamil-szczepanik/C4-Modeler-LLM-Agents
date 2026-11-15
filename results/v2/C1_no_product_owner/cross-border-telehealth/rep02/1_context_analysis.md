## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency while ensuring regulatory compliance, high availability, and traceability.

## Key Elements
- Patients and Licensed Clinicians (External Actors)
- Regional Platforms (`europe-west3` and `us-central1` on GCP)
- AI Symptom Checker Service with versioned models
- Regional Identity Providers (eIDAS-compliant for EU, OAuth/OIDC for US)
- National e-Prescription Gateways (EU) and Pharmacies/EHRs (US)
- Adaptive WebRTC Media Gateways

## Relationships
- Patients/Clinicians interact with regional GCP platforms via HTTPS and WebSockets
- Regional platforms communicate with e-prescription networks using secure REST and HL7 FHIR over TLS 1.3/mTLS
- Global Anycast DNS/Load Balancing routes traffic to isolated regional deployments at the edge
- Cross-region administrative access requires explicit, consent-scoped ABAC evaluation

## Technology Stack
- Google Cloud Platform (GCP) with regions `europe-west3` and `us-central1` for data residency
- TLS 1.3 and mTLS for secure data in transit
- Cloud KMS with region-specific customer-managed encryption keys (CMEK) for data at rest
- OAuth 2.0, OIDC, and regional IdPs for authentication
- HL7 FHIR and national standards for interoperability
- Cloud Logging, BigQuery, and HSM-backed cryptographic signing for EU MDR compliance and immutable audit trails

## Rationale
The isolated dual-region GCP architecture guarantees compliance with GDPR and HIPAA by preventing unconsented cross-border data transit. Furthermore, regional HSM signing, adaptive media gateways, and local active-active multi-zone topologies satisfy strict EU MDR traceability and rural low-bandwidth availability constraints.