## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and AI symptom checking for patients across the EU and US. The system ensures strict data residency, regulatory compliance, and high availability for rural users.

## Key Elements
- **Patients (EU & US) & Licensed Clinicians**: Primary end-users accessing the platform.
- **Web/Mobile Client**: Flutter / React Native frontend application.
- **API Gateway**: Cloud Endpoints / Envoy routing inbound traffic.
- **Core Telehealth Backend Components**: Prescription Orchestrator (Go), Audit Logging Interceptor (Node.js/Go), and Integration Adapter (Go).
- **External Gateways**: EU National e-Prescription Gateways and US Pharmacy Networks.
- **Infrastructure**: GCP (`europe-west3`, `us-central1`), Cloud SQL PostgreSQL, Cloud Storage, and Cloud Pub/Sub.

## Relationships
- **Web/Mobile Client** -> **API Gateway**: Secure client requests via HTTPS / WebRTC.
- **API Gateway** -> **Prescription Orchestrator**: Internal routing via gRPC.
- **Prescription Orchestrator** -> **Consent Management Container**: Authorization checks via gRPC.
- **Prescription Orchestrator** -> **Cloud Pub/Sub**: Asynchronous event queueing via Pub/Sub Protocol.
- **Integration Adapter** -> **External Gateways**: Regional e-prescription transmission via HTTPS / REST.
- **Components** -> **Cloud SQL PostgreSQL**: Regional persistence using PostgreSQL protocol.

## Technology Stack
- **Go & Node.js**: Chosen for high-throughput microservices and robust middleware handling.
- **GCP (europe-west3, us-central1)**: Selected to enforce regional data residency and compliance.
- **Cloud SQL PostgreSQL**: Utilized for regionally sharded, append-only immutable audit logging.
- **Cloud Pub/Sub**: Deployed with partitioned regional topics for resilient asynchronous messaging.
- **gRPC**: Implemented for low-latency, internal component-to-component communication.

## Rationale
This architecture guarantees strict regional data isolation to satisfy GDPR and HIPAA mandates while supporting asynchronous queueing for rural users with unstable internet. Decomposing the backend into specialized components ensures robust auditability, consent enforcement, and high-performance cross-border healthcare delivery.