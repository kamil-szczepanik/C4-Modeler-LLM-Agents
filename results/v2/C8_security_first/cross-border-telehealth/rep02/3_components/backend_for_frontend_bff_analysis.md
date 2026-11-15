## Overview
- A cloud-native Backend-for-Frontend (BFF) built on Node.js and GraphQL, deployed across GCP regions (`europe-west3` and `us-central1`).
- Manages secure, resilient data aggregation and protocol translation for cross-border telehealth patients and clinicians.

## Key Elements
- **GraphQL API Gateway Layer (Apollo Server):** Handles query parsing, schema validation, depth limiting, and complexity analysis.
- **Authentication & Token Translator:** Terminates client JWTs, validates scopes, and issues internal mTLS tokens.
- **Resilience & Batching Middleware:** Manages query batching, optimistic mutations, and connectivity status for rural users.
- **Resolver & Aggregator Engine:** Orchestrates domain-specific data fetching and field-level authorization.
- **Telemetry & Audit Interceptor:** Injects OpenTelemetry context and regional audit headers for EU MDR traceability.

## Relationships
- **Clients -> GraphQL API Gateway Layer:** Sends aggregated queries and mutations over HTTPS.
- **GraphQL API Gateway Layer -> Authentication & Token Translator:** Delegates user session validation [In-process].
- **Authentication & Token Translator -> Resilience & Batching Middleware:** Passes validated operations [In-process middleware].
- **Resilience & Batching Middleware -> Resolver & Aggregator Engine:** Forwards batched requests [In-process function call].
- **Resolver & Aggregator Engine -> Domain Microservices (Consent Manager, AI Triage, E-Prescription):** Dispatches calls via gRPC over mTLS (Istio).

## Technology Stack
- **Node.js:** Core runtime for the BFF containers, managed via GCP Google Kubernetes Engine (GKE).
- **Apollo Server:** GraphQL framework providing schema stitching, query complexity analysis, and depth limiting.
- **gRPC over mTLS (Istio Service Mesh):** Protocol and transport security for all internal container-to-container communications.
- **OpenTelemetry:** Observability framework for distributed tracing and audit logging of AI recommendations.
- **Zod / Joi:** Validation libraries utilized at the GraphQL boundary for payload sanitization.

## Rationale
- Decouples client applications from regional backend complexities while enforcing strict data residency boundaries between the EU and US.
- Mitigates security risks and ensures high availability for unstable rural connections through robust middleware and resource governance.