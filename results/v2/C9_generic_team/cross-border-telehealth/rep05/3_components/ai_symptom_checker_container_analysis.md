## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and high availability over unstable connections.

## Key Elements
* AI Symptom Checker Container
* API Gateway
* Managed Regional Databases (Cloud SQL / Spanner)
* Distributed Cache (Memorystore)
* Interoperability Adapter
* Audit Logging Service

## Relationships
* Patients to API Gateway via HTTPS/WSS over GCP
* API Gateway to AI Symptom Checker Container via gRPC
* AI Symptom Checker Container to Distributed Cache via Redis Protocol
* AI Symptom Checker Container to Audit Logging via Structured JSON Logs

## Technology Stack
* Google Cloud Platform (GCP): Target cloud provider across europe-west3 and us-central1 regions for data residency.
* gRPC: Protocol for inter-service communication ensuring strong typing and metadata propagation.
* Protocol Buffers: Serialization format with strict schema evolution rules for backward compatibility.
* OpenTelemetry: Observability framework for distributed tracing and latency profiling.

## Rationale
This architecture uses gRPC and stateless containers to provide robust traceability, deterministic logging, and strict EU MDR compliance. GCP regional deployments enforce data residency requirements while maintaining high availability for rural users.