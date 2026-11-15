## Overview
Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. Ensures strict regional data residency and compliance via GCP regions.

## Key Elements
- Patients and Clinicians (Users)
- API Gateway / Ingress Controller Containers (Google Cloud Platform Ingress / Envoy)
- Local Async Event Bus / Queue Containers (EMQX/VerneMQ, MQTT, SQLite/RocksDB)
- Stateless Core Application Containers
- Video Streaming Gateway Containers (WebRTC, TURN/STUN)
- AI Inference & Audit Proxy Containers (Python, gRPC)
- FHIR Translation Adapter and National E-Prescription Adapter Containers
- Configuration and Secrets Management Sidecars (GCP Secret Manager)
- Observability & Telemetry Exporter Sidecars (OpenTelemetry)

## Relationships
- Patients/Clinicians -> API Gateway / Ingress Controller Containers [HTTPS / gRPC / WebRTC]
- Local Async Event Bus -> Regional Audit and Compliance Logging Subsystem [MQTT / HTTPS with SHA-256 Checksums]
- Video Streaming Gateway Containers -> Patients/Clinicians [WebRTC]
- Stateless Core Application Containers -> Regional Databases [PostgreSQL / GCP Spanner]

## Technology Stack
- GCP (europe-west3, us-central1): Target cloud provider ensuring regional data residency.
- MQTT & SQLite/RocksDB: Lightweight edge messaging and durable write-ahead-logged storage for unstable rural networks.
- Protocol Buffers: Backward-compatible payload serialization for offline queuing and schema evolution.
- OpenTelemetry: Telemetry export with PII/PHI stripping sidecars.

## Rationale
The architecture combines regional GCP isolation with edge-resilient local queuing to satisfy strict GDPR/HIPAA compliance. Durable local storage, cryptographic validation, and deterministic replay guarantee data integrity and continuous availability for rural users.