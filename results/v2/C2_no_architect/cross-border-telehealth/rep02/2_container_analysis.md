## Overview
[Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients on GCP.]
[Enforces strict regional data residency, HIPAA/GDPR compliance, and AI traceability while supporting unstable rural internet connections.]

## Key Elements
* Patients and Licensed Clinicians (Web/Mobile Clients)
* API Gateway Container with OPA (Open Policy Agent)
* Consent & Identity Management Container
* Video Streaming Container
* AI Symptom Checker Container
* Local Pharmacy Integration Containers
* Regional WORM Storage Buckets
* GCP GKE Clusters (`europe-west3`, `us-central1`)

## Relationships
* Web/Mobile Clients to API Gateway Container via HTTPS/WSS
* API Gateway to regional containers via Istio Service Mesh (mTLS)
* Video Streaming Container to Clients via WebRTC (adaptive bitrate)
* AI Symptom Checker to regional WORM Storage via HTTPS (TLS 1.3)
* Pharmacy Integration Containers to Local Pharmacy Networks via HL7 FHIR and national EU e-prescription standards

## Technology Stack
* GCP (`europe-west3`, `us-central1`): Target cloud providing regional isolation and local Cloud KMS envelope encryption.
* GKE with Istio Service Mesh: Container orchestration enforcing mTLS and zero cross-region traffic by default.
* Open Policy Agent (OPA): Dynamic, policy-based access control embedded in the API Gateway for granular consent management.
* WebRTC: Real-time video protocol with Prometheus/Grafana monitoring to support sub-300 kbit/s degraded modes.
* ArgoCD: GitOps deployment engine with region-locked pipelines ensuring strict data residency.
* Cloud KMS & WORM Storage: Cryptographically signed audit logging for AI outputs satisfying EU MDR traceability.

## Rationale
[Regional container isolation and region-locked GitOps pipelines guarantee strict compliance with GDPR, HIPAA, and data residency mandates.]
[Decoupled architecture with Istio mTLS, OPA authorization, and WORM storage ensures clinical safety, regulatory auditability, and reliable video streaming for rural patients.]