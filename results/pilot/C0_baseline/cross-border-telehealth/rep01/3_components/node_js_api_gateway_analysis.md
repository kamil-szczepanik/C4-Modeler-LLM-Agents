## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. It ensures strict data residency, regulatory compliance, and resilience for low-bandwidth users.

## Key Elements
- Patients & Licensed Clinicians
- Flutter Web and Mobile Applications
- GCP Cloud Armor & Envoy API Gateway
- Node.js API Gateway (Fastify, http-proxy-middleware, opossum)
- Go Clinical Workspace Service & Go Consent & Localization Engine
- AI Symptom Checker Container (Python, FastAPI)
- mediasoup WebRTC SFU
- US HL7 FHIR Adapters & EU National E-Prescription Formatters

## Relationships
- Flutter Apps -> GCP Cloud Armor & Envoy API Gateway: Client requests [HTTPS, WSS]
- GCP Cloud Armor & Envoy API Gateway -> Node.js API Gateway: Routes incoming traffic [mTLS, gRPC/REST]
- Node.js API Gateway -> Go Clinical Workspace Service: Delegates clinical logic [mTLS, gRPC]
- Node.js API Gateway -> Go Consent & Localization Engine: Validates consent [mTLS, gRPC]
- Node.js API Gateway -> AI Symptom Checker Container: Requests AI analysis [Internal gRPC]
- Node.js API Gateway -> mediasoup WebRTC SFU: Coordinates video sessions [WebRTC]

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Multi-region cloud infrastructure ensuring regional data residency.
- Node.js & Fastify: High-throughput API gateway runtime and routing engine.
- gRPC & Protocol Buffers: Low-latency, strictly-typed internal service communication.
- opossum: Circuit breaker pattern implementation for rural connection resilience.
- OpenTelemetry & Prometheus: Distributed tracing and regional metrics collection.

## Rationale
This architecture guarantees strict regional compliance with GDPR and HIPAA by enforcing geo-pinning and consent checks at the API gateway layer. It ensures high availability and low-latency communication for rural users via resilient proxying, gRPC pooling, and multi-region GKE deployment.