## Overview
[Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture enforces regional data residency on GCP while ensuring regulatory compliance, high availability, and traceability.]

## Key Elements
- Patients (EU and US) and Licensed Clinicians
- Region-Isolated API Gateways and Backend Services (GCP, Envoy Proxy, gRPC/REST)
- AI Symptom Checker & Immutable Traceability Logging Service (Python, OpenTelemetry)
- WebRTC SFU Video Streaming Containers (Adaptive Bitrate Streaming)
- Regional GCP Pub/Sub Integration Bus
- Interoperability Adapters (HL7 FHIR for US, national standards for EU)
- Dedicated Consent Evaluation Service and Cloud SQL Auth Proxy

## Relationships
- Patients/Clinicians -> Region-Isolated API Gateways [HTTPS/WebRTC]
- API Gateways -> AI Symptom Checker & Immutable Traceability Logging Service [gRPC/Internal API]
- AI Symptom Checker Service -> Regional GCP Storage (`europe-west3`, `us-central1`) [Encrypted Storage API]
- API Gateways -> Interoperability Adapters [REST/HL7 FHIR]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider for `europe-west3` and `us-central1` regions enforcing strict data residency.
- Python & OpenTelemetry: Core stack for the AI Symptom Checker and immutable traceability logging container.
- Protocol Buffers & gRPC: Used for strict schema contracts and high-performance internal communication.
- SHA-256 Cryptographic Hashing: Implemented via write-ahead append-only logs for tamper-evident EU MDR accountability.
- CQRS & Circuit Breaker Patterns: Decouples real-time AI inference from logging writes to ensure availability during rural connection drops.

## Rationale
[The multi-region GCP architecture guarantees that EU health data remains in `europe-west3` and US data in `us-central1` to satisfy GDPR and HIPAA. Incorporating CQRS, circuit breakers, local fallback heuristics, and idempotent APIs ensures continuous availability and reliability for patients with unstable rural connections.]