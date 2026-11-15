## Overview
A cross-border telehealth platform delivering video consultations, e-prescriptions, and an AI symptom checker for EU and US patients with strict regional data residency. The AI Symptom Checker Service ensures regulatory compliance and resilience in low-bandwidth environments via local PII masking and fallback logic.

## Key Elements
* Patients [person, context]
* Licensed Clinicians [person, context]
* AI Symptom Checker Service [container, container] (Python / FastAPI)
* Inference Orchestrator Component [component] (Python / FastAPI)
* PII/PHI Masking Component [component] (Python / SpaCy/Regex)
* Audit & Traceability Component [component] (Python / SQLAlchemy)
* AI Model Providers / Medical Devices [externalSystem, context]
* Database Cluster [container, container] (Cloud Spanner / PostgreSQL)

## Relationships
* Patients -> Cross-Border Telehealth Platform [HTTPS / WebSockets (adaptive codec)]
* API Gateway & Routing Service -> AI Symptom Checker Service [gRPC / mTLS]
* Inference Orchestrator Component -> PII/PHI Masking Component [In-memory function call]
* Inference Orchestrator Component -> Audit & Traceability Component [Asynchronous gRPC / Database write]
* AI Symptom Checker Service -> AI Model Providers / Medical Devices [HTTPS (REST/gRPC with payload masking)]
* AI Symptom Checker Service -> Database Cluster [TCP / CMEK]

## Technology Stack
* Python / FastAPI: Powers the AI Symptom Checker Service for rapid asynchronous request handling.
* SpaCy/Regex: Enables local PII/PHI masking to satisfy GDPR and HIPAA.
* Google Kubernetes Engine (GKE): Deploys microservices across `europe-west3` and `us-central1` with GCP VPC Service Controls.
* Google Cloud Spanner / PostgreSQL: Secures regional data storage using Google Cloud KMS CMEK.

## Rationale
This architecture enforces strict regional data isolation and localized PII masking to comply with GDPR, HIPAA, and EU MDR mandates. Furthermore, it incorporates robust circuit breakers and lightweight fallbacks to maintain system availability for rural users on unstable connections.