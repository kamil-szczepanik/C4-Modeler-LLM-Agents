## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system ensures strict data residency and regulatory compliance for healthcare operations.

## Key Elements
- **Users:** Patient, Clinician
- **External Systems:** External Pharmacies, Identity Providers, Regional Regulatory Systems, National Health and Insurance Systems
- **Containers:** Web Application, Mobile App, Ingress Layer, API Gateway, Core Telehealth Service, Video Consultation Service, AI Symptom Checker Service, Consent Management Service, E-Prescription & Interoperability Gateway, Audit & Compliance Logging Service, Pub/Sub, Cloud SQL
- **Audit Logging Components:** Audit API Handler, Event Consumer Worker, Compliance Sanitizer & Formatter, Log Persistence Engine, Log Integrity Verifier, Regulatory Reporter

## Relationships
- **API Gateway -> Audit & Compliance Logging Service:** Routes requests securely [gRPC over mTLS]
- **Audit API Handler & Event Consumer Worker -> Compliance Sanitizer:** Processes audit payloads [In-memory function calls]
- **Compliance Sanitizer -> Log Persistence Engine:** Forwards sanitized logs [In-memory function calls]
- **Log Persistence Engine -> Log Integrity Verifier:** Validates cryptographic hash chains [In-memory channels / background goroutine]
- **Log Persistence Engine -> Regulatory Reporter:** Fetches logs for reporting [In-memory function calls]
- **Audit & Compliance Logging Service -> Cloud SQL:** Persists and retrieves logs [PostgreSQL Wire Protocol with TLS]
- **Audit & Compliance Logging Service -> Pub/Sub:** Manages asynchronous events [Cloud Pub/Sub API over TLS]
- **Audit & Compliance Logging Service -> Regional Regulatory Systems:** Transmits compliance data [TLS 1.3]

## Technology Stack
- **Go / Fiber & `pgx`:** Powers the Audit & Compliance Logging Service for high-throughput, concurrent log processing.
- **Google Cloud SQL for PostgreSQL:** Provides region-isolated relational storage with append-only semantics.
- **Google Cloud Pub/Sub:** Enables asynchronous, decoupled event ingestion across regions.
- **gRPC over mTLS:** Secures internal service-to-service communications.

## Rationale
The architecture enforces regional data isolation by deploying region-scoped instances in GCP (`europe-west3` and `us-central1`), ensuring GDPR and HIPAA compliance. Cryptographic hash chaining and dedicated compliance components provide the required traceability and auditability for EU MDR.