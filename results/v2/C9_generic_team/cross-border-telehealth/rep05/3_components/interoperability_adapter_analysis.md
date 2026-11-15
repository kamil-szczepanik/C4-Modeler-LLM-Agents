## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients on GCP. It ensures regional data residency, strict regulatory compliance, and robust interoperability across heterogeneous healthcare standards.

## Key Elements
* Interoperability Adapter container (Region-isolated instances in `europe-west3` and `us-central1`)
* Adapter Plugins & Strategy Pattern (Package-per-Country structure for EU standards and US HL7 FHIR)
* Outbox Pattern & Dead Letter Queue (DLQ) workers for asynchronous e-prescription delivery
* Configuration & Feature Flag Service for dynamic hot-reloading and canary deployments
* External entities: Regional Pharmacies, National Standards APIs, AI Symptom Checker

## Relationships
* Interoperability Adapter -> Regional Pharmacies: Sends e-prescriptions via HL7 FHIR [US] and national e-prescription standards [EU]
* Interoperability Adapter -> National Standards APIs: Fetches reference data and submits transactions [REST/gRPC]
* Interoperability Adapter -> Outbox Worker: Persists asynchronous messaging queues for resilient delivery [Managed Cloud SQL / Spanner]
* Interoperability Adapter -> Configuration Service: Dynamically loads country-specific routing and feature flags [gRPC/HTTPS]

## Technology Stack
* Google Cloud Platform (GCP): Target cloud provider utilizing `europe-west3` and `us-central1` for strict data residency
* HL7 FHIR & REST/gRPC: Protocols for US interoperability and external national standards APIs
* OpenTelemetry: Framework for distributed tracing and correlation ID propagation across adapter boundaries
* Pact & OpenAPI: Technologies used for contract-first development and schema validation gates

## Rationale
Region-isolated adapter instances and the Strategy Pattern strictly enforce GDPR and HIPAA data residency while cleanly encapsulating diverse national e-prescription formats. Asynchronous outbox workflows and caching ensure high availability and resilience for patients facing unstable internet connections.