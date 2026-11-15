## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency and purpose-based consent using a distributed proxy architecture on Google Cloud Platform.

## Key Elements
* Patients and Licensed Clinicians (End Users)
* API Gateway (Google Cloud Platform, HTTPS/WSS)
* Consent Enforcement Proxy Sidecar (gRPC, REST)
* Open Policy Agent (OPA) Policy Engine
* Regional Google Cloud Storage Buckets
* OpenTelemetry Tracing System
* Regional Cloud SQL / Spanner Databases

## Relationships
* Patients and Clinicians -> API Gateway: Access telehealth services [HTTPS/WSS]
* API Gateway -> Consent Enforcement Proxy Sidecar: Intercepts cross-region requests between `europe-west3` and `us-central1` [gRPC/REST]
* Consent Enforcement Proxy Sidecar -> Open Policy Agent: Evaluates declarative Rego policies locally [In-memory]
* Consent Enforcement Proxy Sidecar -> Google Cloud Storage: Pulls cryptographically signed policy bundles [HTTPS]
* Consent Enforcement Proxy Sidecar -> Regional Databases: Validates tokens via local Redis cache and Bloom filter revocation checks [TCP]

## Technology Stack
* Cloud Provider: Google Cloud Platform (Regions: `europe-west3`, `us-central1`) for regional data isolation
* Authorization Engine: Open Policy Agent (OPA) for externalizing declarative compliance rules
* Policy Distribution: Google Cloud Storage for versioned, cryptographically signed policy bundles
* Token Standard: Cryptographically signed JSON Web Tokens (JWTs) for stateless local validation
* Revocation Registry: Distributed Redis cache and Bloom filters for real-time token revocation checks
* Observability: OpenTelemetry for distributed tracing and immutable correlation ID propagation
* Audit Logging: Structured JSON logs flushed via asynchronous append-only buffers

## Rationale
This architecture uses local sidecar evaluation with signed JWTs and OPA policy bundling to eliminate cross-region latency bottlenecks while maintaining strict GDPR and HIPAA compliance. A fail-closed circuit breaker and asynchronous logging ensure high availability during degraded network conditions and full accountability for cross-border data access.