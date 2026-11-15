## Overview
The AI Symptom Checker Service provides traceable, region-isolated medical urgency recommendations for EU and US patients. It processes patient inputs securely while meeting strict GDPR, HIPAA, and EU MDR compliance requirements.

## Key Elements
* API Router & Auth Middleware (FastAPI)
* Input Sanitization & Guardrail Component
* Clinical Inference Proxy (GCP Vertex AI endpoints)
* Output Validation Guardrail
* Traceability & Audit Component (Google Cloud Pub/Sub, WORM storage)
* Data Residency Validator (GCP VPC Service Controls)

## Relationships
* Core Telehealth Backend -> API Router: Requests AI symptom analysis via mTLS with OAuth2/JWT tokens
* API Router -> Input Sanitization: Forwards validated payloads for PII stripping
* Input Sanitization -> Clinical Inference Proxy: Forwards sanitized prompts via internal VPC
* Clinical Inference Proxy -> GCP Vertex AI (`europe-west3`, `us-central1`): Invokes ML models via gRPC
* Traceability & Audit Component -> Google Cloud Pub/Sub: Pushes audit logs via TLS
* Audit Component -> WORM buckets: Stores cryptographically signed, CMEK-encrypted records

## Technology Stack
* Python & FastAPI: Powers lightweight routing, validation, and middleware logic
* GCP Vertex AI: Hosts regionally isolated model endpoints to decouple heavy inference workloads
* Google Cloud Pub/Sub: Enables asynchronous, reliable audit logging to prevent request blocking
* Google Cloud KMS & WORM Storage: Ensures cryptographic traceability and immutable audit logs for EU MDR compliance
* GCP VPC Service Controls: Enforces data residency at the network layer

## Rationale
This architecture decouples heavy ML inference to ensure high availability and prevent timeout bottlenecks. It embeds strict regional isolation, cryptographic audit logging, and input/output guardrails to satisfy demanding healthcare regulations and data residency mandates.