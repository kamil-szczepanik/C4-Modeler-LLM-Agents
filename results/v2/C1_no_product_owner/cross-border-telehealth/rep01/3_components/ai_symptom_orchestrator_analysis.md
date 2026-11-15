## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces regional data residency and compliance with GDPR, HIPAA, and EU MDR.

## Key Elements
- API Router Component (FastAPI)
- Consent Proxy & Policy Enforcer Component
- Model Invocation & Adaptor Component
- Audit & Traceability Logger Component with KMS Signing Interceptor
- AI Symptom Checker Engine (External)
- Consent & Audit Service, Google Cloud SQL (PostgreSQL), Google Memorystore (Redis), Google Cloud Storage (GCS)
- Istio Service Mesh, GCP KMS, ArgoCD

## Relationships
- API Router -> Consent Proxy: In-process function call
- Consent Proxy -> Consent Service: Synchronous gRPC over TLS with Istio circuit breaker
- Model Invocation -> AI Symptom Checker Engine: HTTPS APIs with mTLS and certificate pinning
- Audit Logger -> GCP KMS: Envelope encryption over gRPC
- Audit Logger -> Google Cloud Storage: Asynchronous dispatch with disk-backed WAL buffer

## Technology Stack
- Python, FastAPI: Core framework for the AI Symptom Orchestrator container
- gRPC over TLS, HTTP/2: Inter-service communication protocol
- Google Cloud SQL (PostgreSQL), Google Memorystore (Redis), Google Cloud Storage (GCS): Regional data persistence and caching
- GCP KMS: Cryptographic signing for EU MDR compliance logs
- Istio Service Mesh, ArgoCD: Zero-trust networking and regional deployment management

## Rationale
Regional isolation and local WAL buffers enforce strict GDPR and HIPAA data residency while maintaining high availability. Fail-closed consent policies and GCP KMS cryptographic signing satisfy EU MDR traceability and accountability requirements.