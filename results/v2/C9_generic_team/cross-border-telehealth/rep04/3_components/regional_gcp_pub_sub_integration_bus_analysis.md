## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture uses a multi-region deployment on GCP to enforce strict data residency and compliance mandates.

## Key Elements
- Patients (EU and US) and Licensed Clinicians
- Region-Isolated API Gateways and Backend Services (GCP, Envoy Proxy, REST/gRPC)
- Regional GCP Pub/Sub Integration Bus (`europe-west3` and `us-central1`)
- Interoperability Adapter Containers (HL7 FHIR, EU e-prescription standards)
- AI Symptom Checker & Immutable Traceability Logging Service (Python, OpenTelemetry)
- Dedicated Consent Evaluation Service (Microservice, Policy Engine)
- WebRTC SFU Video Streaming Containers
- Third-Party Pharmacies and National E-Prescription Endpoints

## Relationships
- Region-Isolated API Gateways -> Regional GCP Pub/Sub Integration Bus: Publishes e-prescription and domain events [GCP Pub/Sub]
- Regional GCP Pub/Sub Integration Bus -> Interoperability Adapter Containers: Triggers adapter processing for prescription dispatch [GCP Pub/Sub]
- Backend Services -> Regional GCP Pub/Sub Integration Bus: Publishes events with strict regional topic segregation and W3C trace context [GCP Pub/Sub, OpenTelemetry]

## Technology Stack
- GCP Pub/Sub: Asynchronous messaging bus with strict regional topic segregation and regional CMEK scoping to satisfy GDPR and HIPAA.
- Protocol Buffers & GCP Schema Validation: Enforces strict schema registry and backward-compatible event evolution.
- OpenTelemetry & W3C Traceparent: Maintains unbroken distributed tracing across asynchronous message boundaries.
- GCP IAM & Cloud SQL Auth Proxy: Enforces least-privilege regional service accounts and secure database connections.

## Rationale
This architecture ensures strict regional data residency by isolating Pub/Sub topics and encryption keys per region, preventing cross-border data leakage. It guarantees high availability and auditability through robust message retry, schema validation, and end-to-end distributed tracing.