## Overview
The Go Clinical Workspace Service orchestrates clinician-patient video sessions, triage reviews, and cross-border e-prescriptions within a multi-region Google Cloud Platform architecture. It ensures strict HIPAA and GDPR compliance while maintaining sub-second response times for regional healthcare workflows.

## Key Elements
- Go Clinical Workspace Service: Core container managing clinical workspace logic, session coordination, and prescription routing.
- Session Management Handler & Redis: Internal Go package and localized state caching for rural connection recovery.
- Prescription Router & Adapters: Translates domain models into payloads for US HL7 FHIR Adapters and EU National E-Prescription Formatters.
- Security & Infrastructure: Node.js API Gateway, Envoy API Gateway, GCP Cloud KMS, and GKE regional clusters.

## Relationships
- Node.js API Gateway -> Go Clinical Workspace Service: Delegates clinical domain logic via gRPC over TLS 1.3.
- Go Clinical Workspace Service -> Regional Adapters: Integrates with US HL7 FHIR and EU National E-Prescriptions via REST over mTLS.
- Go Clinical Workspace Service -> Redis: Caches session states locally for fast recovery.

## Technology Stack
- Go (Golang): Selected for low memory footprints, fast execution, and strict concurrency control during consultations.
- Redis: Provides low-latency session caching for degraded rural network conditions.
- GCP GKE & Cloud KMS: Manages regional container orchestration (`europe-west3`, `us-central1`) and customer-managed encryption keys (CMEK) for data residency.
- gRPC & Protocol Buffers: Enforces low-latency internal communication and strict schema validation.
- OpenTelemetry & Prometheus: Handles distributed tracing and real-time runtime metric collection.

## Rationale
The architecture uses Go and Redis to guarantee high throughput and low-latency session recovery, addressing unstable rural internet connections. Regional GKE isolation combined with mTLS, CMEK, and strict token validation ensures complete adherence to HIPAA and GDPR data residency constraints.