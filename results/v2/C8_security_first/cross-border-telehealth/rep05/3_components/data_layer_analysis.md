## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and offline-first availability.

## Key Elements
- Patients (EU & US), Licensed Clinicians, Compliance Officers
- Frontend Client Apps (Flutter)
- API Gateway / BFF (Envoy / gRPC-Web)
- Video Consultation Service (WebRTC / SFU - Mediasoup)
- AI Symptom Checker Container (Python / FastAPI)
- E-Prescription Integration Service (Node.js / Express)
- Consent & Policy Engine (Opa / Go)
- Data Layer (Google Cloud SQL / PostgreSQL, Cloud Bigtable, Cloud Memorystore / Redis, Cloud Pub/Sub, Cloud KMS)

## Relationships
- Frontend Client Apps -> API Gateway / BFF: Client requests [HTTPS / gRPC-Web, TLS 1.3]
- API Gateway / BFF -> Microservices (Video, AI, E-Prescription, Consent): Internal routing [gRPC, mTLS]
- Consent & Policy Engine -> Data Layer: Access validation [PostgreSQL protocol, mTLS]
- Microservices -> Regional Relational Stores: Data persistence [PostgreSQL protocol, mTLS]
- Regional Relational Stores -> Pub/Sub Notification Dispatcher: CDC Event stream [gRPC]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider for scalable infrastructure
- regions europe-west3 & us-central1: Enforces strict data residency (EU data stays in EU, US data in US)
- Cloud SQL (PostgreSQL) with Row-Level Security: Core transactional storage and fine-grained access control
- Cloud Bigtable / Append-Only Tables: High-throughput, immutable storage for AI audit logs and consent history
- Cloud Memorystore (Redis) & Cloud Pub/Sub: Transient session caching, offline sync buffering, and CDC event streaming
- Cloud KMS & IAM: Customer-managed encryption keys, envelope encryption, and dynamic short-lived database credentials

## Rationale
This architecture guarantees strict regional data isolation to comply with GDPR and HIPAA mandates. It leverages purpose-built storage and caching components to ensure audit traceability, cryptographic erasure, and reliable performance even for rural users with unstable internet.