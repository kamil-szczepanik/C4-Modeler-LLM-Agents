## Overview
[The system is a Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. Its core purpose is to deliver secure, cross-border healthcare while strictly enforcing regional data residency and compliance.]

## Key Elements
* API Router Component (Python/FastAPI)
* Consent Enforcement Interceptor (Open Policy Agent SDK)
* Clinical Inference Orchestrator (Python)
* Payload Sanitizer & PII Redactor (Python/Presidio)
* Region-Aware Model Router (Python)
* Symptom Session Cache (Async-LRU / Redis client)
* FHIR Interoperability Mapper (Custom Pydantic-FHIR)
* Audit & Traceability Logger (Python)

## Relationships
* API Router Component -> Consent Enforcement Interceptor: Validates user consent [In-memory function call]
* Consent Enforcement Interceptor -> Clinical Inference Orchestrator: Triggers analysis [In-memory function call]
* Clinical Inference Orchestrator -> Payload Sanitizer & PII Redactor: Sanitizes symptom text [In-memory function call]
* Payload Sanitizer & PII Redactor -> AI Model Provider / Inference Service: Sends de-identified clinical payloads [HTTPS / REST]
* Clinical Inference Orchestrator -> Region-Aware Model Router: Resolves regional endpoint [In-memory function call]
* Region-Aware Model Router -> AI Model Provider / Inference Service: Sends de-identified payload to region-specific AI instance [HTTPS / REST]
* API Router Component & Clinical Inference Orchestrator -> Symptom Session Cache: Manages multi-turn conversation state [In-memory / Redis]
* Clinical Inference Orchestrator -> FHIR Interoperability Mapper: Normalizes symptom assessment output [In-memory function call]
* FHIR Interoperability Mapper -> Audit & Traceability Logger: Passes structured FHIR audit payload [In-memory queue]
* Audit & Traceability Logger -> GCP Cloud Storage with Object Retention (WORM): Writes immutable logs [GCP IAM / HTTPS]

## Technology Stack
* Python (FastAPI): Powers the core container services and REST/gRPC routing.
* Open Policy Agent SDK: Enforces regional consent policies locally.
* Microsoft Presidio: Strips PII locally before external AI inference for GDPR/HIPAA compliance.
* Async-LRU / Redis: Caches multi-turn session states for rural connectivity resilience.
* Custom Pydantic-FHIR: Standardizes clinical outputs to HL7 FHIR resources for interoperability.
* GCP Cloud Storage (WORM): Stores immutable audit logs for EU MDR traceability compliance.

## Rationale
[This architecture fits the requirements by isolating region-specific processing in GCP (europe-west3 and us-central1) to maintain strict data residency. It ensures compliance, traceability, and resilience for unstable rural connections through local caching and PII sanitization.]