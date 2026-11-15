## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures regional compliance by keeping EU patient data in `europe-west3` and US data in `us-central1` on GCP.

## Key Elements
- API Router / Endpoint Handler (FastAPI / Pydantic)
- Region-Aware Model Orchestrator (Python)
- Clinical Rules Engine (Python / Pydantic)
- Traceability Logger (Python)
- GCP Cloud Storage (Model weights storage)
- GCP BigQuery (Audit logs sink)

## Relationships
- `API Router` -> `Model Orchestrator`: Direct function calls
- `Model Orchestrator` -> `Clinical Rules Engine`: In-memory data passing [In-memory]
- `Clinical Rules Engine` -> `API Router`: In-memory data passing [In-memory]
- `Model Orchestrator` -> `Traceability Logger`: Asynchronous audit event emission [In-memory / Async Queue]
- `Traceability Logger` -> `GCP BigQuery`: Audit log export [HTTPS / GCP BigQuery API]
- `Model Orchestrator` -> `GCP Cloud Storage`: Model weight retrieval with SHA-256 verification [HTTPS]

## Technology Stack
- FastAPI & Python: Powers the core component runtime with high-performance asynchronous handling.
- Pydantic: Enforces strict input validation and schema sanitization to prevent prompt injection.
- GCP Cloud Storage: Stores immutable, version-tagged model weights with cryptographic verification.
- GCP BigQuery: Securely stores pseudonymized, timestamped audit payloads for EU MDR traceability.
- GKE & Anthos Service Mesh: Manages pod resource isolation, node pools, and mTLS traffic routing.

## Rationale
This component architecture enforces strict EU MDR traceability and security controls by decoupling inference, deterministic clinical validation, and immutable audit logging. Regional isolation and cryptographic integrity checks ensure full compliance with regional healthcare regulations without compromising performance.