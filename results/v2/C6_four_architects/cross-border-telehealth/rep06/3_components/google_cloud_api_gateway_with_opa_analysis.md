## Overview
Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It runs on GCP (`europe-west3` and `us-central1`) ensuring strict regional data residency and regulatory compliance.

## Key Elements
- Patients and Clinicians (Users)
- Web & Mobile Apps (React / React Native)
- Google Cloud API Gateway with OPA (Google Cloud API Gateway, Open Policy Agent)
- Core Telehealth Service (Go)
- AI Symptom Checker Service (Python / FastAPI)
- Video Streaming Service (mediasoup SFU on GCP Compute Engine)
- Integration Service (Node.js)
- Datastores (Cloud SQL PostgreSQL, Memorystore Redis, Google Cloud BigQuery, Cloud Storage)
- API Gateway Components: API Router, Context Extractor, Rate Limiting Component, Authorization Engine (OPA), Audit Logger (Fluentbit sidecar)

## Relationships
- Web & Mobile Apps -> Google Cloud API Gateway with OPA: Sends requests and media [HTTPS, WSS, WebRTC/UDP]
- API Router -> Rate Limiting Component: Checks quotas [gRPC / Memorystore Redis]
- API Router -> Context Extractor: Passes raw requests [In-memory]
- Context Extractor -> Authorization Engine (OPA): Forwards claims [gRPC]
- Authorization Engine -> Audit Logger: Emits decision logs [Async IPC / Fluentd]
- Google Cloud API Gateway -> Backend Services (Core/AI/Integration): Routes traffic [gRPC with JWT/Token propagation]
- Google Cloud API Gateway -> Google Cloud API Gateway: Cross-region access [Federated mTLS over HTTPS]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider for regional isolation in `europe-west3` and `us-central1`
- Open Policy Agent (OPA): Enforces dynamic purpose-based patient consent via Rego policies
- Google Cloud API Gateway: Manages API routing, TLS termination, and mTLS enforcement
- Memorystore Redis: Backs the rate-limiting component for traffic throttling
- Fluentbit: Sidecar component for forwarding structured audit logs to BigQuery

## Rationale
This architecture enforces GDPR and HIPAA data residency constraints by isolating processing per region while allowing secure, consented cross-region access. The component breakdown within the API gateway ensures low-latency authorization, auditability, and resilient routing for unstable connections.