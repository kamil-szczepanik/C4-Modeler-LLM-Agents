## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and AI symptom checking for patients across the EU and US. The Integration Service securely bridges internal domain models with external pharmacy networks while strictly enforcing regional data residency.

## Key Elements
- FHIR Adapter Component (TypeScript / HAPI FHIR or custom mapper)
- EU E-Prescription Gateway Component (TypeScript)
- Data Residency Enforcer Component (Region-isolated instances in `europe-west3` and `us-central1`)
- Audit Logger Component
- Retry & Dead-Letter Queue Component (BullMQ / Redis)
- Transformation Engine Component (JSONata / Handlebars)
- Circuit Breaker & Rate Limiter Component (Opossum)

## Relationships
- Integration Service (EU/US instances) -> External Pharmacy Networks: Transmits payloads [HTTPS/REST, mTLS]
- EU E-Prescription Gateway & FHIR Adapter -> Transformation Engine: Applies schema mappings [In-memory]
- Adapters -> Retry & Dead-Letter Queue: Offloads failed outbound requests [Redis protocol]
- Adapters -> Circuit Breaker: Evaluates health and dispatches outbound requests [In-memory]
- Circuit Breaker -> External Pharmacy Networks: Sends payloads [HTTPS/REST, mTLS]
- Integration Service -> Google Cloud BigQuery: Records audit logs asynchronously [BigQuery API]

## Technology Stack
- Node.js with TypeScript: Ensures rapid asynchronous I/O handling and strict type safety for healthcare schemas.
- Redis (Memorystore) via BullMQ: Provides reliable, low-latency job persistence for asynchronous message queuing.
- JSONata: Enables declarative, side-effect-free data transformation for complex national e-prescription schemas.
- Opossum: Delivers lightweight, in-memory circuit breaking and rate limiting for external pharmacy integrations.

## Rationale
This component architecture enforces strict regional data residency by isolating EU and US traffic paths to comply with GDPR and HIPAA. Furthermore, it guarantees resilience against unstable rural internet connections through robust queuing, schema transformation, and circuit-breaking mechanisms.