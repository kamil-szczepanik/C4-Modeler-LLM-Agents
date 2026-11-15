## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. It ensures strict regional data residency and regulatory compliance across Google Cloud Platform regions.

## Key Elements
- Patients and Clinicians (EU/US users interacting via HTTPS and WebSockets)
- Compliance Officer (Auditor managing regional consent and AI traceability logs)
- Cross-Border Telehealth Platform (Core system spanning GCP `europe-west3` and `us-central1`)
- External Systems: National E-Prescription Gateways (EU), US Pharmacy Networks, Identity Providers (IdP)

## Relationships
- Patients/Clinicians interact with the Platform via HTTPS and WebRTC (DTLS-SRTP) for video consultations
- Platform connects to National E-Prescription Gateways (EU) via REST/SOAP and US Pharmacy Networks via HL7 FHIR over HTTPS
- Platform authenticates users via Identity Providers using OAuth 2.0 / OIDC
- Compliance Officer accesses audit logs and regional consent data via HTTPS

## Technology Stack
- Cloud Provider: Google Cloud Platform (`europe-west3` and `us-central1`) with VPC Service Controls for data residency
- Compute & Deployment: Fully isolated regional cluster instances managed via ArgoCD GitOps
- Security & Encryption: Cloud KMS with CMEK, TLS 1.3, mTLS, Cloud Armor WAF, and WORM storage (Cloud Storage Object Retention)
- Messaging & Integration: GCP Pub/Sub with dead-letter routing for asynchronous tasks and e-prescriptions
- Video & Observability: WebRTC with adaptive media fallbacks, Cloud Monitoring, and Cloud Trace

## Rationale
Isolated regional deployments in GCP enforce strict GDPR and HIPAA data residency constraints while maintaining high availability. Decoupled asynchronous messaging and adaptive WebRTC media streams guarantee reliable operations and fallback modes for rural patients with unstable connections.