## Overview
The Prescription & Record Service is a secure, regionally isolated enterprise container within the Cross-Border Telehealth Platform responsible for processing, translating, and securely dispatching e-prescriptions. It bridges fragmented national e-prescription standards across the EU and US while strictly enforcing data residency and patient consent mandates.

## Key Elements
* Prescription API Controller (Spring MVC)
* FHIR / National Adapter Engine (Spring Integration / Camel)
* Audit & Compliance Logger (Spring AOP)
* Prescription State & Idempotency Manager (Spring Data JPA / Redis)
* External Gateways: National E-Prescription Gateways (EU) and US Pharmacy Networks
* Supporting Services: Consent & Identity Service (Keycloak / PostgreSQL), Regional Pub/Sub (GCP)

## Relationships
* Prescription API Controller -> Consent & Identity Service: Validates patient consent and OAuth 2.0 JWT tokens via gRPC with mTLS
* Prescription API Controller -> Prescription State & Idempotency Manager: Checks and stores idempotency tokens via JDBC and Redis
* FHIR / National Adapter Engine -> Regional Pub/Sub: Publishes asynchronous prescription payloads for decoupled dispatch
* FHIR / National Adapter Engine -> External Gateways: Sends HL7 FHIR and national standard payloads via outbound HTTPS/TLS 1.3 with mutual authentication

## Technology Stack
* Java / Spring Boot: Chosen for robust enterprise integration, security tooling, and ecosystem maturity.
* Spring Integration / Camel: Implements the Strategy pattern for dynamic payload routing across fragmented e-prescription standards.
* GCP Memorystore & Cloud Pub/Sub: Provides high-availability Redis caching for idempotency and asynchronous decoupling for unstable networks.
* GCP Secret Manager & CMEK: Secures mTLS keys, API credentials, and ensures data-at-rest encryption aligned with regional boundaries.

## Rationale
This architecture isolates regional health data in GCP (`europe-west3` and `us-central1`) to satisfy GDPR and HIPAA residency mandates. Asynchronous queuing, idempotency caching, and resilience patterns ensure reliable e-prescription delivery despite unstable rural connectivity and external gateway latency.