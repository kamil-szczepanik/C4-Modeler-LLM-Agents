## Overview
The AI Symptom Checker Container is a secure, low-latency microservice that provides automated urgency recommendations for patients in the EU and US. It ensures strict regulatory compliance, data residency, and traceability under EU MDR and HIPAA standards.

## Key Elements
* API Router Component (FastAPI)
* Inference Engine Component (PyTorch / ONNX Runtime)
* Audit & Traceability Component
* Fallback Cache Component (Redis / Local LRU)
* Immutable Storage (Regional GCP Cloud Storage)

## Relationships
* API Router Component -> Inference Engine Component: In-process [Python function call] via gRPC ingestion
* API Router Component -> Fallback Cache Component: Queries cached profiles [In-process LRU / Redis client]
* Inference Engine Component -> Audit & Traceability Component: Dispatches audit payload [In-process queue]
* Audit & Traceability Component -> Immutable Storage: Writes cryptographically signed audit logs [HTTPS, regional GCP Cloud Storage]

## Technology Stack
* Python / FastAPI: High-performance asynchronous API routing and payload validation
* PyTorch / ONNX Runtime: Localized symptom analysis model execution
* GCP Cloud Run / GKE with KEDA: Serverless and containerized deployment with region-locked IAM
* GCP Cloud KMS: Customer-managed encryption keys (CMEK) for at-rest data security

## Rationale
This architecture guarantees cross-border data residency compliance by isolating regional workloads in `europe-west3` and `us-central1`. It ensures high availability and accountability for rural users through local caching, encrypted disk buffering, and immutable audit logging.