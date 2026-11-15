## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, regulatory compliance, and resilience for low-bandwidth rural environments on GCP.

## Key Elements
- Patient Management Component (Go)
- Consultation Orchestrator Component (Go)
- Prescription Coordinator Component (Node.js)
- Data Residency Enforcement Middleware (Go)
- Audit Logging Interceptor Component (Go)
- Consent Verification Interceptor (Go)
- Resilience & Fallback Handler Component (Go/Node.js)

## Relationships
- API Gateway -> Consent Verification Interceptor: Initial inbound request evaluation [gRPC over mTLS]
- Consent Verification Interceptor -> Patient Management Component & Consultation Orchestrator: Forwards validated requests [In-process function calls]
- Consultation Orchestrator -> Video Consultation Service: Initiates rooms [gRPC]
- Consultation Orchestrator & Prescription Coordinator -> Audit Logging Interceptor: Dispatches compliance events [In-process function calls]
- Consultation Orchestrator -> Resilience & Fallback Handler: Manages low-bandwidth state [In-process function calls]
- All Components -> Data Residency Enforcement Middleware: Wraps database queries [In-process middleware]
- All Components -> Cloud SQL (Regional): Data access via region-pinned connection pools [PostgreSQL Wire Protocol over TLS]
- Audit Logging Interceptor & Resilience Handler -> Pub/Sub: Publishes audit streams and deferred events [Cloud Pub/Sub API over TLS]

## Technology Stack
- Go: Used for performance-critical and concurrency-heavy backend components and middleware.
- Node.js: Powers the Prescription Coordinator component for integration flexibility.
- Google Cloud SQL for PostgreSQL: Provides region-isolated relational data persistence in `europe-west3` and `us-central1`.
- Google Cloud Pub/Sub: Handles asynchronous messaging and telemetry streaming over TLS.

## Rationale
This architecture uses Go and Node.js components to balance rapid I/O with high concurrency within regional GCP clusters. Dedicated middleware, interceptors, and region-pinned databases strictly enforce GDPR, HIPAA, and data residency constraints.