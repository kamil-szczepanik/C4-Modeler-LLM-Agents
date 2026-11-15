## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US while enforcing strict regional data residency. The AI Symptom Checker Service is architected as an isolated, compliant component pipeline running locally on GCP to meet GDPR, HIPAA, and EU MDR standards.

## Key Elements
- **API Router / Endpoint Controller**: FastAPI-based controller validating incoming gRPC requests.
- **Consent & Policy Enforcement Interceptor**: FastAPI Middleware verifying active patient consent per data-sharing purpose.
- **Regional Context & Guardrails Engine**: Enforces clinical triage guidelines and strips PHI prior to inference.
- **Inference Orchestrator**: Manages prompt engineering, context windows, and model execution.
- **ML Model Runtime**: Runs local quantized LLM/classification models via ONNX Runtime / gRPC-local.
- **Clinical Triage Validator**: Post-processes urgency scores against deterministic safety thresholds.
- **Audit & Traceability Logger**: Captures inputs, model versions, and outputs for EU MDR traceability.

## Relationships
- *API Router* -> *Consent Interceptor* (In-process FastAPI Middleware)
- *Consent Interceptor* -> *Guardrails Engine* (In-process)
- *Guardrails Engine* -> *Inference Orchestrator* (In-process)
- *Inference Orchestrator* -> *ML Model Runtime* (In-process via ONNX Runtime / gRPC-local)
- *Inference Orchestrator* -> *Clinical Triage Validator* (In-process)
- *Clinical Triage Validator* -> *API Router* (In-process)
- *Audit Logger* -> *Google Cloud Pub/Sub* ([gRPC])
- *Audit Logger* -> *Google Cloud BigQuery / Cloud Storage* ([REST/gRPC via Pub/Sub])

## Technology Stack
- **Python / FastAPI**: Core framework for the AI Symptom Checker container due to robust ML ecosystem support.
- **ONNX Runtime / vLLM**: Local model runtime executing quantized LLMs to prevent external API calls and ensure regional data residency.
- **Google Cloud Pub/Sub & BigQuery / Cloud Storage**: Asynchronous messaging and regional datastores ensuring immutable audit logging for EU MDR compliance.
- **GCP (europe-west3, us-central1)**: Target cloud regions enforcing isolated data storage per jurisdiction.

## Rationale
This component architecture separates boundary security, deterministic validation, and local inference to comply with GDPR, HIPAA, and EU MDR regulations. Asynchronous, region-locked telemetry and in-process execution eliminate cross-border data leakage while maintaining high accountability and availability.