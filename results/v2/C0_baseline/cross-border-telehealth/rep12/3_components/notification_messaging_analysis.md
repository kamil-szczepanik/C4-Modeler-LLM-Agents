## Overview
[The Notification & Messaging component handles asynchronous alerts, push notifications, and SMS distribution for the Cross-Border Telehealth Platform.]
[It ensures reliable, privacy-compliant communication for patients across the EU and US under variable network conditions.]

## Key Elements
- Notification & Messaging Container (Node.js on Cloud Run)
- Notification Orchestrator
- Consent Enforcer
- Channel Adapters
- Token Signer / Deep Link Generator
- Google Cloud Pub/Sub
- Google Cloud Memorystore (Redis)
- Google Cloud KMS / CMEK
- Google Secret Manager
- Firebase Cloud Messaging (FCM) / Apple Push Notification service (APNs)
- Twilio SMS Gateway

## Relationships
- Google Cloud Pub/Sub -> Notification Orchestrator: Consumes regional events via gRPC
- Notification Orchestrator -> Google Cloud Memorystore: Enforces idempotent delivery using Redis
- Consent Enforcer -> Consent Management Service: Validates recipient communication preferences via HTTPS/REST
- Channel Adapters -> FCM / APNs / Twilio: Dispatches outbound alerts using HTTPS/REST with TLS 1.3 and mTLS
- Notification & Messaging -> BigQuery: Emits delivery metrics and audit logs

## Technology Stack
- Node.js on Cloud Run: Lightweight, serverless execution matching regional deployment constraints
- Google Cloud Pub/Sub: Asynchronous messaging with regional topics for data residency (R-05)
- Google Cloud Memorystore (Redis): Deduplication layer preventing duplicate alerts on unstable networks (R-06)
- FCM, APNs, Twilio: Multi-channel delivery for mobile push and SMS fallbacks
- Google Cloud KMS & Secret Manager: Encryption at rest via CMEK and cryptographic key management
- OpenTelemetry: Distributed tracing and observability across regional pipelines

## Rationale
[Decomposing the service into specialized internal components (Orchestrator, Enforcer, Adapters, Token Signer) guarantees strict adherence to GDPR and HIPAA compliance by isolating consent checks and masking PHI.]
[Regional deployment models combined with multi-channel fallbacks, idempotency checks, and circuit breakers ensure high availability and accountability for patients in rural or unstable network environments.]