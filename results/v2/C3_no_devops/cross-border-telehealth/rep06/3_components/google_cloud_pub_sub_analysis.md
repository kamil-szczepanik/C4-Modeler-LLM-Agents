## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It guarantees regional data residency, regulatory compliance, and high availability over unstable connections.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Web Application & Mobile Apps (Flutter / React)
- Regional API Gateways (Google Cloud API Gateway in `europe-west3`, `us-central1`)
- Core Telehealth Service (Go / Spring Boot)
- Video Mediation Service (Twilio / WebRTC)
- E-Prescription Integrator (Node.js)
- AI Orchestrator & Audit Logger (Python)
- Google Cloud Pub/Sub with Schema Validation (Messaging)
- Cloud SQL for PostgreSQL (PostgreSQL) and Memorystore for Redis (Redis)

## Relationships
- Web/Mobile Apps -> Regional API Gateways: HTTPS / WSS for client traffic
- Core Telehealth Service -> Google Cloud Pub/Sub: Publishes asynchronous domain events [Cloud Pub/Sub API / gRPC]
- E-Prescription Integrator -> Google Cloud Pub/Sub: Publishes e-prescription events [Cloud Pub/Sub API / gRPC]
- AI Orchestrator & Audit Logger -> Google Cloud Pub/Sub: Publishes AI and audit events [Cloud Pub/Sub API / gRPC]
- Core Telehealth Service -> Cloud SQL & Memorystore: Persists operational data and session state [PostgreSQL Wire Protocol / Redis Protocol]

## Technology Stack
- Google Cloud Platform (`europe-west3`, `us-central1`): Target cloud provider ensuring regional separation.
- Google Cloud Pub/Sub with Schema Registry: Asynchronous messaging enforcing Protocol Buffers for structured, compliant event payloads.
- Cloud KMS: Customer-Managed Encryption Keys (CMEK) for cryptographic data separation.
- VPC Service Controls: Prevents public ingress/egress and enforces network perimeters.

## Rationale
Two isolated regional Pub/Sub instances enforce strict GDPR and HIPAA data residency requirements between the EU and US. Protocol Buffers and CMEK encryption ensure data integrity, consent validation, and audit traceability for medical AI outputs.