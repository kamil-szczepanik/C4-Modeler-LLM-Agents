## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency, GDPR/HIPAA compliance, and EU MDR traceability.

## Key Elements
- Patients & Licensed Clinicians
- Web Application & Mobile Client Gateway (React / React Native)
- API Gateway (Node.js / Go)
- AI Symptom Checker Service (Python / FastAPI, Vertex AI): Comprising API Router, Pseudonymization & Sanitization, Inference Orchestrator, Audit & Traceability, and External Fallback Handler components.
- Database and Storage (Google Cloud SQL PostgreSQL, Google Cloud Storage WORM with Bucket Lock)
- Service Mesh (Istio Service Mesh, Envoy proxy)

## Relationships
- Web App / Mobile Client -> API Gateway: Manages requests [HTTPS / REST]
- API Gateway -> AI Symptom Checker Service: Invokes AI symptom analysis and logging [gRPC over mTLS (Istio)]
- Inference Orchestrator -> Vertex AI: Requests symptom analysis [HTTPS / Cloud APIs over VPC Service Controls]
- Audit & Traceability -> Google Cloud Storage WORM: Persists immutable logs [HTTPS / Cloud Storage API]

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Ensures regional data residency compliance.
- Python / FastAPI & Vertex AI: Powers the traceable AI symptom checker.
- Google Cloud Storage WORM (Compliance Mode): Guarantees tamper-proof medical audit logs.
- Istio Service Mesh & Envoy: Enforces mTLS, traffic routing, and circuit breaking.

## Rationale
This architecture uses regional GCP deployments and VPC Service Controls to guarantee strict data residency between the EU and US. Containerized microservices, immutable WORM storage, and automated sanitization ensure compliance with GDPR, HIPAA, and EU MDR traceability mandates.