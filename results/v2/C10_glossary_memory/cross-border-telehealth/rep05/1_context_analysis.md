## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency while ensuring regulatory compliance, high availability, and traceability.

## Key Elements
- **Users**: Patients, Licensed Clinicians, Compliance Officers / Auditors.
- **Software System**: Cross-Border Telehealth Platform.
- **Containers**: Regional Kubernetes Clusters, WebRTC Media Servers (LiveKit/Janus), AI Inference Microservices, Consent Management Service.
- **External Systems**: EU National E-Prescription Gateways, US Pharmacy Networks (Surescripts), Identity Providers (eIDAS / OAuth2/OIDC), Regional Payment & Insurance Gateways.

## Relationships
- **Patients & Clinicians** -> **Platform**: HTTPS/WebRTC (DTLS-SRTP, adaptive bitrate for connections <300 kbit/s).
- **Platform** -> **EU/US Pharmacy Systems & Gateways**: secure APIs via mTLS and HL7 FHIR / REST.
- **Platform** -> **Regional Payment Gateways**: HTTPS/REST with tokenization via GCP VPC Service Controls.
- **Auditors** -> **Platform**: HTTPS (Read-Only Audit Logs via IAM roles).

## Technology Stack
- **Cloud Provider**: GCP (`europe-west3` Frankfurt, `us-central1` Iowa) for strict data residency.
- **Orchestration**: Kubernetes (GKE) with regionally isolated clusters and policy-as-code (OPA/Gatekeeper).
- **Video Streaming**: LiveKit or Janus for low-bandwidth WebRTC media handling.
- **Security & Identity**: OIDC/OAuth2, GCP Secret Manager, Cloud Audit Logs, and Customer-Managed Encryption Keys (CMEK).

## Rationale
This multi-region GCP architecture guarantees compliance with GDPR and HIPAA by physically separating EU and US data planes. Isolated regional components, tokenized integrations, and robust traceability mechanisms successfully meet strict EU MDR and security constraints.