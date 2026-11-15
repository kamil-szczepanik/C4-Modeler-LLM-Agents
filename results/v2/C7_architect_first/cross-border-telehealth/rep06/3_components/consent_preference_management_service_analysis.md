## Overview
- Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients on GCP.
- Core architecture enforces strict GDPR and HIPAA compliance, regional data residency, and real-time consent management via dedicated microservices.

## Key Elements
- Patients and Licensed Clinicians (Users)
- API Gateway (Cloud Armor, Cloud Load Balancing)
- Patient PWA & Clinician Dashboard Frontends (React, Cloud Storage, Cloud CDN)
- Core Telehealth Backend (Node.js, Express)
- AI Symptom Checker Service (Python, FastAPI)
- Video Media Router (Mediasoup SFU)
- Consent & Preference Management Service (Node.js, Express)
- Consent API Controller, Consent Evaluation Engine, Audit Publisher Component, Consent Cache Manager, Consent Data Access Repository
- Data Tier (Cloud SQL PostgreSQL, Cloud Storage, GCP Memorystore Redis, GCP Pub/Sub, Cloud KMS)

## Relationships
- Patient PWA / Clinician Dashboard -> API Gateway: HTTPS / REST / WebSockets
- API Gateway -> Consent & Preference Management Service: gRPC / mTLS
- Consent API Controller -> Consent Evaluation Engine: In-memory function calls [TypeScript]
- Consent Evaluation Engine -> Consent Cache Manager: TCP / Redis Protocol (TLS)
- Consent Evaluation Engine -> Audit Publisher Component: Asynchronous dispatch [GCP Pub/Sub SDK]
- Consent Evaluation Engine -> Consent Data Access Repository: Parameterized SQL [TLS 1.3 / IAM Auth]
- Audit Publisher Component -> GCP Pub/Sub: HTTPS / TLS 1.3

## Technology Stack
- Node.js & Express: Lightweight, high-throughput runtime for backend services.
- GCP Memorystore (Redis): In-memory caching layer for active consent states to achieve sub-millisecond evaluation SLAs.
- Cloud SQL PostgreSQL: Regional relational data store enforcing strict EU (`europe-west3`) and US (`us-central1`) data residency.
- GCP Pub/Sub: Resilient message transport ensuring at-least-once durable delivery for immutable audit logs.
- Cloud KMS: Cryptographic key management for encrypting cached patient consent tokens at rest.
- OpenTelemetry: Distributed tracing standard for monitoring evaluation SLAs across gRPC boundaries.

## Rationale
- The architecture guarantees strict regional data isolation to comply with GDPR and HIPAA mandates while utilizing caching and managed GCP services to maintain sub-50ms consent evaluation latencies. Resilient event-driven auditing and encryption-at-rest ensure full accountability and security for cross-border health data access.