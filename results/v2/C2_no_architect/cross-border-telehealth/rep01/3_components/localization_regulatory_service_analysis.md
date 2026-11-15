## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The Localization & Regulatory Service enforces regional data residency, granular consent management, and audit traceability.]

## Key Elements
- Patients (EU & US)
- Compliance & QA Officers
- Localization & Regulatory Service (Container)
- Regional GKE Clusters (europe-west3, us-central1)
- Regional Read-Only Database Replicas
- Cloud Pub/Sub & Cloud Run Background Workers
- Cloud KMS & WORM Cloud Storage

## Relationships
- Patients & Officers -> Localization & Regulatory Service [HTTPS/TLS]
- Localization & Regulatory Service -> Regional GKE Clusters [mTLS via Istio]
- Localization & Regulatory Service -> Regional Read-Only Database Replicas [SQL/TLS]
- Localization & Regulatory Service -> Cloud Pub/Sub [Async Messaging]
- Localization & Regulatory Service -> WORM Cloud Storage [Encrypted Storage]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider for infrastructure.
- Kubernetes & Istio: Container orchestration and mTLS zero-trust service mesh.
- Cloud KMS: Envelope encryption and per-patient crypto-shredding.
- Cloud Pub/Sub & Cloud Run: Asynchronous processing for compliance exports.
- Cloud Storage (Bucket Lock): Immutable WORM storage for audit logs.

## Rationale
[Strict regional isolation with VPC Service Controls and independent databases guarantees GDPR and HIPAA compliance. Asynchronous pipelines and read-only replicas protect core transactional availability for patients.]