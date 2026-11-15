## Overview
The Dedicated Consent Evaluation Service provides real-time, policy-driven data privacy enforcement for the Cross-Border Telehealth Platform across the EU and US. It ensures compliance with regional health data residency mandates by evaluating and validating patient consent prior to any data access.

## Key Elements
- Dedicated Consent Evaluation Service: Microservice acting as the core policy engine.
- Region-Isolated API Gateways and Backend Services: Clients invoking the consent service.
- GCP Pub/Sub: Asynchronous messaging bus for cache invalidation events.
- Distributed Cache (Redis): In-memory caching layer for low-latency evaluations.
- Open Policy Agent (OPA): Policy framework evaluating rules via Rego.

## Relationships
- Region-Isolated API Gateways and Backend Services -> Dedicated Consent Evaluation Service: Validates patient consent [Internal REST/gRPC API, W3C Trace Context]
- Dedicated Consent Evaluation Service -> GCP Pub/Sub: Publishes and consumes cache invalidation events [GCP Pub/Sub Protocol]
- Dedicated Consent Evaluation Service -> Distributed Cache (Redis): Reads and writes cached consent states [TCP/Redis Protocol]

## Technology Stack
- Open Policy Agent (OPA) / Rego: Chosen for version-controlled, immutable policy bundling and testability.
- Redis: Selected for low-latency in-memory consent evaluation caching with short TTLs.
- GCP Pub/Sub: Utilized for decoupled, asynchronous cache invalidation across regions (`europe-west3` and `us-central1`).
- Protocol Buffers (Protobuf): Implemented for backward-compatible schema versioning and API contracts.

## Rationale
This architecture ensures low-latency evaluations on the critical path through distributed caching and stateless design. It strictly enforces regional data residency and compliance via immutable policy bundling and comprehensive audit logging.