## Overview
- Cross-border telehealth platform delivering video consultations, e-prescriptions, and an AI symptom checker across the EU and US.
- Built for strict regional data residency, HIPAA/GDPR compliance, and resilient operations over unstable rural internet connections.

## Key Elements
- Patients, Licensed Clinicians, Platform Administrators, Regional Health Authorities/Auditors
- API Gateway Container (GCP GKE, OPA, Istio)
- AI Symptom Checker Container (GCP GKE, Confidential VMs with AMD SEV-SNP, Cloud KMS)
- Consent & Identity Management Container
- Video Streaming Container (WebRTC)
- Regional WORM Storage Buckets (GCP Cloud Storage WORM)
- GCP Pub/Sub (Regional event queues)

## Relationships
- API Gateway Container -> AI Symptom Checker Container: Routes sanitized requests [Istio Service Mesh mTLS, Server-Sent Events/SSE]
- AI Symptom Checker Container -> Regional WORM Storage Buckets: Persists immutable audit logs and versioned inputs [HTTPS TLS 1.3]
- API Gateway Container -> Consent & Identity Management Container: Validates explicit patient consent [Open Policy Agent / OPA]

## Technology Stack
- Google Cloud Platform (GCP): Deployed in `europe-west3` and `us-central1` for strict data residency.
- GCP GKE & Istio: Container orchestration and traffic management with mTLS.
- Confidential VMs (AMD SEV-SNP): Protects in-memory patient health data and AI model weights.
- GCP Pub/Sub: Asynchronous queuing for reliable processing over unstable links.
- GCP Binary Authorization: Ensures cryptographic model weight verification.

## Rationale
- Decouples AI processing via asynchronous queuing and SSE to maintain triage availability on sub-300 kbit/s rural connections.
- Employs Confidential Computing and WORM storage to satisfy EU MDR traceability and cross-border privacy mandates.