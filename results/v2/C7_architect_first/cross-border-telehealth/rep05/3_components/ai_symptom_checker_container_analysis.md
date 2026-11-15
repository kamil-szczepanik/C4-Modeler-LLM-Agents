## Overview
The AI Symptom Checker Container is a secure, multi-region microservice providing traceable, low-latency medical symptom analysis and urgency triage. It processes patient inputs while strictly enforcing regional data residency and regulatory compliance for EU and US healthcare markets.

## Key Elements
* API Router / Endpoint Handler (Python / FastAPI)
* Data Residency Guard
* Inference Engine (PyTorch / ONNX Runtime)
* Model Cache / Warm Loader
* Clinical Output Formatter
* Audit & Traceability Logger

## Relationships
* Core Services Container -> API Router: Sends symptom analysis requests [gRPC over mTLS]
* API Router -> Data Residency Guard: Validates regional payload boundaries [In-process]
* Data Residency Guard -> Inference Engine: Forwards verified payloads [In-process]
* Inference Engine -> Model Cache / Warm Loader: Retrieves pre-loaded model weights [In-memory]
* Inference Engine -> Clinical Output Formatter: Passes raw prediction vectors [In-process]
* Inference Engine -> Audit & Traceability Logger: Exports prediction metadata, inputs, and model versions [Asynchronous]
* Audit & Traceability Logger -> Google Cloud Cloud Logging / Cloud Storage: Persists immutable audit logs [HTTPS / Cloud Storage API]

## Technology Stack
* Python / FastAPI: High-performance asynchronous API framework for handling routing and request validation.
* PyTorch / ONNX Runtime: Optimized machine learning inference engine for rapid symptom analysis.
* Google Kubernetes Engine (GKE) Autopilot: Multi-region container orchestration enforcing strict isolation in `europe-west3` and `us-central1`.
* OpenTelemetry / Cloud Logging: Structured observability framework for capturing audit trails and model versioning.
* Cosign / Google Cloud KMS: Cryptographic container image signing and key management ensuring model binary integrity and encryption.

## Rationale
Isolating identical GKE clusters in Frankfurt and Iowa strictly enforces regional compliance for GDPR and HIPAA. Pre-loading models into memory via ONNX Runtime guarantees sub-two-second responses for rural users while maintaining rigorous traceability for EU MDR.