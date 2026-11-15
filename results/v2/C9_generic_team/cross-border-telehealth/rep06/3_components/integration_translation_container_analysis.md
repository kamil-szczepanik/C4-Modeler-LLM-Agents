## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker across the EU and US. It ensures region-locked data residency, strict regulatory compliance, and high availability over GCP.

## Key Elements
- Integration & Translation Container (Node.js / GCP Cloud Run)
- Anti-Corruption Layer (ACL) with Plugin/Adapter Architecture
- GCP Pub/Sub Dead-Letter Queue (DLQ)
- Regional GCP Pub/Sub Topics (`europe-west3`, `us-central1`)
- State & Session Management Container (Redis / GCP Memorystore)

## Relationships
- API Gateway / Edge Proxy Container -> Integration & Translation Container: Routes requests [gRPC over mTLS]
- Integration & Translation Container -> External Health Integrations & Pharmacies: Communicates with external partners [HL7 FHIR, EU national e-prescription standards]
- Integration & Translation Container -> State & Session Management Container: Retrieves transient state during transformations [Redis protocol]
- Integration & Translation Container -> GCP Pub/Sub: Routes failed payloads to regional DLQ [gRPC/HTTPS]

## Technology Stack
- Node.js on GCP Cloud Run: Provides scalable, stateless compute for I/O-bound protocol mapping.
- Zod / JSON Schema: Enforces strict data validation at adapter boundaries.
- Pact: Enables contract testing to catch breaking external API changes in CI/CD.
- Opossum: Implements circuit breakers for resilient outbound calls.

## Rationale
This architecture isolates volatile external standards using an Anti-Corruption Layer, ensuring regional compliance and robust error handling. Stateless Cloud Run instances combined with regional messaging guarantee strict data residency and high availability.