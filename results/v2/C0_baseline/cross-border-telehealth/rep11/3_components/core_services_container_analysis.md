## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture uses a multi-region Google Cloud Platform deployment to enforce strict regional data residency and compliance.

## Key Elements
* Patients (EU and US) and Licensed Clinicians
* API Gateway (Cloud Endpoints / Envoy)
* Core Services Container (Spring Boot / Java) with internal components: Patient Management & Consent, E-Prescription Routing, Clinical Documentation, and Interoperability & Translation
* Identity & Access Management / Consent Service (OAuth2 / OIDC)
* Async Event Broker (Google Cloud Pub/Sub with DLQ)
* Data Storage (Cloud SQL PostgreSQL with CMEK)
* External Pharmacies and Regional Payment Gateways

## Relationships
* API Gateway -> Core Services Container: Routes validated requests via gRPC with mTLS
* Patient Management & Consent Component -> Data Storage: Reads and writes encrypted relational data using CMEK
* E-Prescription Routing Component -> Async Event Broker: Publishes asynchronous prescription events via AMQP/Pub/Sub
* Interoperability & Translation Component -> External Pharmacies: Transmits prescriptions via outbound HTTPS REST/SOAP with mTLS and circuit breaking

## Technology Stack
* Spring Boot / Java: Core business logic container for performance and enterprise ecosystem
* Google Cloud Platform (`europe-west3`, `us-central1`): Enforces regional data separation constraints
* Google Cloud Pub/Sub: Manages reliable asynchronous messaging and dead-letter queues for degraded network resilience
* PostgreSQL with CMEK: Provides encrypted, region-locked relational data storage
* OpenTelemetry & Istio: Enables distributed tracing and mTLS service mesh security

## Rationale
This architecture guarantees strict GDPR and HIPAA compliance by isolating regional data while permitting cross-border care through verified patient consent. Additionally, it ensures high availability and accountability for rural users via asynchronous queuing and immutable audit logging.