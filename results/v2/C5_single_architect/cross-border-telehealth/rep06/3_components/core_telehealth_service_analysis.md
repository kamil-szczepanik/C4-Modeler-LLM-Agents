## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and resilience for unstable network connections.

## Key Elements
- **Patients & Clinicians**: End-users accessing telehealth services.
- **Global Load Balancer with Cloud Armor**: Google Cloud Global Load Balancer & Cloud Armor.
- **API Gateway / BFF**: Go, gRPC/REST.
- **Core Telehealth Service (Node.js / TypeScript)**: Decomposed into Profile & Consent Manager, Appointment & Scheduling Engine, Audit Logger, and Sync & State Manager.
- **Video Consultation Service**: Golang / WebRTC SFU (LiveKit).
- **AI Orchestrator**: Python, FastAPI.
- **E-Prescription Integrator**: Java / Spring Boot.
- **Data Storage**: Cloud SQL (PostgreSQL), Cloud Storage, Cloud Bigtable.
- **External Systems**: National Pharmacy Networks (EU) & US Pharmacy Systems, AI Model Provider/LLM API, Third-Party Identity Providers & Payment Gateways.

## Relationships
- **API Gateway / BFF -> Core Telehealth Service Components**: gRPC over mTLS via Istio.
- **Profile & Consent Manager -> Regional Cloud SQL (PostgreSQL)**: TypeORM via SSL with row-level security (RLS).
- **All Internal Components -> Audit Logger**: Asynchronous event publishing via GCP Pub/Sub.
- **Sync & State Manager -> Appointment & Scheduling Engine**: Internal asynchronous message queue.
- **Video Consultation Service -> Patients / Clinicians**: WebRTC for low-bandwidth video (R-06).

## Technology Stack
- **GCP (`europe-west3`, `us-central1`)**: Cloud infrastructure ensuring regional data isolation.
- **Node.js / TypeScript**: Core business logic and service orchestration.
- **Golang**: High-throughput video streaming and WebRTC SFU (LiveKit).
- **Python / FastAPI**: AI orchestration and symptom checker integration.
- **Java / Spring Boot**: Enterprise-grade E-Prescription Integrator.
- **Cloud SQL (PostgreSQL)**: Relational storage utilizing regional partitioning and row-level security.

## Rationale
This architecture enforces GDPR and HIPAA compliance by isolating EU and US health data within regional GCP boundaries. The modular Node.js microservices and resilient sync components ensure uninterrupted care over unstable connections and strict traceability for AI diagnostics.