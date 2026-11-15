## Overview
[A secure, multi-region cross-border telehealth platform offering video consultations, e-prescriptions, and an AI symptom checker for EU and US patients on Google Cloud Platform (GCP). It enforces strict GDPR and HIPAA compliance, regional data residency, and MDR traceability while supporting users with unstable rural internet connections.]

## Key Elements
* **People & External Systems**: Patients, Licensed Clinicians, EU Telehealth System, US Telehealth System, Global Management Plane, National E-Prescription Gateways (EU), HL7 FHIR Interoperability Services (US), Regional IAM Services, Local EU/US Pharmacies.
* **Containers (GCP GKE europe-west3, us-central1)**: API Gateway (Cloud Endpoints / Envoy), Video Consultation Service (WebRTC SFU via LiveKit), AI Symptom Checker (Python / FastAPI), Interoperability Adapter (Node.js), Consent Management Service (Go / gRPC), Data Storage (Cloud SQL PostgreSQL + Cloud Storage).
* **AI Symptom Checker Components**: Symptom API Controller, PHI Sanitization Middleware, Clinical NLP Pipeline (spaCy / Hugging Face), Triage Inference Engine (PyTorch / Triton Inference Server), Audit & Traceability Logger, Istio Service Mesh Circuit Breaker.

## Relationships
* API Gateway -> Symptom API Controller: Routes authenticated ingress requests [mTLS / HTTPS].
* Symptom API Controller -> Consent Management Service: Synchronously validates user consent [gRPC].
* Symptom API Controller -> Clinical NLP Pipeline -> Triage Inference Engine: Internal data flow for tokenization and urgency classification.
* Triage Inference Engine -> Audit & Traceability Logger: Emits signed audit records [In-memory queue].
* Audit & Traceability Logger -> Data Storage: Persists immutable logs regionally [gRPC / SQL with CMEK].

## Technology Stack
* **Cloud Infrastructure**: GCP (regions `europe-west3` and `us-central1`) for isolated regional data residency.
* **Orchestration & Mesh**: GKE with Istio Service Mesh for traffic management, circuit breaking, and mTLS.
* **AI / ML Runtime**: PyTorch, Triton Inference Server, and spaCy/Hugging Face Transformers for NLP and triage inference.
* **Security & Auditing**: Cosign for container image signing, Google Cloud KMS with regionally isolated CMEK, and WORM-configured Cloud Storage for audit logging.
* **APIs & Protocols**: gRPC and HTTPS for internal/external communication; WebRTC (LiveKit) for video consultations.

## Rationale
[This architecture enforces regional data boundaries and regulatory compliance (GDPR, HIPAA, EU MDR) through isolated GCP regions and immutable audit logging. It ensures high availability for low-bandwidth rural users via Istio circuit breakers and localized GPU-accelerated triage inference.]