## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, regulatory compliance, and high availability for unstable connections.

## Key Elements
- **Patients (EU & US):** Access video consultations and manage consent.
- **Licensed Clinicians:** Deliver care and review patient histories.
- **Cross-Border Telehealth Platform:** Core system deployed in `europe-west3` and `us-central1`.
- **EU National E-Prescription Gateways & US Pharmacy Networks:** External prescription fulfillment systems.
- **AI Inference Service:** External system providing urgency recommendations.

## Relationships
- **Patients & Clinicians -> Platform:** HTTPS and WebRTC (TLS 1.3 / DTLS-SRTP) for video and data management.
- **Platform -> EU/US Pharmacies:** REST/FHIR and national standards over HTTPS/mTLS.
- **Platform -> AI Inference Service:** gRPC over TLS 1.3 with sidecar interception for audit logs.

## Technology Stack
- **Cloud Provider:** GCP (`europe-west3` and `us-central1`) for regional data isolation.
- **Infrastructure:** Terraform and ArgoCD for multi-region GitOps and immutable deployments.
- **Media Streaming:** WebRTC media servers (SFUs) with real-time telemetry for bitrate degradation.
- **Security & Encryption:** GCP Cloud KMS with regional CMEK, OAuth 2.0 / OIDC, and JWTs.
- **Interoperability:** HL7 FHIR (US) and national standards (EU).

## Rationale
Isolated regional deployments guarantee compliance with GDPR, HIPAA, and EU MDR data residency mandates. Edge-terminated media streaming and sidecar-enforced audit logging ensure high availability for rural users and strict accountability for AI medical devices.