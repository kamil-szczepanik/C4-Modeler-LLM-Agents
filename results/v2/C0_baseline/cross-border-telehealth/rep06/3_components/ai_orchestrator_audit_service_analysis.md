## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The system enforces strict regional data residency, GDPR/HIPAA compliance, and traceable AI triage.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- AI Orchestrator & Audit Service (Python/Go on GKE)
- API Router & Sanitizer Component (Python/FastAPI)
- Orchestration Engine Component (Python/Go)
- Audit & WORM Writer Component (Go)
- Consent-Aware Retention Worker Component (Python/Go)
- External AI Inference Service
- Regional Data Storage (Cloud SQL, BigQuery, Google Cloud Storage Bucket Lock)
- Google Cloud KMS

## Relationships
- API Gateway -> API Router & Sanitizer: Routes AI symptom checking and audit requests via gRPC / mTLS (Istio Mesh)
- API Router & Sanitizer -> AI Inference Service: Sends sanitized prompts for urgency recommendations via gRPC with local PII sanitization
- Audit & WORM Writer -> Regional Data Storage: Writes immutable audit logs via WORM storage / BigQuery
- Consent-Aware Retention Worker -> Google Cloud KMS: Executes crypto-shredding of encryption keys for consent revocation

## Technology Stack
- Google Cloud Platform (GCP): Primary cloud provider utilizing `europe-west3` and `us-central1` regions for data residency
- Google Kubernetes Engine (GKE): Container orchestration platform managed via ArgoCD with regional node pools
- Python & Go: Core implementation languages for services and workers
- Istio Service Mesh: Provides zero-trust mTLS service-to-service communication
- Google Cloud KMS: Implements envelope encryption, cryptographic signing, and crypto-shredding

## Rationale
This architecture ensures strict compliance with EU GDPR, US HIPAA, and EU MDR through regional isolation and immutable WORM logging. It maintains high availability and patient safety via fail-closed PII sanitization and circuit-breaker fallbacks to human clinicians.