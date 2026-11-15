## Overview
The AI Symptom Checker Container is a Python/FastAPI microservice within the Cross-Border Telehealth Platform that provides real-time, traceable triage recommendations for patients in the EU and US. It balances low-latency inference with strict regional data residency and EU MDR compliance.

## Key Elements
* Triage Orchestrator (FastAPI): Manages conversation flow and service coordination.
* Model Inference Engine (Hugging Face Transformers): Executes localized LLM inference.
* Clinical Rule Validator (Pydantic): Applies deterministic safety overrides and input validation.
* Audit Logger: Handles regional traceability and immutable logging.

## Relationships
* Node.js API Gateway -> Triage Orchestrator: Requests AI symptom analysis [Internal gRPC, mTLS]
* Triage Orchestrator -> Model Inference Engine & Clinical Rule Validator: Coordinates validation and local inference [In-memory Python calls]
* Audit Logger -> Go Consent & Localization Engine: Dispatches structured JSON payloads and model version tags [Internal gRPC, async]

## Technology Stack
* Python 3.11 & FastAPI: Core runtime for high-performance asynchronous API endpoints.
* Hugging Face Transformers: Localized LLM execution for symptom triage.
* Pydantic: Strict schema validation and deterministic rule interception.
* Google Kubernetes Engine (GKE): Container orchestration with GPU node pools (`europe-west3`, `us-central1`).
* Istio Service Mesh: Enforces mutual TLS (mTLS) and telemetry tracking.

## Rationale
This architecture ensures low-latency AI inference while maintaining strict regional data isolation required by GDPR and HIPAA. Furthermore, asynchronous auditing and deterministic safety overrides guarantee full traceability for EU MDR compliance and patient safety.