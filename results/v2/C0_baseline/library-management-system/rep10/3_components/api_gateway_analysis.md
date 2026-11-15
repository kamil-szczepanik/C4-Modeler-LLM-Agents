## Overview
[The system is the Library Management System API Gateway, responsible for ingress routing, security enforcement, and telemetry for public and academic library portals.]

## Key Elements
- Kong/Envoy API Gateway Container
- TLS Termination & Routing Plugin Component
- Authentication & Authorization Filter Component (with Redis-backed token cache)
- Rate Limiting & Throttling Module Component
- Analytics & Telemetry Emitter Component
- External Identity Provider (IdP)
- Observability Platform & SIEM

## Relationships
- Library Patrons / Staff / Administrators -> API Gateway: Access via [HTTPS/REST]
- API Gateway -> Patron Web App & API: Routes traffic via [gRPC over mTLS]
- API Gateway -> Staff Management API: Routes traffic via [gRPC over mTLS]
- API Gateway -> External Identity Provider (IdP): Validates tokens via [HTTPS]
- API Gateway -> Observability Platform & SIEM: Streams telemetry via [OpenTelemetry (OTel) / Prometheus over TLS]

## Technology Stack
- Kong/Envoy: Chosen as the API Gateway for robust plugin architecture and high-performance routing.
- Redis: Used for local token-caching to reduce IdP dependency and maintain sub-second latency.
- OpenTelemetry (OTel) & Prometheus: Utilized for asynchronous metric and trace emission while maintaining performance SLAs.
- gRPC over mTLS: Implemented for secure, high-performance inter-container communication.

## Rationale
[The architecture decomposes the API Gateway into modular components with local token caching and asynchronous telemetry to achieve the strict < 800 ms search performance requirement. It enforces strict zero-trust security and PII-scrubbing at the edge to ensure robust EU data residency compliance.]