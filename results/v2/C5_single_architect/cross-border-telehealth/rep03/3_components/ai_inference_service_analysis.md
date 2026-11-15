## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency, GDPR/HIPAA compliance, and EU MDR traceability.

## Key Elements
* Patients and Licensed Clinicians (Users)
* API Gateway (Envoy / GCP API Gateway)
* AI Inference Service (Python / FastAPI)
* API Controller (FastAPI component)
* Consent & Policy Enforcer (Python middleware component)
* Model Orchestrator (PyTorch / Hugging Face component)
* Audit & Lineage Logger (SQLAlchemy component)
* Regional Data Stores (GCP Cloud SQL / Spanner)
* External Systems: National E-Prescription Networks (EU), Pharmacy Systems (US)

## Relationships
* API Gateway -> API Controller: Routes symptom check requests [gRPC / REST]
* API Controller -> Consent & Policy Enforcer: Intercepts requests for consent validation [In-process middleware]
* Consent & Policy Enforcer -> Regional Data Stores: Reads active patient consent flags [SQL]
* API Controller -> Model Orchestrator: Delegates inference tasks [In-process Python calls]
* Model Orchestrator & API Controller -> Audit & Lineage Logger: Persists inputs, outputs, and model versions [SQL]

## Technology Stack
* GCP (europe-west3, us-central1): Cloud platform ensuring strict regional data isolation per compliance mandates.
* Python / FastAPI: Core framework for the AI Inference Service and API Controller.
* PyTorch / Hugging Face: ML runtime for region-locked symptom checker models.
* Redis: Low-latency local cache for consent and policy evaluation.
* SQLAlchemy: ORM ensuring secure, consistent writes to regional databases.

## Rationale
This architecture guarantees strict regional data residency by isolating EU and US workloads while maintaining immutable audit logs for EU MDR compliance. Modular internal components ensure low-latency policy enforcement and traceable AI outputs without cross-border data leakage.