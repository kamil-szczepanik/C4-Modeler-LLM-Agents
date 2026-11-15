## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and AI symptom checking for patients across the EU and US. It enforces strict regional data residency, regulatory compliance, and localized interoperability.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Web/Mobile Frontend App (Flutter/React)
- API Gateway (Envoy/GCP API Gateway)
- Core Telehealth Service (Go/Spring Boot)
- WebRTC SFU Video Service (Mediasoup)
- AI Inference Service (Python/FastAPI)
- E-Prescription Integrator (Node.js) containing:
  - FHIR Event Consumer Component
  - Jurisdiction Routing Guard Component
  - US Pharmacy Adapter Component
  - EU National Gateway Adapter Component
  - Prescription Status Tracker Component
- FHIR Event Bus (GCP Pub/Sub)
- Regional Data Stores (GCP Cloud SQL/Spanner in `europe-west3` and `us-central1`)
- External National E-Prescription Networks (EU) and US Pharmacy Systems

## Relationships
- Web/Mobile Frontend App -> API Gateway: Manages requests [HTTPS/REST]
- API Gateway -> Core Telehealth Service: Routes core domain requests [gRPC]
- Core Telehealth Service -> FHIR Event Bus: Publishes prescription events [GCP Pub/Sub (HL7 FHIR)]
- FHIR Event Consumer -> Jurisdiction Routing Guard: Routes event [In-Memory]
- Jurisdiction Routing Guard -> US/EU Adapters: Dispatches regionally compliant payloads [In-Memory]
- US Pharmacy Adapter -> US Pharmacy Systems: Sends prescriptions [HTTPS/REST]
- EU National Gateway Adapter -> National E-Prescription Networks: Sends prescriptions [SOAP/REST with mTLS]
- US/EU Adapters -> Prescription Status Tracker: Reports delivery status [gRPC]

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Ensures regional data residency compliance (GDPR/HIPAA).
- Node.js/TypeScript: Powers the E-Prescription Integrator container and internal components.
- GCP Pub/Sub (HL7 FHIR): Asynchronous messaging and event bus.
- gRPC: High-performance internal service communication.
- HTTPS/REST and SOAP with mTLS: Secure external communication with US pharmacies and EU national networks.

## Rationale
This architecture guarantees strict regional data isolation between `europe-west3` and `us-central1` to satisfy GDPR and HIPAA mandates. It also isolates disparate regional pharmacy integration protocols within modular internal components.