## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker across the EU and US while enforcing strict regional data residency and compliance. The Interoperability Adapter container translates internal domain models into external sovereign healthcare standards.]

## Key Elements
- FHIR Translation Service (TypeScript/Fastify)
- EU E-Prescription Adapter (TypeScript)
- Egress Policy Enforcer (Rust/WebAssembly)
- Resilience & Queue Manager (Node.js/BullMQ)
- Data Residency Enforcer
- GCP Pub/Sub Regional DLQ Topics
- GCP Cloud KMS (HSM tier) & Secret Manager

## Relationships
- API Gateway -> Egress Policy Enforcer: Routes outbound requests [gRPC]
- Egress Policy Enforcer -> FHIR Translation Service & EU E-Prescription Adapter: Forwards sanitized payloads [Internal]
- EU E-Prescription Adapter -> National E-Prescription Gateways (EU): Submits prescriptions [HTTPS with eIDAS/mTLS]
- FHIR Translation Service -> HL7 FHIR Interoperability Services (US): Exchanges resources [HTTPS/REST with OAuth2]
- Resilience & Queue Manager -> GCP Pub/Sub: Offloads failing egress messages [gRPC/HTTPS]

## Technology Stack
- Node.js & TypeScript: Core runtime for adapter and queue management services for rapid asynchronous I/O
- Rust/WebAssembly: Powers the Egress Policy Enforcer for high-performance deterministic payload inspection
- GCP Pub/Sub (Regional): Manages Dead Letter Queues with CMEK for resilient asynchronous retries
- GCP Cloud KMS & Secret Manager: Secures eIDAS private keys in HSMs and manages US FHIR OAuth2 tokens
- OpenTelemetry: Provides distributed tracing and observability across regional gateway interactions

## Rationale
[Regionally isolated GKE deployments and CMEK-encrypted Pub/Sub queues guarantee that EU and US health data never cross borders without explicit consent. Cryptographic signing and dedicated policy enforcers satisfy strict EU MDR traceability and HIPAA compliance mandates.]