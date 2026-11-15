## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI-driven symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance (GDPR, HIPAA, EU MDR), and robust tracing for medical outputs.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Google Cloud API Gateway / Envoy
- AI Symptom Checker Container (Python / FastAPI)
- API Router / Controller (FastAPI)
- Consent & Scope Validator (Middleware)
- Triage Engine (Python/PyTorch or LangChain)
- Audit & Traceability Logger
- Google Cloud SQL (PostgreSQL with FHIR extensions)
- Core Telehealth Service (Node.js / Go)

## Relationships
- API Gateway -> Consent & Scope Validator: Routes symptom check requests [gRPC over mTLS]
- Consent & Scope Validator -> API Router: Forwards validated requests [Internal function call]
- API Router -> Triage Engine: Initiates urgency assessment [In-memory function call]
- Triage Engine -> Audit & Traceability Logger: Captures model inputs, versions, and outputs [Asynchronous event]
- Triage Engine -> Google Cloud SQL: Persists clinical data locally [SQL over mTLS, region-bound]
- Core Telehealth Service -> Audit & Traceability Logger: Sends clinician overrides [gRPC]

## Technology Stack
- GCP (europe-west3, us-central1): Cloud provider and regions selected to enforce strict regional data residency.
- Python / FastAPI: Core framework for the AI Symptom Checker Container and its internal routing/triage components.
- PyTorch / LangChain: Frameworks powering the symptom-to-urgency AI inference engine.
- gRPC with mTLS: Internal service-to-service communication protocol ensuring encrypted, authenticated transport.
- Google Cloud SQL (PostgreSQL): Regional data storage supporting FHIR extensions and transactional integrity.
- GCP VPC Service Controls & Binary Authorization: Security controls enforcing network boundaries, container image signing, and data isolation.

## Rationale
This architecture segregates data processing per region to satisfy strict EU GDPR and US HIPAA residency mandates. Furthermore, dedicated components like the Audit & Traceability Logger and Consent Validator guarantee EU MDR compliance and secure, traceable AI operations.