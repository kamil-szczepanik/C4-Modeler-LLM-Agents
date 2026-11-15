## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture enforces strict regional data isolation to comply with GDPR and HIPAA mandates.

## Key Elements
- **Patients and Clinicians**: End-users accessing the platform globally.
- **API Gateway / Envoy (Go)**: Entry point routing incoming traffic.
- **Video Consultation Service (Node.js / WebRTC SFU / Mediasoup)**: Manages real-time video sessions with Coturn relay servers.
- **Clinical Core & E-Prescription Service (Java / Spring Boot)**: Handles clinical records and prescription workflows.
- **AI Symptom Checker Service (Python / FastAPI)**: Evaluates patient symptoms and recommends care urgency.
- **Consent & Identity Management Service (Java / Spring Security)**: Manages authentication and user data-sharing permissions.
- **Notification & Pharmacy Integration Service (Go)**: Handles messaging and external pharmacy communications.
- **Data Storage Containers**: Relational Data Store (Cloud SQL PostgreSQL), Object Store (Cloud Storage), Event Bus (Cloud Pub/Sub), and Audit & Traceability Store (Append-Only PostgreSQL).
- **External Systems**: External Pharmacy Gateways, Identity Providers (IdP), Payment Gateways (Stripe).

## Relationships
- **Clinical Core & E-Prescription Service -> Relational Data Store**: Reads and writes structured data via PostgreSQL Wire Protocol (TLS 1.3) using CMEK.
- **AI Symptom Checker Service -> Relational Data Store**: Reads clinical context and writes session states via PostgreSQL Wire Protocol (TLS 1.3).
- **AI Symptom Checker Service -> Audit & Traceability Store**: Logs inputs and model versions via PostgreSQL Wire Protocol (TLS 1.3).
- **Consent & Identity Management Service -> Relational Data Store**: Stores identity and consent data via PostgreSQL Wire Protocol (TLS 1.3).
- **Notification & Pharmacy Integration Service -> Data Storage**: Publishes and consumes events via Cloud Pub/Sub (gRPC/HTTPS).
- **Video Consultation Service -> Coturn Relay Server**: Handles real-time media streams via WebRTC/TURN/STUN.

## Technology Stack
- **Cloud Provider**: Google Cloud Platform (GCP) in regions `europe-west3` and `us-central1` for data residency compliance.
- **Databases**: Cloud SQL (PostgreSQL) for relational data and tamper-evident audit logs.
- **Storage**: Cloud Storage with signed URLs for unstructured medical assets and binary transfers.
- **Messaging**: Cloud Pub/Sub for asynchronous event-driven integration.
- **Security**: TLS 1.3 for data in transit; Customer-Managed Encryption Keys (CMEK) partitioned via `europe-west3-kms` and `us-central1-kms`.

## Rationale
This architecture guarantees strict regional data residency by isolating EU and US workloads, satisfying GDPR and HIPAA requirements. The modular component design and asynchronous event bus ensure system availability even under constrained network conditions.