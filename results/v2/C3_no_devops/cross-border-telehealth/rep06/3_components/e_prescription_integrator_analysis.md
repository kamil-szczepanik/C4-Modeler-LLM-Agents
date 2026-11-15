## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict regional data residency, regulatory compliance, and high availability over unstable connections.

## Key Elements
- Patients and Licensed Clinicians
- Web Application & Mobile Apps (Flutter / React)
- Regional API Gateways (Google Cloud API Gateway in `europe-west3`, `us-central1`)
- E-Prescription Integrator (Node.js) with four internal components: Prescription Transformation Engine, Gateway Adapter Client, Status Polling & Event Handler, and Resilience & Queue Manager
- Cloud SQL for PostgreSQL (PostgreSQL) and Memorystore for Redis (Redis)
- Google Cloud Pub/Sub
- Local Pharmacies and EU National E-Prescription Networks

## Relationships
- E-Prescription Integrator -> Cloud SQL for PostgreSQL: Fetches encrypted payloads on-demand [PostgreSQL Wire Protocol over TLS]
- Resilience & Queue Manager -> Memorystore for Redis: Buffers reference IDs and state metadata [Redis Protocol over TLS]
- Status Polling & Event Handler -> Google Cloud Pub/Sub: Publishes fulfillment events [Cloud Pub/Sub API]
- Status Polling & Event Handler -> Regional API Gateways: Broadcasts transmission state changes [Server-Sent Events / WebSockets with short-lived JWTs]
- Gateway Adapter Client -> Local Pharmacies & EU National Networks: Transmits e-prescriptions [HL7 FHIR / REST / SOAP over HTTPS with mTLS]

## Technology Stack
- Node.js / TypeScript: Implements the E-Prescription Integrator for asynchronous processing and integration flexibility.
- BullMQ / Redis (Memorystore): Manages queuing and retries for transient network failures.
- Google Cloud SQL (PostgreSQL): Stores encrypted clinical data regionally with CMEK protection.
- Google Cloud Pub/Sub: Decouples status tracking and event-driven communication.
- GCP KMS: Enforces regional encryption-at-rest keys for GDPR and HIPAA data residency.

## Rationale
This architecture guarantees strict regional data isolation between `europe-west3` and `us-central1` using regional CMEK encryption and segregated databases. It ensures resilient delivery of e-prescriptions over unstable rural connections through decoupled queuing, status tracking, and automated retries.