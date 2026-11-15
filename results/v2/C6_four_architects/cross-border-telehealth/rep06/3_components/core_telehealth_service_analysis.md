## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict regional data residency, GDPR/HIPAA compliance, and robust performance on unstable rural internet connections.

## Key Elements
- **Consultation Manager (Go)**: Orchestrates video session lifecycles.
- **Prescription Engine (Go)**: Manages regional e-prescription routing.
- **Consent & Policy Enforcement Engine (Go)**: Enforces region-specific data residency and explicit patient consents.
- **Audit Logger (Go)**: Emits structured audit trails.
- **Symptom Checker Orchestrator (Go)**: Coordinates AI triage assessments and model versioning.
- **Degraded Mode Handler (Go)**: Adapts network quality for low-bandwidth connections.
- **Video Streaming Service**: mediasoup SFU on GCP Compute Engine with TURN/STUN relay.
- **Datastores**: Cloud SQL PostgreSQL, Memorystore Redis, and Google Cloud BigQuery.

## Relationships
- **Consent & Policy Enforcement Engine** -> **Datastores**: Executes region-isolated queries [PostgreSQL and Redis protocols].
- **Consultation Manager** -> **Video Streaming Service**: Controls media sessions [gRPC].
- **Symptom Checker Orchestrator** -> **AI Symptom Checker Service (Python / FastAPI)**: Triggers triage analysis [gRPC].
- **Prescription Engine** -> **Integration Service (Node.js)**: Dispatches regional e-prescription payloads [gRPC].
- **Internal Components** -> **Audit Logger**: Dispatches immutable tracing payloads [Buffered Go Channels].

## Technology Stack
- **Go**: Chosen for high performance and concurrency in core telehealth orchestration.
- **Python / FastAPI**: Used for the AI Symptom Checker Service to leverage machine learning ecosystem libraries.
- **mediasoup SFU on GCP Compute Engine**: Selected for scalable, low-latency video streaming.
- **Google Cloud API Gateway with Open Policy Agent (OPA)**: Implemented for secure, policy-driven API routing.
- **Cloud SQL PostgreSQL & Memorystore Redis**: Utilized for transactional data storage and caching with strict regional isolation.

## Rationale
This architecture uses GCP multi-region deployment (`europe-west3` and `us-central1`) with isolated datastores to satisfy strict GDPR and HIPAA data residency mandates. The modular Go component design within the Core Telehealth Service ensures high availability, medical device traceability, and graceful degradation for rural connections under 300 kbit/s.