## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency and compliance using a distributed GCP-hosted architecture.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Legal/Compliance Officers (Admin Persona)
- Web/Mobile Client (Flutter / React Native)
- API Gateway (Cloud Endpoints / Envoy)
- Core Telehealth Backend (Node.js / Go)
- Consent Management Container (Decomposed into Consent API Controller, Consent Evaluation Engine, Audit Logger & Ledger, and Consent Pub/Sub Broker)
- Regional Databases (Cloud SQL PostgreSQL & WORM Cloud Storage)
- Regional Pub/Sub Broker (Redis / Memorystore)

## Relationships
- Web/Mobile Client -> API Gateway: Routes client requests via HTTPS / REST
- API Gateway -> Consent API Controller: Verifies permissions via gRPC [gRPC]
- Consent Evaluation Engine -> Consent Ledger: Queries compliance records via internal gRPC [gRPC]
- Consent Evaluation Engine -> Consent Pub/Sub Broker: Broadcasts revocation events via RESP [Redis Protocol]
- Core Telehealth Backend -> Consent Pub/Sub Broker: Subscribes to revocation events via RESP [Redis Protocol]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing `europe-west3` and `us-central1` for geographic isolation.
- Node.js & Go: Chosen for high-throughput, low-latency microservices and backend processing.
- Redis (Memorystore): Provides regional pub/sub messaging for sub-second consent revocation.
- PostgreSQL & Cloud Storage: Used for transactional data and immutable WORM audit logging.
- ArgoCD: Implements regional GitOps deployments to strictly enforce data residency.
- OpenTelemetry: Used for distributed tracing and sub-second latency monitoring.

## Rationale
This architecture guarantees GDPR and HIPAA compliance by isolating regional data infrastructure and maintaining immutable audit ledgers. Furthermore, it achieves a strict 1-second consent revocation SLA using regional gRPC and Redis pub/sub messaging without violating data residency boundaries.