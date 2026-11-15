## Overview
The AI Symptom Checker Service provides secure, traceable AI-powered urgency recommendations for patients within a cross-border telehealth platform. It enforces regional data residency and strict regulatory compliance across the EU and US.

## Key Elements
- Symptom Assessment API Handler (Python / FastAPI)
- Consent & Policy Enforcer (Python / OPA SDK)
- Clinical NLP Processor (Python / spaCy & Transformers)
- Inference Orchestrator (Python / PyTorch / LangChain)
- Regional Model Gateway (Python / HTTPX)
- Safety & Fallback Guardrail Engine (Python / Rule-based heuristics)
- Traceability & Audit Emitter (Python / OpenTelemetry SDK)
- Audit Persistence Hook (Python / SQLAlchemy)

## Relationships
- Symptom Assessment API Handler -> Consent & Policy Enforcer: Validates active data-processing consent [gRPC / Local Cache]
- Symptom Assessment API Handler -> Clinical NLP Processor: Extracts entities [In-memory]
- Clinical NLP Processor -> Inference Orchestrator: Requests urgency score [In-memory]
- Inference Orchestrator -> Regional Model Gateway: Dispatches sanitized features to regional LLM endpoints [REST/mTLS]
- Inference Orchestrator -> Safety & Fallback Guardrail Engine: Validates raw urgency recommendation [In-memory]
- Safety & Fallback Guardrail Engine -> Symptom Assessment API Handler: Returns finalized care urgency [In-memory]
- Inference Orchestrator -> Traceability & Audit Emitter: Publishes immutable audit logs [gRPC]
- Traceability & Audit Emitter -> Audit Persistence Hook: Persists audit logs locally [PostgreSQL over mTLS]

## Technology Stack
- Python / FastAPI: High-performance asynchronous API handling and request validation
- spaCy & Transformers: Advanced NLP for extracting clinical entities from unstructured text
- PyTorch & LangChain: Core ML inference orchestration and regional LLM execution
- OPA SDK: Runtime GDPR/HIPAA data-processing consent enforcement
- OpenTelemetry SDK & SQLAlchemy: Immutable audit logging and regional PostgreSQL persistence for EU MDR traceability

## Rationale
This component architecture enforces strict regional data residency in GCP (`europe-west3` and `us-central1`) via the Regional Model Gateway. Additionally, it guarantees EU MDR and HIPAA compliance through built-in OPA consent checks, OpenTelemetry audit logging, and deterministic safety guardrails.