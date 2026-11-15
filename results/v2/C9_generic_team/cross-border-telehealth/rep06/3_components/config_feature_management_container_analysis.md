## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US while enforcing strict regional data residency and compliance. The architecture leverages GCP regions (`europe-west3` and `us-central1`) with robust fallback mechanisms and immutable versioning to guarantee high availability and auditability.

## Key Elements
- Patients and Licensed Clinicians
- API Gateway / Edge Proxy Container (GCP Cloud Load Balancing / Envoy)
- Config & Feature Management Container (GCP Cloud Config / Custom Service with Client-Side SDK)
- Integration & Translation Container (Node.js / GCP Cloud Run)
- Audit & Traceability Logging Container (GCP Pub/Sub / Cloud Logging)
- Data Persistence Container (Cloud SQL / Spanner)

## Relationships
- API Gateway / Edge Proxy Container -> Config & Feature Management Container: Fetches configurations, feature flags, and syncs caches via [gRPC over mTLS] with server-side streaming
- Config & Feature Management Container -> Audit & Traceability Logging Container: Records config changes and rule evaluations via [gRPC / GCP Pub/Sub]
- Integration & Translation Container -> Data Persistence Container: Stores regional health data via [PostgreSQL Protocol / JDBC]

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Target cloud provider and regions for data residency enforcement
- gRPC over mTLS: Protocol for secure, high-performance inter-container communication
- Node.js / GCP Cloud Run: Runtime environment for microservices and translation services
- JSON Schema: Technology used for validating configuration payloads at publishing boundaries
- Redis / GCP Memorystore: Technology for regional in-memory caching and session state management

## Rationale
This architecture ensures strict compliance with GDPR and HIPAA by enforcing regional data isolation and cryptographic verification of cross-border data flows. Additionally, local caching, circuit breakers, and default-safe fallback mechanisms maintain high availability and continuous video consultations even during unstable rural internet connections or regional network partitions.