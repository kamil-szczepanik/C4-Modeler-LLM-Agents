## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system ensures strict regional data residency, HIPAA/GDPR compliance, and high availability for unstable rural connections.

## Key Elements
- **API Gateway / BFF**: Node.js container running GraphQL, deployed in regional GCP instances (`europe-west3`, `us-central1`).
- **GraphQL Schema Coordinator & Complexity Analyzer**: Component managing unified graphs and AST-based query depth limits.
- **Auth & Scope Middleware**: Component validating OAuth2/OIDC JWTs and patient consent scopes.
- **Regional Routing & Istio Context Injector**: Component enforcing regional data residency and injecting security/trace headers.
- **WebSocket Connection Manager**: Component handling persistent duplex connections for real-time video signaling.
- **Downstream Microservices**: Consultation, Prescription, AI Symptom Orchestrator, and Consent & Audit services communicating via gRPC.

## Relationships
- **Clients -> GraphQL Schema Coordinator**: Client-facing traffic and real-time communication [HTTPS and WebSockets]
- **GraphQL Schema Coordinator -> Auth & Scope Middleware**: Internal request pipeline [Internal Middleware]
- **Auth & Scope Middleware -> Regional Routing Interceptor**: Internal request pipeline [Internal Middleware]
- **Regional Routing Interceptor -> Downstream Services**: Internal cross-service routing [gRPC over Istio mTLS]

## Technology Stack
- **Node.js**: Runtime for the API Gateway / BFF, chosen for asynchronous WebSocket concurrency.
- **GraphQL**: API query language for flexible client data aggregation and query complexity control.
- **Istio Service Mesh**: Secures internal service-to-service communication via mTLS and SPIFFE/SPIRE workload identities.
- **GCP (europe-west3, us-central1)**: Target cloud provider and regions for strict EU/US data residency compliance.
- **Kubernetes HPA**: Autoscaling driven by memory utilization for WebSocket connection stability.

## Rationale
Regional separation of gateway instances guarantees that EU and US health data never cross borders unlawfully, satisfying strict GDPR and HIPAA mandates. Furthermore, memory-optimized WebSocket management and AST complexity analysis ensure resilience against rural network degradation and edge-based denial-of-service attacks.