## Overview
[A secure, cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. It enforces regional data residency and compliance using isolated cloud deployments.]

## Key Elements
* Patients & Licensed Clinicians
* Pharmacies & Regional Health Authorities/Payers
* AI Triage Model Provider (GCP Vertex AI)
* Identity & Consent Providers
* Web & Mobile Apps (Flutter/React)
* API Gateway & BFF (Envoy/Go)
* Core Telehealth Service (Java/Spring Boot)
* AI Triage Service (Python/FastAPI)
* Consent & Audit Ledger (PostgreSQL)
* E-Prescription Dispatcher (Go)

## Relationships
* Patients & Licensed Clinicians -> Cross-Border Telehealth Platform (HTTPS/WebRTC)
* Cross-Border Telehealth Platform -> Pharmacies & Regional Health Authorities/Payers (REST / HL7 FHIR)
* Cross-Border Telehealth Platform -> AI Triage Model Provider (Version-pinned inference APIs via mTLS)
* Cross-Border Telehealth Platform -> Identity & Consent Providers (OIDC / SAML)
* API Gateway & BFF -> Core Telehealth Service (gRPC / REST)
* Core Telehealth Service -> E-Prescription Dispatcher (Internal Messaging / gRPC)

## Technology Stack
* GCP (`europe-west3`, `us-central1`): Enforces regional data residency constraints.
* Go: Powers the API Gateway & BFF and E-Prescription Dispatcher for high-performance dispatching.
* Java / Spring Boot: Implements reliable core telehealth business logic.
* Python / FastAPI: Powers the AI Triage Service for local PHI/PII sanitization and model interaction.
* PostgreSQL: Stores consent and audit ledger data secured via Customer-Managed Encryption Keys (CMEK) via Cloud KMS.

## Rationale
[The multi-region GCP architecture guarantees strict compliance with GDPR and HIPAA by ensuring EU and US health data remain in their respective regions. Decoupled microservices with robust idempotency and cryptographic controls ensure reliable, secure cross-border dispatching even over unstable connections.]