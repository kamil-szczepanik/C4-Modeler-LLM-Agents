## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and AI symptom checking for patients across the EU and US. The architecture enforces strict regional data residency, HIPAA/GDPR compliance, and high availability on Google Cloud Platform.

## Key Elements
- Patients and Clinicians (Users)
- Web & Mobile App (Flutter / TypeScript)
- API Gateway (Google Cloud API Gateway)
- Core Services Container (Spring Boot / Java)
- AI Symptom Checker Container (Python / FastAPI)
- Integration Service Container (Node.js / TypeScript) with internal components: Prescription Router, EU/US E-Prescription Adapters, Outbox Event Processor, Audit & Telemetry Interceptor, and DLQ Manager
- Video Media Server (LiveKit / WebRTC)
- Cloud SQL PostgreSQL, Cloud Storage, and Cloud Pub/Sub
- EU National E-Prescription Gateways and US Pharmacy Networks

## Relationships
- Web & Mobile App -> API Gateway: Routes client requests via HTTPS / WSS
- API Gateway -> Core Services Container: Forwards authenticated API requests via gRPC
- Core Services Container -> Integration Service Container: Dispatches e-prescription events via region-isolated Cloud Pub/Sub topics
- Integration Service Container -> EU National E-Prescription Gateways: Sends e-prescription data via REST / SOAP with mTLS
- Integration Service Container -> US Pharmacy Networks: Sends e-prescription data via REST / HL7 FHIR over TLS
- DLQ Manager -> Core Services Container: Publishes permanent dispatch failure notifications via Cloud Pub/Sub

## Technology Stack
- Google Cloud Platform (`europe-west3`, `us-central1`): Chosen for regional isolation and compliance capabilities.
- Node.js / TypeScript: Powers the Integration Service Container for asynchronous event handling.
- Spring Boot / Java: Implements core business logic in the Core Services Container.
- LiveKit / WebRTC: Delivers real-time video consultations supporting degraded network modes.
- PostgreSQL & Cloud Pub/Sub: Manages persistent relational data and decoupled asynchronous messaging.
- Terraform: Automates infrastructure provisioning and regional parity.

## Rationale
Regionally isolated container deployments and field-level KMS encryption strictly enforce GDPR and HIPAA data residency constraints without crossing borders unlawfully. Decoupled asynchronous messaging via Cloud Pub/Sub and dedicated DLQ management guarantee high availability and accountability for critical e-prescription workflows.