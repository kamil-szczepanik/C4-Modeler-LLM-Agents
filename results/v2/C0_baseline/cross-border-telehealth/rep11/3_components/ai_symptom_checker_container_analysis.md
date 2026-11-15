## Overview
Cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. Ensures GDPR and HIPAA compliance with strict regional data residency.

## Key Elements
- Patients (EU/US) & Licensed Clinicians
- Web App & Mobile App (React / Flutter)
- API Gateway (Cloud Endpoints / Envoy)
- AI Symptom Checker Container (Python / FastAPI / PyTorch / MLflow)
- Input Sanitization & Validation Engine (Pydantic / FastAPI)
- Inference Engine (PyTorch)
- Disclaimer & Localization Formatter
- Audit & Telemetry Logger (MLflow Tracking Client)
- Data Storage (Cloud SQL PostgreSQL / Cloud Storage / CMEK)

## Relationships
- API Gateway -> AI Symptom Checker Container: Routes gRPC requests with mTLS (Istio/Anthos)
- API Router -> Input Sanitization Engine: Validates raw payloads [In-process]
- Input Sanitization -> Inference Engine: Passes sanitized features [In-process]
- Inference Engine -> Disclaimer Formatter: Passes raw recommendation [In-process]
- Disclaimer Formatter -> Audit Logger: Triggers telemetry record [Async Queue]
- Audit Logger -> Data Storage: Persists immutable logs via SQL/REST with CMEK

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Enforces regional data residency constraints.
- Python / FastAPI: High-performance async API routing and strict schema validation.
- PyTorch / MLflow: Local symptom-checking model execution and traceability logging.
- Pydantic: Payload validation and adversarial input defense.
- Kubernetes / Istio: Regional deployments, canary rollouts, and traffic management.

## Rationale
Regional container isolation in GCP guarantees strict compliance with EU GDPR and US HIPAA mandates. Decoupled async auditing and strict input validation ensure EU MDR traceability, security, and high availability for rural users.