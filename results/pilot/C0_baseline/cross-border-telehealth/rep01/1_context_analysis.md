## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and resilient low-bandwidth connectivity.

## Key Elements
- **Actors:** Patients, Licensed Clinicians, External Pharmacies, National E-Prescription Gateways, Regional Identity Providers.
- **Containers:** Regional API Gateways, WebRTC Media Servers, AI Symptom Checker Service, Consent Management Service, Regional Databases.
- **Infrastructure:** GCP `europe-west3` and `us-central1` regions, Cloud KMS, Regional Load Balancers, Kubernetes Clusters.

## Relationships
- Patients/Clinicians to Regional API Gateways via HTTPS/WebRTC for UI interactions and video consultations.
- Regional API Gateways to External Pharmacies/Gateways via TLS-encrypted REST and HL7 FHIR APIs for e-prescriptions.
- Services to Regional Databases via encrypted connections with zero cross-border database peering.
- Platform to AI inference endpoints via gRPC over TLS for traceable triage recommendations.

## Technology Stack
- **Cloud Provider:** Google Cloud Platform (GCP) for isolated regional deployments.
- **Communication Protocols:** WebRTC with adaptive TURN/STUN relays and fallback codecs for video/audio under 300 kbit/s; gRPC over TLS for AI inference.
- **Interoperability Standards:** HL7 FHIR for US data; national e-prescription standards for EU.
- **Security & Encryption:** OAuth 2.0 with OIDC, mutual TLS (mTLS), and Cloud KMS with regional keys.
- **Infrastructure & Policy:** Terraform/Pulumi, ArgoCD, and OPA Gatekeeper for compliance enforcement.

## Rationale
This architecture guarantees GDPR and HIPAA compliance by physically isolating EU and US data within their respective GCP regions using strict cryptographic barriers and policy controls. It ensures high availability and accountability for rural users and medical devices through low-bandwidth WebRTC optimizations and cryptographically signed audit logs.