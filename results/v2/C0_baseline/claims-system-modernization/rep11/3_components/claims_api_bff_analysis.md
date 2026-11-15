## Overview
[The Claims API (BFF) is a containerized backend service running in Azure Kubernetes Service that mediates interactions between modern React portals and legacy mainframe systems.]
[It ensures secure, high-performance claim processing while enabling a gradual, risk-free 3-year system modernization.]

## Key Elements
* Routing Mediator
* Aggregator / ViewModel Builder
* Authentication Middleware
* Session & Token Manager
* Payload Schema Validator
* Outbound Resilience Policy Engine
* Fallback & Graceful Degradation Handler
* Lifecycle & Health Management Component
* Azure Application Insights

## Relationships
* Web / Adjuster Portals -> Session & Token Manager (HTTPS / HttpOnly Cookies)
* Session & Token Manager -> Authentication Middleware (OIDC / Azure AD)
* Routing Mediator -> Outbound Resilience Policy Engine (Internal API / HTTPS)
* Aggregator -> Fallback & Graceful Degradation Handler (TCP/TLS / Cosmos DB cache)
* Claims API (BFF) -> Azure Cosmos DB (TCP/TLS)

## Technology Stack
* Node.js / TypeScript: Selected for asynchronous I/O performance and team capability alignment
* Azure Kubernetes Service (AKS): Container orchestration platform supporting horizontal scaling
* Zod: Schema validation library for strict inbound payload sanitization
* Opossum: Circuit breaker library for outbound mainframe request resilience
* Azure Application Insights: Native telemetry and distributed tracing monitoring tool

## Rationale
[Decomposing the BFF into modular components addresses strict performance constraints (<2s load times) despite slow mainframe responses.]
[Robust security controls and resilience policies protect against data loss and unauthorized access during hybrid cloud migration.]