## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The E-Prescription Integration Service securely routes prescriptions to regional pharmacies while enforcing strict data residency and compliance.]

## Key Elements
*   Frontend Client Apps (Flutter)
*   API Gateway / BFF (Envoy / gRPC-Web)
*   E-Prescription Integration Service (Node.js / Express)
    *   Prescription API Controller
    *   Regional Adapter Engine
    *   Async Status Poller / Webhook Receiver
    *   DLQ Management & Retry Worker
    *   Audit & Telemetry Middleware
*   Consent & Policy Engine (Opa / Go)
*   Data Layer (PostgreSQL / Cloud SQL)
*   EU National e-Prescription Gateways & US Pharmacy Networks
*   GCP Services (Cloud Pub/Sub, Cloud KMS, Cloud Logging, Cloud Monitoring)

## Relationships
*   API Gateway / BFF -> Prescription API Controller: Routes e-prescription requests [gRPC, mTLS]
*   Prescription API Controller -> Regional Adapter Engine: Invokes translation and dispatch [In-process, TypeScript]
*   Regional Adapter Engine -> EU National Gateways & US Pharmacy Networks: Secure fulfillment [HTTPS / mTLS]
*   Async Status Poler -> Cloud Pub/Sub: Publishes fulfillment updates [gRPC]
*   DLQ Management & Retry Worker -> Regional Adapter Engine: Re-dispatches corrected payloads [In-process]
*   E-Prescription Integration Service -> Cloud Logging: Emits immutable audit trails [HTTPS]

## Technology Stack
*   Node.js / Express & TypeScript: Chosen for asynchronous I/O performance and strong typing in integration logic.
*   GCP (Cloud Run / GKE, Cloud Pub/Sub, Cloud KMS): Ensures scalable regional deployments in `europe-west3` and `us-central1` with envelope encryption.
*   HL7 FHIR & NCPDP: Enables interoperability with US networks and EU national e-prescription standards.
*   Envoy & gRPC: Guarantees secure, low-latency internal communication with mTLS.

## Rationale
[This architecture enforces strict regional isolation and encryption to satisfy GDPR and HIPAA data residency mandates. Pluggable regional adapters and dead-letter queues ensure reliable prescription delivery despite unstable third-party networks.]