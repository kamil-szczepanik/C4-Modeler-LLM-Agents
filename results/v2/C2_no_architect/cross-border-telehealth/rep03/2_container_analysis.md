## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. It ensures strict regional data residency, regulatory compliance, and resilience for unstable rural connections.

## Key Elements
* **Patients (EU/US)**: End-users accessing care via a PWA container.
* **Licensed Clinicians**: Healthcare providers using the Clinical Workspace container.
* **Platform Administrators / Compliance Officers**: Users managing audits, credentials, and compliance.
* **Patient Portal Container (PWA)**: Edge interface supporting offline resilience and async workflows.
* **Clinical Workspace Container**: Interface managing video consultations and e-prescription routing.
* **Consent & Compliance Container**: Microservice enforcing granular consent and immutable AI audit logging.
* **Vertex AI**: External system providing AI symptom-checker recommendations.
* **Local Pharmacies**: External regional systems receiving e-prescriptions.

## Relationships
* **Patients & Clinicians to PWA/Clinical Workspace**: HTTPS, WebRTC for video consultations, and OAuth2/OIDC via Identity-Aware Proxy (IAP).
* **Containers to Vertex AI**: gRPC/REST over mTLS for symptom-checker inferences.
* **Clinical Workspace to Local Pharmacies**: REST APIs using HL7 FHIR (US) and national e-prescription standards (EU).
* **Internal Microservices**: mTLS inside GKE clusters via Istio service mesh and OAuth2 token validation at the API Gateway.

## Technology Stack
* **Cloud Platform (GCP)**: Isolated GKE clusters in `europe-west3` and `us-central1` to enforce strict data residency.
* **Video & Edge**: LiveKit WebRTC SFU with adaptive bitrate transcoding for low-bandwidth connections (<300 kbit/s).
* **Storage & Caching**: Regionally isolated BigQuery with WORM policies for AI audit logs, and regional Redis for PWA sync.
* **Security & Compliance**: Cloud KMS with region-specific CMEK, Google Cloud Secret Manager with Workload Identity, Binary Authorization, and Istio service mesh.
* **Observability**: OpenTelemetry collectors for tracing cross-border workflows and Argo Rollouts for deployments.

## Rationale
The architecture strictly segregates regional data into isolated GCP regions to satisfy EU GDPR and US HIPAA mandates. Additionally, edge-resilient PWA containers, adaptive WebRTC streaming, and WORM-backed audit logging fulfill the availability, offline resilience, and EU MDR traceability requirements.