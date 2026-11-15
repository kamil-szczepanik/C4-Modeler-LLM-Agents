## Overview
This system is a cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. Its core purpose is delivering secure, compliant, and regionally isolated medical services while ensuring strict regulatory adherence (GDPR, HIPAA, and EU MDR).

## Key Elements
* Patients and Clinicians (Users)
* API Gateway (Cloud Endpoints / Apigee)
* Regional Application Services (Google Kubernetes Engine)
* AI Symptom Checker Container (GKE/Vertex AI Boundary):
  * Symptom Intake API Controller (Python/FastAPI)
  * Inference Orchestrator (Python)
  * Explainability & Sanitization Engine (Python)
  * Audit & Traceability Logger (Go)
* Policy & Consent Engine (Open Policy Agent)
* Vertex AI Endpoints (Gemini / Custom Models)
* Data & Audit Tier (Cloud SQL, Cloud Spanner, WORM Cloud Storage)
* External Pharmacy Networks, National Health Systems, and Identity Providers

## Relationships
* Regional Application Services -> Symptom Intake API Controller: Sends requests [gRPC, internal TLS]
* Symptom Intake API Controller -> Policy & Consent Engine (OPA): Verifies consent [gRPC, internal TLS]
* Symptom Intake API Controller -> Inference Orchestrator: Invokes triage [In-memory / gRPC]
* Inference Orchestrator -> Vertex AI Endpoint: Executes inference [Managed gRPC with mTLS and Workload Identity]
* Inference Orchestrator -> Explainability & Sanitization Engine: Processes outputs [In-memory]
* Explainability & Sanitization Engine -> Audit & Traceability Logger: Streams logs [Cloud Pub/Sub]
* Audit & Traceability Logger -> WORM Cloud Storage: Persists audit data [Encrypted via Cloud KMS CMEK]

## Technology Stack
* Google Cloud Platform (europe-west3, us-central1): Chosen for robust regional data residency controls and compliance tooling.
* Python (FastAPI, LangChain) & Go: Selected for high-performance microservice APIs and concurrent logging tasks.
* Vertex AI Endpoints: Provides scalable, managed machine learning inference infrastructure.
* Open Policy Agent (OPA): Enforces fine-grained, decentralized access control and patient consent checks.
* Cloud Pub/Sub & WORM Cloud Storage: Ensures reliable asynchronous messaging and immutable compliance auditing.

## Rationale
This architecture enforces strict regional data residency and compliance via GCP multi-region deployment (`europe-west3` and `us-central1`). Decomposing the AI Symptom Checker with explicit security, sanitization, and audit layers ensures high availability, rigorous EU MDR traceability, and patient data protection.