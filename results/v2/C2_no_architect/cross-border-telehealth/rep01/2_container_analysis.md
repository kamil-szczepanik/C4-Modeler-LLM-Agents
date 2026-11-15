## Overview
Cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. Enforces strict regional data residency and regulatory compliance.

## Key Elements
- Patients (EU & US), Licensed Clinicians, Compliance & QA Officers
- Regional GKE Clusters (`europe-west3`, `us-central1`)
- Localization & Regulatory Service Container
- WebRTC Media Server Containers (SFUs)
- AI Symptom Checker Container
- Clinician Dashboard & Handoff Container
- Patient Engagement & Notification Gateway Container
- External Pharmacies (EU & US)

## Relationships
- Patients to WebRTC Media Server via WebRTC/mTLS for video consultations (R-01)
- AI Symptom Checker to Cloud Logging via gRPC for audit logs (R-07)
- Localization & Regulatory Service to Regional Databases via SQL/TLS for consent management (R-04)
- Clinician Dashboard to Notification Gateway via HTTPS/TLS for e-prescription dispatch (R-02)

## Technology Stack
- Google Cloud Platform (`europe-west3`, `us-central1`) for regional cloud infrastructure
- Kubernetes (GKE) with Istio service mesh for container orchestration and mTLS
- Jitsi/Mediasoup SFU for low-bandwidth WebRTC video streaming (R-06)
- GCP VPC Service Controls and Cloud KMS for data residency and CMEK encryption (R-05)
- OpenTelemetry and Prometheus for observability and SLI/SLO tracking

## Rationale
Regional GKE isolation and VPC Service Controls guarantee GDPR and HIPAA compliance while enforcing strict data residency. WebRTC SFU media servers with dynamic throttling ensure high availability and resilient video consultations for rural patients.