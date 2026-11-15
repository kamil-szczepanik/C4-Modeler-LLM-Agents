## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency while ensuring rural accessibility and regulatory compliance (GDPR/HIPAA).

## Key Elements
- Patients and Licensed Clinicians (Users)
- External Identity Providers (IdP) and Local Pharmacies
- Regional GKE Clusters (`europe-west3`, `us-central1`)
- Node.js/GraphQL Backend-for-Frontend (BFF) Container
- Mediasoup WebRTC SFU Media Container
- AI Triage Service & Consent Manager Containers
- E-Prescription Adapter Container
- Istio Service Mesh & API Gateway

## Relationships
- Patients/Clinicians to API Gateway via HTTPS (TLS 1.3)
- BFF to Regional Microservices via gRPC over mTLS (Istio)
- E-Prescription Adapter to US Pharmacies via HL7 FHIR and to EU Pharmacies via national standards (REST/SOAP)
- WebRTC SFU to Clients via DTLS-SRTP
- Containers to Regional WORM Storage via HTTPS

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing `europe-west3` and `us-central1` for strict data residency.
- Google Kubernetes Engine (GKE): Container orchestration for regional microservices with CIS benchmark hardening and non-root policies.
- Istio Service Mesh: Manages mTLS, traffic splitting, and VPC Service Controls for network isolation.
- Node.js & GraphQL: Powers the regional Backend-for-Frontend (BFF) to abstract regional data formats.
- Mediasoup: WebRTC SFU container for video/audio streaming with sub-300 kbit/s bandwidth degradation.
- OpenTelemetry & Prometheus: Observability stack for distributed tracing, metrics, and automated SLO monitoring.

## Rationale
Regional GKE deployments combined with Istio service mesh and VPC Service Controls strictly satisfy GDPR and HIPAA data residency mandates without relying solely on application logic. Containerizing Mediasoup SFU with dynamic bitrate reduction guarantees resilient video and audio consultations for rural patients on unstable connections.