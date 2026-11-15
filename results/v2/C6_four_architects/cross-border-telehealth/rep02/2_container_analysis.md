## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency while ensuring high availability for unstable connections.

## Key Elements
* Web & Mobile Clients (React / React Native)
* API Gateway & Routing (Kong / GCP API Gateway)
* Core Telehealth Service (Java / Spring Boot)
* WebRTC Media Broker (Node.js / Mediasoup)
* AI Symptom Checker Service (Python / FastAPI)
* FHIR & E-Prescription Integration Service (Python / Java)
* Consent & Audit Logging Service (Go)
* Messaging (Cloud Pub/Sub)
* Databases (Cloud SQL PostgreSQL, Cloud Storage)

## Relationships
* Web & Mobile Clients -> API Gateway (TLS 1.3 over HTTPS, WSS)
* API Gateway -> Core Telehealth Service & AI Symptom Checker (gRPC via internal VPC Service Controls)
* Core Telehealth Service -> WebRTC Media Broker (gRPC, WebSockets/UDP)
* AI Symptom Checker -> Cloud Pub/Sub (gRPC)
* FHIR Integration Service -> National E-Prescription Gateways & US Pharmacy Networks (HTTPS with mTLS)
* Consent & Audit Logging Service -> Cloud Storage (Encrypted via CMEK)

## Technology Stack
* GCP (`europe-west3`, `us-central1`): Region-isolated cloud infrastructure ensuring strict GDPR and HIPAA compliance.
* Java/Spring Boot & Python/FastAPI: Robust backend runtimes for telehealth logic and AI inference.
* Node.js / Mediasoup: SFU-based WebRTC routing supporting degraded modes below 300 kbit/s.
* Cloud SQL PostgreSQL & Cloud Storage: Region-isolated transactional stores and cryptographically bound audit logs.
* VPC Service Controls & Cloud KMS: Perimeter security and Customer-Managed Encryption Keys enforcing data residency.

## Rationale
The architecture strictly isolates EU and US health data within designated GCP regions using VPC Service Controls and CMEK to satisfy GDPR and HIPAA mandates. Furthermore, Mediasoup-based WebRTC streaming and decoupled asynchronous logging ensure rural availability and traceable AI medical outputs.