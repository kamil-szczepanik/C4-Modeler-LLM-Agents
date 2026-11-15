## Overview
[The Adjuster BFF is a Node.js/TypeScript backend-for-frontend service that aggregates hybrid data sources to power the new web application for claims adjusters.]
[It masks legacy mainframe latency to meet strict sub-two-second performance requirements while enforcing security policies.]

## Key Elements
- Azure API Management Gateway (Azure API Management, OAuth2/OIDC)
- Adjuster BFF (Node.js, TypeScript, Express.js, RxJS)
- Modular Monolith (Node.js, TypeScript)
- Redis Cache (Redis Cache, node-cache)
- Legacy Mainframe COBOL/DB2 System

## Relationships
- Azure API Management Gateway -> Adjuster BFF: Routes adjuster requests [HTTPS, mTLS, OAuth2/OIDC]
- Adjuster BFF -> Modular Monolith: Invokes core domain operations [HTTP/REST, mTLS]
- Adjuster BFF -> Redis Cache: Stores transient claim state and cached legacy segments [TCP, TLS]
- Adjuster BFF -> Legacy Mainframe COBOL/DB2 System: Fetches fallback legacy claim data via integration layer [HTTPS]

## Technology Stack
- Node.js & TypeScript: Provides rapid asynchronous I/O handling for high-concurrency data aggregation
- Express.js & RxJS: Used for HTTP routing and reactive stream coordination without blocking the event loop
- Redis Cache: Caches legacy claim segments to meet the sub-two-second latency SLA despite slow legacy responses
- Azure App Service / AKS: Containerized deployment platform with automated health probes and blue-green slots

## Rationale
[This architecture uses a Backend-for-Frontend pattern to decouple the adjuster UI from the underlying hybrid complexity and shield users from slow legacy response times.]
[It isolates modern claim handling within a scalable cloud container while safely orchestrating data from the 30-year-old mainframe.]