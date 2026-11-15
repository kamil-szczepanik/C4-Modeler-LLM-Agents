## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict data residency, regulatory compliance, and auditability across regional GCP cloud environments.

## Key Elements
- AI Symptom Checker Container (regional GKE clusters in `europe-west3` and `us-central1`)
- API Gateway Container (Istio Service Mesh with mTLS)
- Google Cloud Logging and Monitoring / OpenTelemetry
- Google Cloud Artifact Registry (region-locked)
- GCP Cloud Armor and Cloud CDN

## Relationships
- API Gateway Container -> AI Symptom Checker Container: Routes symptom checking requests via [Istio mTLS]
- AI Symptom Checker Container -> Google Cloud Logging and Monitoring: Logs inputs, model versions, confidence scores using [OpenTelemetry, Region-bound log sinks]
- GKE Nodes -> Google Cloud Artifact Registry: Pulls immutable, signed AI model weights using [Binary Authorization]

## Technology Stack
- Google Kubernetes Engine (GKE): Orchestrates regional container workloads to enforce data residency
- Istio Service Mesh: Secures container-to-container communication via mTLS and zero-trust policies
- OpenTelemetry: Captures structured audit logs including inputs, model versions, and confidence scores for EU MDR compliance
- Google Cloud Artifact Registry: Stores region-locked, immutable AI model artifacts
- AppArmor / Seccomp: Restricts container runtime permissions for enhanced security

## Rationale
This architecture guarantees strict regional data isolation to comply with GDPR and HIPAA mandates. It also ensures traceability and clinical safety for the AI symptom checker via immutable artifacts and comprehensive logging.