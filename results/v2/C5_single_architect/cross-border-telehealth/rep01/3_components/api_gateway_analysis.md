## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and high availability over unstable networks.

## Key Elements
* Patients and Clinicians (Users)
* Single-Patient / Mobile App (Flutter / TypeScript container)
* API Gateway (Google Cloud API Gateway container) decomposed into:
  * Routing & Regional Dispatcher (Go / Envoy Proxy component)
  * JWT & mTLS Termination Filter component
  * Rate Limiting & Circuit Breaker component
  * Compliance Audit Logger component
* Core Telehealth Service (Go / gRPC)
* AI Inference Wrapper (Python / FastAPI)
* SFU Media Server / LiveKit (GKE)
* US FHIR Adapter (Node.js / TypeScript) & EU E-Prescription Gateway (Java / Spring Boot)
* Cloud SQL PostgreSQL & Cloud Storage (GCP)

## Relationships
* Mobile App -> API Gateway (JWT & mTLS Termination Filter): Routes encrypted ingress traffic [HTTPS/mTLS]
* Routing & Regional Dispatcher -> Core Telehealth Service / AI Inference Wrapper / US FHIR Adapter / EU E-Prescription Gateway: Forwards requests [Internal gRPC]
* Routing & Regional Dispatcher -> Compliance Audit Logger: Sends routing telemetry [Internal gRPC]
* Compliance Audit Logger -> Cloud Storage / Cloud Pub/Sub: Persists regional compliance logs [HTTPS/Cloud Pub/Sub]

## Technology Stack
* Google Cloud API Gateway: Managed entry point for secure, scalable routing.
* Go / Envoy Proxy: High-performance regional routing and dispatching.
* GCP VPC Service Controls: Enforces strict regional data isolation between `europe-west3` and `us-central1`.
* HTTPS/mTLS and gRPC: Ensures encrypted, high-performance transport protocols across microservices.

## Rationale
This architecture enforces strict regional data residency by routing EU and US traffic exclusively to compliant GCP regions. The internal API Gateway decomposition ensures robust security, auditable compliance logging, and fault-tolerant routing for degraded connections.