## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and high availability over unstable connections.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Web/Mobile Frontend App (Flutter/React)
- API Gateway (Envoy/GCP API Gateway)
- Core Telehealth Service (Go/Spring Boot)
- WebRTC SFU Video Service (Mediasoup)
- AI Inference Service (Python/FastAPI)
- E-Prescription Integrator (Node.js)
- FHIR Event Bus container (GCP Pub/Sub) containing Event Router, FHired Schema Validator, Audit Ledger Sink, and Regional Isolation Enforcer components
- Regional Data Stores (GCP Cloud SQL/Spanner in `europe-west3` and `us-central1`)
- External National E-Prescription Networks (EU) and Pharmacy Systems (US)

## Relationships
- Core Telehealth Service -> Event Router: Publishes regional FHIR bundles [gRPC over GCP Pub/Sub]
- Event Router -> Regional Isolation Enforcer: Validates residency before queuing [Internal function call]
- Event Router -> Audit Ledger Sink: Forwards event metadata for tracing [Internal gRPC]
- FHIR Event Bus -> E-Prescription Integrator: Consumes e-prescription events [GCP Pub/Sub (HL7 FHIR)]

## Technology Stack
- GCP (regions `europe-west3` and `us-central1`): Enforces regional data residency per compliance constraints.
- Go and Python/FastAPI: High-performance backend services and AI inference.
- GCP Pub/Sub with HL7 FHIR: Asynchronous, standards-compliant event messaging.
- Mediasoup WebRTC SFU: Enables real-time video consultations in degraded bandwidth modes.

## Rationale
This architecture enforces strict regional data isolation between the EU and US to satisfy GDPR and HIPAA mandates. Using decoupled microservices, regional event routing, and HL7 FHIR compliance guarantees security, auditability, and interoperability across borders.