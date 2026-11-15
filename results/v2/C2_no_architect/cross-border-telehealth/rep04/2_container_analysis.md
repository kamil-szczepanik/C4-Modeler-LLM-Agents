## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, HIPAA/GDPR compliance, and high availability over unstable networks.

## Key Elements
- **Users**: Patients (EU & US), Licensed Clinicians, Compliance Officers, Local Pharmacy Partners.
- **Systems**: External Pharmacies (EU/US).
- **Containers**: API Gateway, Frontend Container, WebRTC SFU (Mediasoup/coturn), AI Symptom Checker Container with Audit Sidecar, Regional GKE Clusters (`europe-west3`, `us-central1`), Cloud WAF.

## Relationships
- Patients & Clinicians to API Gateway via HTTPS/TLS 1.3 and WebRTC over UDP/TCP.
- API Gateway to Regional GKE Containers via Istio Service Mesh using mTLS with SPIFFE IDs.
- AI Symptom Checker to WORM Cloud Storage via gRPC/HTTPS for immutable audit logging.
- Regional Containers to External Pharmacies via HL7 FHIR (US) and national standards (EU).

## Technology Stack
- **Cloud Provider**: Google Cloud Platform (GCP) across `europe-west3` and `us-central1` for strict data residency.
- **Orchestration**: Google Kubernetes Engine (GKE) managed via Anthos/Fleet with distroless container images.
- **Networking & Security**: Istio Service Mesh, Cloud KMS with CMEK, OAuth2/OIDC, and Cloud WAF.
- **Video & Telemetry**: Mediasoup/coturn for WebRTC SFUs; OpenTelemetry for distributed tracing.

## Rationale
Isolated regional GKE deployments with Istio mTLS and regional KMS key rings strictly enforce EU/US data residency and compliance. Mediasoup SFUs, sidecar audit proxies, and robust API validation ensure low-bandwidth video resilience and traceable AI recommendations.