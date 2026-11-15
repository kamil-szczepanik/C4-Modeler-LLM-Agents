## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients on GCP. It enforces strict regional data residency, regulatory compliance, and resilience for rural areas.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Web Frontend (PWA) (Next.js / React)
- API Gateway (Envoy and Cloud Load Balancing)
- Core Backend services (Go / Spring Boot) consisting of Consent & Policy Engine, Consultation Orchestrator, Clinical Record Manager, Audit & Compliance Logger, and Session State Cache (Redis / Memorystore)
- AI Symptom Checker (Python / FastAPI)
- Integration / Interoperability Service (Node.js / Java)
- Media Relaying Service (LiveKit SFU/MCU)
- Data Storage (Cloud SQL PostgreSQL and Cloud Storage WORM buckets)

## Relationships
- Web Frontend -> API Gateway: Accesses platform services [HTTPS / WebSocket]
- API Gateway -> Core Backend services: Routes and authorizes requests [gRPC]
- Consent & Policy Engine -> Audit & Compliance Logger: Emits access and consent decisions [gRPC]
- Consultation Orchestrator -> Session State Cache: Buffers ephemeral session states [Redis Protocol]
- Core Backend services -> AI Symptom Checker: Requests AI symptom analysis [gRPC]
- Core Backend services -> Data Storage: Persists records and audit logs [PostgreSQL Protocol / WORM Storage]

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Isolated multi-region infrastructure enforcing regional data residency.
- Go & Spring Boot: High-concurrency backend services and complex domain logic.
- Redis (Memorystore): Ephemeral session buffering for rural connection drops.
- PostgreSQL (Cloud SQL) & WORM Cloud Storage: Transactional persistence and immutable, encrypted audit logging.
- OpenTelemetry & ArgoCD: Distributed tracing and GitOps regional deployment isolation.

## Rationale
This architecture ensures strict GDPR and HIPAA compliance by isolating regional data workloads while supporting high-availability video care in rural areas. The modular Go and Spring Boot backend guarantees audit traceability for medical devices and robust resilience against intermittent connectivity.