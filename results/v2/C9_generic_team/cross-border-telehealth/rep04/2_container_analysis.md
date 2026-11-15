## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. It ensures strict data residency, regulatory compliance, and resilient operations over unstable networks.

## Key Elements
- Patients (EU and US) and Licensed Clinicians
- Region-Isolated API Gateways and Backend Services (`europe-west3`, `us-central1`)
- WebRTC SFU Video Streaming Containers
- AI Symptom Checker & Immutable Traceability Logging Service
- Interoperability Adapter Containers (HL7 FHIR / EU e-prescription standards)
- Regional GCP Pub/Sub Integration Bus
- Dedicated Consent Evaluation Service
- Envoy API Rate Limiting and Circuit Breaker Sidecars
- Cloud SQL Auth Proxy & OpenTelemetry Observability Agents

## Relationships
- Patients & Clinicians interact with Regional API Gateways via HTTPS/WebRTC
- Backends communicate with regional GCP Cloud SQL via Cloud SQL Auth Proxy
- Core Services publish e-prescription events via regional GCP Pub/Sub to Adapter Containers
- Adapter Containers integrate with Third-Party Pharmacies and National Endpoints using HL7 FHIR and EU standards

## Technology Stack
- Google Cloud Platform (GCP): Multi-region deployment in `europe-west3` and `us-central1` for data residency
- WebRTC Selective Forwarding Units (SFUs): Enables adaptive bitrate video streaming for unstable connections
- GCP Pub/Sub: Asynchronous messaging bus for decoupled third-party integrations
- OpenTelemetry: Distributed tracing and telemetry collection for AI audit logs and video metrics
- Envoy Proxy: Edge rate limiting and DoS protection

## Rationale
This multi-region, containerized architecture strictly enforces GDPR and HIPAA data residency by isolating EU and US workloads while using asynchronous messaging to handle intermittent rural network connectivity. Decoupled adapters and immutable logging sidecars ensure third-party interoperability and EU MDR traceability compliance without compromising core system availability.