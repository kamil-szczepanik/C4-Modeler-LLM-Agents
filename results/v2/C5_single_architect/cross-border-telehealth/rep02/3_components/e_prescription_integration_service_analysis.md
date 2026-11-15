## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency and interoperability standards on GCP.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- Web Application & Mobile App (Flutter / React)
- API Gateway (Google Cloud API Gateway / Envoy)
- Core Telehealth Service (Go / Spring Boot)
- AI Symptom Checker Orchestrator (Python / FastAPI)
- E-Prescription Integration Service (Node.js / Java) containing:
  - Prescription Router Component (Node.js / Express)
  - EU National Gateway Adapter Component (Node.js / TypeScript)
  - US HL7 FHIR Adapter Component (Node.js / TypeScript)
  - Audit & Compliance Logger Component
- Media Relay & Signaling Service (WebRTC / LiveKit)
- Cloud SQL PostgreSQL (PostgreSQL) and Memorystore Redis (Redis)
- External Systems: National e-Prescription Gateways (EU) & Pharmacy Systems (US)

## Relationships
- Web & Mobile Apps -> API Gateway: Client requests [HTTPS / WSS]
- API Gateway -> E-Prescription Integration Service: Routes prescription requests [gRPC over GCP VPC]
- Prescription Router -> EU & US Adapters: Dispatches normalized prescription data [In-process function calls]
- Adapters -> National e-Prescription Gateways & Pharmacy Systems: Dispatches prescriptions [REST / SOAP / FHIR via mTLS and HTTPS]
- Adapters -> Cloud Pub/Sub: Emits compliance audit logs [gRPC over VPC]
- E-Prescription Integration Service -> Cloud SQL: Persists local dispatch status [PostgreSQL Wire Protocol via TLS]

## Technology Stack
- Google Cloud Platform (GCP) in `europe-west3` and `us-central1`: Ensures regional data isolation and compliance.
- Node.js / TypeScript & Java: Core runtime for microservices and integration adapters.
- `fhir-kit-client` & `axios`: Protocol clients for US HL7 FHIR REST endpoints and EU XML/SOAP gateways.
- Cloud Pub/Sub: Asynchronous, region-isolated audit logging.
- PostgreSQL & Redis: Relational data storage and caching.

## Rationale
This architecture guarantees strict regional data residency (EU data in `europe-west3`, US data in `us-central1`) to satisfy GDPR and HIPAA. Dedicated regional adapters fulfill diverse interoperability standards (HL7 FHIR and national EU formats) while maintaining verifiable audit logs.