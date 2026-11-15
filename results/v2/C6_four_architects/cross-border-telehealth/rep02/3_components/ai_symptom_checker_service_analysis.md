## Overview
[Component-level architecture for the AI Symptom Checker Service within the Cross-Border Telehealth Platform, providing traceable, AI-driven triage for EU and US patients.]

## Key Elements
* Inference Controller (Python / FastAPI)
* Region-Aware State Sanitizer (Python)
* Model Orchestrator (Python / LangChain)
* Fallback & Caching Engine (Redis / Python LRU)
* Metadata Redactor (Python)
* Audit & Traceability Logger (Python)

## Relationships
* Inference Controller -> Region-Aware State Sanitizer [In-process]
* Region-Aware State Sanitizer -> Model Orchestrator [gRPC]
* Model Orchestrator -> Fallback & Caching Engine [Redis Protocol]
* Model Orchestrator -> External AI Model Registry & Inference Provider [HTTPS/gRPC]
* Model Orchestrator -> Metadata Redactor [In-process]
* Metadata Redactor -> Audit & Traceability Logger [In-process]
* Audit & Traceability Logger -> Cloud Pub/Sub [gRPC]

## Technology Stack
* Python / FastAPI: High-performance asynchronous API framework for handling internal gRPC and HTTP routing.
* Redis / Python LRU: Caching layer providing offline resilience and non-diagnostic triage guidelines for unstable connections.
* GCP Cloud Pub/Sub: Messaging protocol ensuring asynchronous, reliable transmission of immutable audit logs.
* LangChain / Custom Wrappers: Orchestration tooling for managing external AI model inference requests.

## Rationale
[This component architecture enforces strict regional data residency and PII minimization to satisfy GDPR and HIPAA compliance. It ensures EU MDR traceability through immutable logging while maintaining offline resilience for rural patients.]