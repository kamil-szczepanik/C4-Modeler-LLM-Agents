## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI-driven symptom checker for patients across the EU and US. It enforces regional data residency and strict regulatory compliance (GDPR, HIPAA, and EU MDR) using Google Cloud Platform.

## Key Elements
- **AI Symptom Checker Container**: Python-based container running FastAPI and PyTorch on GKE.
- **API Router / Controller**: FastAPI component handling internal gRPC endpoints.
- **Preprocessing & NLP Component**: spaCy / Hugging Face component for clinical entity extraction.
- **Inference Engine**: PyTorch-based execution engine for care urgency prediction.
- **Audit & Traceability Logger**: Component capturing inputs, predictions, and model versions.
- **Model Registry Client**: Component fetching version-pinned models from regional GCP Artifact Registry.
- **Google Cloud Pub/Sub**: Message broker for asynchronous audit event emission.
- **Istio Service Mesh**: Enforces mTLS, circuit breaking, and traffic management.

## Relationships
- `Core Telehealth Service` -> `API Router`: Sends symptom analysis data [Internal gRPC with mTLS and JWT metadata]
- `API Router` -> `Preprocessing & NLP Component`: Sanitizes and extracts entities [In-memory function calls]
- `Preprocessing & NLP Component` -> `Inference Engine`: Passes clinical tokens [PyTorch tensors]
- `Inference Engine` -> `Audit & Traceability Logger`: Dispatches traceability events [Asynchronous event dispatch]
- `Audit & Traceability Logger` -> `Google Cloud Pub/Sub`: Emits audit payloads [gRPC / REST regional topics]
- `Inference Engine` -> `Model Registry Client`: Loads model weights [Local cache read]

## Technology Stack
- **Python / FastAPI**: Powers the symptom checker container API for rapid async request handling.
- **PyTorch**: Executes machine learning models for symptom analysis and care urgency prediction.
- **spaCy / Hugging Face**: Performs clinical natural language processing and tokenization.
- **Google Kubernetes Engine (GKE)**: Orchestrates container workloads with NVIDIA T4 GPU node pools.
- **Istio Service Mesh**: Secures service-to-service communication via mTLS and provides circuit breaking.
- **Google Cloud Pub/Sub**: Decouples non-blocking asynchronous audit logging across regional topics.
- **Google Cloud KMS & Storage**: Secures data at rest with CMEK and enforces immutable object retention.

## Rationale
This architecture guarantees strict regional isolation of health data in `europe-west3` and `us-central1` to satisfy GDPR and HIPAA mandates. Furthermore, decoupling asynchronous audit logging via Google Cloud Pub/Sub and utilizing immutable storage ensures complete traceability for AI outputs required by EU MDR without compromising runtime availability or inference latency.