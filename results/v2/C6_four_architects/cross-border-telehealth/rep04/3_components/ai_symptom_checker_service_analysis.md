## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The system ensures strict regulatory compliance, data residency, and traceability across GCP regions.

## Key Elements
* API Router / Controller (FastAPI)
* Region Routing / Data Residency Enforcer
* FHIR Normalizer
* Clinical NLP Pipeline (spaCy / Hugging Face transformers)
* Model Registry Client
* Inference Engine (PyTorch / ONNX Runtime)
* Audit & Traceability Component

## Relationships
* API Router -> Region Routing / Data Residency Enforcer: Validates residency constraints [Internal Python method call]
* Region Routing -> FHIR Normalizer: Translates patient data [Internal Python method call]
* FHIR Normalizer -> Clinical NLP Pipeline: Extracts normalized medical entities [Internal Python method call]
* Model Registry Client -> Inference Engine: Provides loaded model artifacts and version IDs [In-memory reference]
* Inference Engine -> Audit & Traceability Component: Passes inference payloads and model version metadata [Internal event dispatch]
* Audit & Traceability Component -> Google Cloud Pub/Sub: Emits cryptographic audit logs [Cloud Pub/Sub API over TLS]

## Technology Stack
* Python / FastAPI: Core framework for asynchronous REST endpoints
* PyTorch / ONNX Runtime: Low-latency, predictable inference execution for triage models
* spaCy / Hugging Face transformers: Clinical NLP processing for entity extraction
* Google Cloud Pub/Sub: Asynchronous event streaming for audit logs
* GCP (europe-west3, us-central1): Cloud infrastructure ensuring region-locked data residency

## Rationale
This component architecture isolates the AI inference pipeline while enforcing strict region boundaries and tamper-evident audit logging. This design directly satisfies GDPR, HIPAA, and EU MDR compliance for traceability and data residency.