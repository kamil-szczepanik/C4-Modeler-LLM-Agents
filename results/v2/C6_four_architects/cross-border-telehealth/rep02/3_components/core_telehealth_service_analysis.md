## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The architecture enforces strict regional data residency, regulatory compliance, and resilience for low-bandwidth connections.

## Key Elements
- Patients and Clinicians (Users)
- Web & Mobile Clients (React / React Native)
- API Gateway & Routing (Kong / GCP API Gateway)
- Core Telehealth Service (Java / Spring Boot container containing 8 internal components: Consultation Session Manager, Prescription Orchestrator, Data Residency Guard, Symptom Checker Gateway, Consent Enforcement Interceptor, Degraded Mode Adaptor, Regional Routing Router, Audit Event Dispatcher)
- WebRTC Media Broker (Node.js / Mediasoup)
- AI Symptom Checker Service (Python / FastAPI)
- FHIR & E-Prescription Integration Service (Python / Java)
- Consent & Audit Logging Service (Go)
- Messaging (Cloud Pub/Sub)
- Databases (Cloud SQL PostgreSQL, Cloud Storage)
- External Systems (Global Media Relay Network, National E-Prescription Gateways EU, US Pharmacy Networks, Identity & Consent Providers, AI Model Registry & Inference Provider)

## Relationships
- API Gateway & Routing -> Core Telehealth Service: Routes ingress traffic with region context headers [gRPC]
- Consultation Session Manager -> WebRTC Media Broker: Initiates room allocation and manages video sessions [gRPC, WebSockets/UDP]
- Prescription Orchestrator -> FHIR & E-Prescription Integration Service: Dispatches regional e-prescription payloads [gRPC]
- Prescription Orchestrator -> Messaging (Cloud Pub/Sub): Publishes asynchronous e-prescription events [Protobuf over gRPC]
- Symptom Checker Gateway -> AI Symptom Checker Service: Submits symptom payloads with metadata tracking [gRPC]
- Audit Event Dispatcher -> Messaging (Cloud Pub/Sub): Publishes cryptographically signed audit payloads [gRPC / Protobuf]
- Data Residency Guard -> Cloud SQL PostgreSQL: Enforces region-locked connection strings (`europe-west3` / `us-central1`) [JDBC/TLS]

## Technology Stack
- Java / Spring Boot: Core Telehealth Service implementation using modular monolith boundaries, Spring Application Events, and Spring Security aspects for consent enforcement
- GCP (regions `europe-west3` and `us-central1`): Target cloud provider for strict data residency and VPC Service Controls
- gRPC / Protobuf: Primary protocol for high-performance internal microservice and container communication
- Cloud Pub/Sub: Asynchronous messaging for event-driven workflows and audit logging
- Cloud SQL PostgreSQL: Region-isolated relational storage utilizing thread-local regional context

## Rationale
This architecture uses GCP VPC Service Controls, strict data residency guards, and regional routing to satisfy rigorous GDPR and HIPAA compliance mandates. Additionally, the inclusion of a dedicated Degraded Mode Adaptor and audit event streaming ensures high availability in rural areas and complete traceability for medical AI outputs.