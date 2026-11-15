## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict regional data residency, regulatory compliance, and high availability.]

## Key Elements
- Patients (EU/US) & Licensed Clinicians
- Flutter Patient Mobile/Web App
- Clinician Portal (React / Node.js)
- GCP API Gateway (Cloud Endpoints / Envoy)
- Core Telehealth Service (Go / Spring Boot)
- AI Inference Wrapper (Python / FastAPI)
- Pharmacy Integration Gateway (Apache Camel / Spring Integration)
- GCP GKE Regional Clusters (europe-west3, us-central1)
- Cloud SQL PostgreSQL Databases

## Relationships
- Patient App to GCP API Gateway via HTTPS/WSS
- Clinician Portal to GCP API Gateway via HTTPS/WSS with JWT Authentication
- Session Controller to Core Telehealth Service via WSS (WebSocket Secure) for WebRTC signaling
- Prescription Dispatcher to Pharmacy Integration Gateway via gRPC / Protocol Buffers over TLS (mTLS via Envoy sidecar)
- Audit & Traceability Client to AI Inference Wrapper via HTTPS/REST

## Technology Stack
- GCP (europe-west3, us-central1): Target cloud infrastructure ensuring regional data isolation
- GKE & Kubernetes HPA: Container orchestration and autoscaling based on concurrent connections
- React & TypeScript: Frontend framework for low-latency UI rendering
- Node.js & Express: Backend component layer for session and prescription handling
- Go & Spring Boot: High-performance core backend services
- Python & FastAPI: AI inference wrapper for symptom checking
- Cloud SQL PostgreSQL: Regional relational data storage
- OpenTelemetry & GCP Cloud Logging: Distributed tracing and compliance log aggregation

## Rationale
[This architecture enforces GDPR and HIPAA compliance by isolating EU and US workloads into region-specific GKE clusters. Decoupled, stateless container design combined with gRPC, WSS, and Envoy proxies ensures low-latency communication, strict security, and resilience over unstable connections.]