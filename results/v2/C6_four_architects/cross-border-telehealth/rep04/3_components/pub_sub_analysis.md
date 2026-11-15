## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency while ensuring regulatory compliance, high availability, and traceable AI recommendations.

## Key Elements
- Patients and Clinicians (Users)
- React Web Application, Flutter Mobile App
- Google Cloud Global HTTPS Load Balancer, Cloud Armor, Cloud DNS (Ingress Layer)
- Google Cloud API Gateway
- Core Telehealth Service (Node.js / Go)
- Video Consultation Service (LiveKit)
- AI Symptom Checker Service (Python / FastAPI)
- Consent Management Service (Go)
- E-Prescription & Interoperability Gateway (Node.js / TypeScript, Java / Spring Boot FHIR Adapter)
- Audit & Compliance Logging Service (Go)
- Google Cloud Pub/Sub (Async Event Processing)
- Google Cloud SQL for PostgreSQL (Database)

## Relationships
- Web/Mobile Apps -> Ingress Layer: HTTPS / WSS
- Ingress Layer -> API Gateway: HTTP/2 over TLS
- API Gateway -> Core & Microservices: gRPC / REST over TLS
- Microservices -> Google Cloud Pub/Sub: Cloud Pub/Sub API over TLS
- Microservices -> Google Cloud SQL: PostgreSQL wire protocol over TLS
- Video Consultation Service -> LiveKit: WebRTC

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Enforces regional data residency for GDPR and HIPAA compliance.
- Google Cloud Pub/Sub: Powers asynchronous event-driven messaging with region-isolated topics.
- LiveKit: Handles real-time video streaming with degraded mode support for unstable connections (<300 kbit/s).
- Python / FastAPI: Implements the AI symptom checker with model version tracking.
- Java Spring Boot & Node.js: Implements HL7 FHIR adapters and e-prescription integrations.

## Rationale
The GCP multi-region architecture isolates EU and US health data to satisfy strict GDPR and HIPAA residency requirements. Asynchronous eventing via Cloud Pub/Sub with decoupled microservices ensures high resilience, auditability, and interoperability across diverse regional healthcare standards.