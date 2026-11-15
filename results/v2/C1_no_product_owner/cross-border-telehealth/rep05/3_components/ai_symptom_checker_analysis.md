## Overview
Cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. Enforces strict regional data residency and compliance via GCP multi-region deployment.

## Key Elements
* API Router / Controller Component (FastAPI)
* Clinical NLP / Feature Extraction Component (spaCy / Hugging Face Transformers)
* Inference Orchestrator Component (Python)
* Audit & Traceability Component (Python SDK, Cloud KMS)
* Terminology Mapping Component (Python)
* Infrastructure: Google Kubernetes Engine (GKE), Google Cloud Storage (GCS), GCP Pub/Sub

## Relationships
* API Gateway -> API Router: Routes requests via gRPC over mTLS
* Inference Orchestrator -> Regional GCS Buckets: Fetches model weights via HTTPS
* Audit & Traceability Component -> Immutable Audit Logging Service: Pushes signed audit logs via gRPC

## Technology Stack
* FastAPI / Python: High-throughput async gRPC execution for AI components
* spaCy / Hugging Face Transformers: Clinical NLP feature extraction and tokenization
* Cloud KMS / Sigstore: Cryptographic signing and model integrity verification
* OpenTelemetry: Distributed tracing across gRPC service boundaries

## Rationale
Containerized microservices running on GKE across `europe-west3` and `us-central1` isolate regional data to comply with GDPR and HIPAA mandates. Isolated internal components ensure strict AI auditability, memory sanitization, and EU MDR compliance.