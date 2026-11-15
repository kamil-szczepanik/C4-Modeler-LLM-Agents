## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The system ensures strict data residency, privacy compliance (GDPR/HIPAA), and AI output traceability.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- Core Telehealth Backend (Go-based micro-components: Consultation Orchestrator, E-Prescription Workflow, Consent Enforcement Middleware, Symptom Checker Orchestrator, Patient Profile & Consent Manager, Event Dispatcher, Outbox Pattern Handler)
- Video Consultation Service (WebRTC / Janus Media Server on GCE MIGs)
- AI Symptom Checker (Python / FastAPI)
- Interoperability Adapter (Java / Spring Boot)
- Asynchronous Event Broker (GCP Pub/Sub with region-pinned topics)
- Dedicated Audit & Logging Container (Fluentbit / OpenTelemetry)
- Regional Databases (Cloud SQL PostgreSQL, Cloud Storage, Cloud Firestore)
- External Systems: National Pharmacies, National EHR Gateways, Stripe, Twilio/Firebase

## Relationships
- Consultation Orchestrator -> Video Consultation Service: Manages media streams [gRPC]
- E-Prescription Workflow -> Interoperability Adapter: Dispatches national-format payloads [gRPC]
- Symptom Checker Orchestrator -> AI Symptom Checker: Requests urgency recommendations [gRPC]
- Event Dispatcher -> Asynchronous Event Broker: Publishes sanitized domain events to region-pinned topics [gRPC/Protobuf]
- All Components -> Regional Databases: Enforces geo-pinned data storage [PostgreSQL wire protocol]
- Core Telehealth Backend -> Dedicated Audit & Logging Container: Sends audit logs [gRPC]

## Technology Stack
- Core Telehealth Backend: Go for high throughput and low latency micro-components
- Cloud Platform: Google Cloud Platform (GCP regions europe-west3 and us-central1)
- Messaging: GCP Pub/Sub with region-pinned topics and Outbox Pattern for eventual consistency
- Video Streaming: WebRTC and Janus Media Server on GCE MIGs
- Interoperability & Compliance: HL7 FHIR (US), national e-prescription standards (EU), Open Policy Agent for consent

## Rationale
This architecture enforces strict regional data residency by isolating EU and US data through region-pinned databases and message topics, ensuring full GDPR and HIPAA compliance. Furthermore, the Go-based micro-component design with transactional outbox patterns guarantees resilience under unstable network conditions while maintaining EU MDR traceability via immutable audit logs.