## Overview
Modernizes a regional insurer's claims platform via a hybrid architecture while the legacy mainframe remains the system of record. Decomposes the Adjuster Workspace container into a secure, low-latency component topology in Azure West Europe.

## Key Elements
* Workspace UI Shell (React, TypeScript)
* Claim Processing Controller (Node.js, Express)
* Distributed Cache Client (Node.js Redis client)
* Circuit Breaker / Fallback Manager (Opossum)
* Azure Redis Cache
* Adjuster Backend Service (Java, Spring Boot, ACL)

## Relationships
* Claims Adjusters -> Workspace UI Shell: Interacts to manage claims [HTTPS]
* Workspace UI Shell -> Claim Processing Controller: REST API calls [HTTPS/JSON]
* Claim Processing Controller -> Adjuster Backend Service: Fetches/updates claim data [REST/HTTPS/mTLS]
* Claim Processing Controller -> Distributed Cache Client: Read/Write claim view models [Redis Protocol/TLS]
* Distributed Cache Client -> Azure Redis Cache: External caching with TTL [Redis Protocol/TLS]

## Technology Stack
* Azure Container Apps: Hosts Node.js and React components with blue/green revisions for zero-downtime deployments.
* Azure Redis Cache: Centralized external caching with TLS and managed identity for sub-2s claim screen rendering (R-05).
* Node.js / TypeScript: Runtime for UI controllers and schema validation (Zod/Joi) to prevent injection risks.
* Opossum Circuit Breaker: Manages downstream mainframe latency spikes (up to 5s) to guarantee UI responsiveness.
* OpenTelemetry & Application Insights: Enforces distributed tracing and P99 latency alerts across the hybrid boundary.

## Rationale
The hybrid architecture protects the 3-year legacy mainframe migration constraint while providing a sub-2s cloud adjuster workspace via Azure Redis caching and circuit-breaking. Security and maintainability are enforced through OIDC Active Directory integration, encrypted state management, and containerized blue/green deployments.