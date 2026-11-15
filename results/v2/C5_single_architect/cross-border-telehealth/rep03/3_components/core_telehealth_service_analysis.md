## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The architecture enforces strict regional data residency and compliance using GCP across `europe-west3` and `us-central1`.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Web/Mobile Frontend App (Flutter/React)
- API Gateway (Envoy/GCP API Gateway)
- Core Telehealth Service (Go/Spring Boot container containing Consultation Manager, Consent & Privacy Enforcement, Prescription Coordinator, and Symptom Assessment Logger components)
- WebRTC SFU Video Service (Mediasoup)
- AI Inference Service (Python/FastAPI)
- E-Prescription Integrator (Node.js)
- FHIR Event Bus (GCP Pub/Sub)
- Regional Data Stores (GCP Cloud SQL/Spanner)
- National E-Prescription Networks (EU) and Pharmacy Systems (US)

## Relationships
- API Gateway -> Core Telehealth Service: Routes API requests [gRPC]
- API Gateway -> Symptom Assessment Logger: Submits symptom check requests [gRPC]
- Core Telehealth Service -> WebRTC SFU Video Service: Establishes video sessions [WebRTC/UDP]
- Core Telehealth Service -> FHIR Event Bus: Publishes e-prescription events [GCP Pub/Sub (HL7 FHIR)]
- Core Telehealth Service -> Regional Data Stores: Reads and writes regional data [SQL]
- Consultation Manager -> Consent & Privacy Enforcement: Validates patient consent [In-memory function call]
- Symptom Assessment Logger -> Regional Data Stores: Persists immutable audit logs [SQL]

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Ensures regional data residency for EU and US compliance.
- Go / Spring Boot: Chosen for the Core Telehealth Service to deliver high concurrency and low latency.
- Mediasoup: SFU Video Service ensuring degraded mode operation for unstable connections below 300 kbit/s.
- GCP Pub/Sub: Event bus handling HL7 FHIR messaging and e-prescription distribution.
- GCP Cloud SQL/Spanner: Regional data stores enforcing strict EU/US data isolation.

## Rationale
This architecture uses regional GCP deployments and isolated data stores to satisfy strict GDPR and HIPAA data residency mandates. Furthermore, Domain-Driven Design components in Go and dedicated audit logging ensure high availability, traceability for EU MDR compliance, and interoperability across regions.