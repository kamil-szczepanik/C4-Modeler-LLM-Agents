## Overview
[Component-level C4 architecture summary for the AI Symptom Checker Service within the Cross-Border Telehealth Platform.]
[Processes patient symptoms using AI to recommend care urgency while ensuring EU GDPR and US HIPAA compliance.]

## Key Elements
- API Router / Controller (FastAPI): Handles incoming gRPC requests
- Clinical NLP / Feature Extractor (spaCy / SciSpaCy): Normalizes text into HL7 FHIR / SNOMED CT
- Inference Engine (PyTorch / Hugging Face): Executes clinical triage models
- Explainability Module (SHAP / LIME): Generates feature-attribution weights
- Semantic Caching Component (Regional Memorystore for Redis): Caches symptom results
- Audit & Traceability Logger: Captures synchronous write-ahead logs
- Google Kubernetes Engine (GKE): Container orchestration platform

## Relationships
- Core Telehealth Backend -> API Router / Controller: Sends symptom data via [gRPC / mTLS]
- API Router -> Semantic Caching Component: Checks for cached triage results [Redis Protocol / mTLS]
- API Router -> Inference Engine: Evaluates uncached symptom inputs [Internal Python function call]
- Inference Engine -> Audit & Traceability Logger: Persists immutable logs to [Regional Cloud SQL & WORM Cloud Storage]
- Explainability Module -> Clinician Dashboard: Provides transparency data via [HTTPS / REST]

## Technology Stack
- FastAPI & Python: Core framework for high-performance async request handling
- PyTorch & SciSpaCy: Machine learning and clinical NLP processing libraries
- Redis (Memorystore): Regionally isolated caching for low-latency responses
- Istio Service Mesh: Enforces mTLS and circuit breaking
- Google Cloud KMS: Provides regional encryption keys for data residency compliance
- gVisor: Runtime sandbox for secure fallback execution

## Rationale
[This component architecture ensures strict regional data residency across GCP regions while meeting EU MDR traceability mandates.]
[It provides fault-tolerant degradation to support rural patients with unstable internet connections.]