## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system enforces strict regional data residency and GDPR/HIPAA compliance via isolated GCP cloud regions.

## Key Elements
* Patients (EU / US), Licensed Clinicians, Platform Administrator / Compliance Officer
* Regional API Gateways (Kong / GCP API Gateway)
* Consent Management Service (Go / Node.js)
* Internal Components: Consent API Controller, Consent Policy Engine, Consent Audit Logger, Consent Event Dispatcher, Template Resolution Sub-component
* Regional Cloud Spanner, Regional BigQuery, Regional Pub/Sub

## Relationships
* Regional API Gateways -> Consent API Controller: Forwards consent requests [gRPC over mTLS]
* Consent API Controller -> Consent Policy Engine: Evaluates consent rules [In-process function call]
* Consent Policy Engine -> Consent Audit Logger: Emits compliance audit trails [Async channel / gRPC]
* Consent Policy Engine -> Regional Cloud Spanner: Persists consent tokens [Cloud Spanner Go Client / gRPC over mTLS]
* Consent Policy Engine -> Consent Event Dispatcher: Triggers revocation events [In-process]
* Consent Event Dispatcher -> Regional Pub/Sub: Publishes token invalidation events [Pub/Sub API]

## Technology Stack
* Go: Used for Consent Management Service components for low memory footprint and high concurrency
* GCP Cloud Spanner: Regional transactional data storage enforcing strict data residency boundaries
* GCP BigQuery: Immutable, hash-chained audit logging for HIPAA/GDPR accountability
* Regional Pub/Sub: Event-driven instant revocation messaging with Dead Letter Queues
* SPIFFE/SPIRE: Secure inter-component mTLS authentication within GKE clusters

## Rationale
The microservices architecture with regional isolation guarantees that EU and US health data remain strictly within `europe-west3` and `us-central1`. Decoupled event-driven revocation ensures immediate security enforcement while maintaining sub-50ms latency SLAs for cross-border operations.