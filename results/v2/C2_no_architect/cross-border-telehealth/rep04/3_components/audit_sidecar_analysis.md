## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The architecture enforces strict regional data residency and regulatory compliance using isolated cloud infrastructure and cryptographically chained audit logging.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Google Cloud Platform (GCP)
- Regional GKE Clusters (`europe-west3`, `us-central1`)
- API Gateway (Istio Service Mesh / Envoy)
- AI Symptom Checker Container (Python, TensorFlow, Distroless)
- Audit Sidecar Container
- Google Cloud Storage with Object Lock (WORM)
- Cloud KMS

## Relationships
- Patients and Clinicians interact with the platform via HTTPS and WebRTC (Mediasoup / coturn).
- API Gateway routes traffic securely using Istio Service Mesh via mTLS.
- AI Symptom Checker processes clinical inputs and routes logs to the Audit Sidecar over secured localhost.
- Audit Sidecar writes encrypted, hash-chained audit logs to regional WORM Cloud Storage via HTTPS.

## Technology Stack
- Google Kubernetes Engine (GKE): Orchestrates regional container deployments for multi-region isolation.
- Istio Service Mesh / Envoy: Secures internal pod communication with mTLS and enforces authorization policies.
- Python / TensorFlow (Distroless): Powers the containerized AI symptom checker.
- Google Cloud Storage (WORM) & Cloud KMS: Ensures immutable, region-locked storage and envelope encryption for compliance data.

## Rationale
The architecture strictly segregates regional data into `europe-west3` and `us-central1` to satisfy GDPR and HIPAA data residency mandates. The asynchronous Audit Sidecar with cryptographic chaining and envelope encryption guarantees EU MDR traceability and accountability without impacting core telehealth availability.