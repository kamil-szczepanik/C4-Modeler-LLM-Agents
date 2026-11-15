## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency and compliance via GCP.

## Key Elements
- Patients (EU and US) and Licensed Clinicians
- Web/Mobile Frontend App (React/Flutter)
- API Gateway / Core Backend (Go/Node.js)
- AI Symptom Checker (Python/FastAPI)
- Interoperability Adapter (Plugin architecture)
- Video Session Manager (WebRTC SFU)
- External Systems (Global IdP, EU E-Prescription Gateways, US Pharmacy Networks, Video Relay)

## Relationships
- Clients to API Gateway via HTTPS/gRPC
- Interoperability Adapter to EU gateways and US pharmacies via REST/SOAP (HL7 FHIR / national standards)
- Video Session Manager to Web/Mobile Frontend via WebRTC
- Inter-container traffic secured via mTLS (SPIFFE/SPIRE on GKE)

## Technology Stack
- Cloud Provider: Google Cloud Platform (`europe-west3` and `us-central1` regions)
- Encryption: GCP Cloud KMS (CMEK, AES-256 at rest, TLS 1.3 in transit)
- Security: OAuth 2.0 / OIDC, GCP Cloud HSM for cryptographic AI output signing, GCP Secret Manager
- Observability: Prometheus/Grafana, Fluentbit sidecars streaming to GCP BigQuery

## Rationale
Regional container clusters on GCP strictly isolate EU and US health data to satisfy GDPR and HIPAA requirements. The microservices architecture with regional SFUs and pluggable interoperability adapters ensures high availability under unstable rural network conditions and rapid scaling across diverse healthcare jurisdictions.