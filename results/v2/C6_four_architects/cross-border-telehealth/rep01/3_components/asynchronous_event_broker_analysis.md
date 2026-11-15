## Overview
Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture uses GCP regions to strictly enforce regional data residency and compliance.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- External Systems: National Pharmacies, National EHR Gateways, Payment Gateways (Stripe), Notification Providers (Twilio/Firebase)
- API Gateway & Consent Container (Envoy / Google Cloud Endpoints, Open Policy Agent)
- Core Telehealth Backend (Node.js / Go)
- Video Consultation Service (WebRTC / Janus Media Server on GCE MIGs)
- AI Symptom Checker (Python / FastAPI)
- Interoperability Adapter (Java / Spring Boot)
- Asynchronous Event Broker (GCP Pub/Sub with regional EU/US topics, Schema Registry, Event Flow Router, and DLQ Manager)
- Dedicated Audit & Logging Container (Fluentbit / OpenTelemetry)
- Regional Databases (Cloud SQL PostgreSQL, Cloud Storage, Cloud Firestore)

## Relationships
- AI Symptom Checker -> Schema-Validated EU/US Topics: Publishes structured recommendation events via `gcp-pubsub-client` [gRPC]
- Core Telehealth Backend -> Asynchronous Event Broker: Publishes and consumes asynchronous events [gRPC/HTTPS]
- Asynchronous Event Broker (Event Flow Router) -> Interoperability Adapter: Pushes filtered e-prescription events [gRPC]
- Dedicated Audit & Logging Container -> EU/US Event Bus: Subscribes via push subscriptions to forward telemetry [HTTPS]
- Asynchronous Event Broker (DLQ Retry Manager) -> Regional Cloud Storage: Archives unprocessable event payloads [gRPC]

## Technology Stack
- Google Cloud Platform (GCP): Primary cloud provider spanning `europe-west3` and `us-central1` for geographic isolation
- GCP Pub/Sub: Asynchronous event broker with integrated Schema Registry for payload validation
- WebRTC / Janus Media Server: Powers real-time video consultations in bandwidth-constrained environments
- PostgreSQL / Firestore / Cloud Storage: Regional persistence layers enforcing data residency
- Node.js, Go, Python, Java: Microservices runtime environments per container specification

## Rationale
The architecture strictly confines EU health data to `europe-west3` and US data to `us-central1` to satisfy GDPR and HIPAA mandates. Attribute-based event routing and schema validation ensure resilience for low-bandwidth connections and complete audit traceability for AI medical outputs.