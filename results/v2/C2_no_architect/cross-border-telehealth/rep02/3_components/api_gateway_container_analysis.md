## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance (GDPR/HIPAA/MDR), and resilience for rural users via GCP multi-region architecture.

## Key Elements
- Patients & Licensed Clinicians
- Platform Administrators & Regional Health Authorities/Auditors
- Local Pharmacy Networks
- API Gateway Container (GCP GKE, OPA, Istio, WAF)
- Consent & Identity Management Container (GCP GKE, Istio)
- Video Streaming Container (GCP GKE, WebRTC, Prometheus/Grafana)
- AI Symptom Checker Container (GCP GKE, Cloud KMS)
- Local Pharmacy Integration Containers (GCP GKE, HL7 FHIR)
- Regional WORM Storage Buckets (GCP Cloud Storage WORM)

## Relationships
- Patients & Licensed Clinicians -> API Gateway Container: Accesses telehealth services [HTTPS/WSS via TLS 1.3]
- API Gateway Container -> Consent & Identity Management Container: Validates consent and identity [Istio Service Mesh (mTLS)]
- API Gateway Container -> Video Streaming Container: Routes video consultations [Istio Service Mesh (mTLS)]
- API Gateway Container -> AI Symptom Checker Container: Routes symptom analysis requests [Istio Service Mesh (mTLS)]
- API Gateway Container -> Local Pharmacy Integration Containers: Sends e-prescriptions [Istio Service Mesh (mTLS)]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing `europe-west3` and `us-central1` regions.
- Google Kubernetes Engine (GKE): Container orchestration platform for regional deployments.
- Istio: Service mesh managing mTLS, circuit breaking, distributed tracing (OpenTelemetry), and telemetry.
- Open Policy Agent (OPA): Enforces dynamic data residency and purpose-based consent rules at runtime.
- WebRTC: Protocol supporting low-bandwidth video consultations in degraded connection modes.
- HL7 FHIR: Interoperability standard for US pharmacy integrations.
- GCP Secret Manager & Cloud KMS: Manages cryptographic keys and isolated container secrets.

## Rationale
This multi-region architecture enforces strict geographic data residency and regulatory compliance (GDPR/HIPAA) through edge routing, OPA policies, and encrypted regional storage. Istio service mesh integration and low-bandwidth handling ensure high availability and security for rural users.