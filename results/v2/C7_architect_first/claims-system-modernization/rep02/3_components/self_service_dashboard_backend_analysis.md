## Overview
[Self-Service Dashboard Backend for the Insurance Claims Modernization platform, providing a unified customer and broker interface that bridges legacy mainframe systems and the new Azure cloud platform.]

## Key Elements
- Dashboard Aggregator Component
- Claim Submission Orchestrator Component
- Cache-Aside Client Component
- Auth & Context Validator Component
- Normalization Service Component
- Event-Driven Projection Listener

## Relationships
- Self-Service Dashboard Backend to Claims Processing Service via gRPC / Async messaging over TLS 1.3
- Cache-Aside Client to Reference Data & Policy Cache (Redis) via mTLS
- Auth & Context Validator to Insurer Active Directory via OAuth2/OIDC (JWKS)
- Event-Driven Projection Listener to Azure WORM Storage for audit logging

## Technology Stack
- NestJS / TypeScript: Modular backend framework ensuring type safety and code reuse
- RxJS: Reactive stream merging for legacy and modern data sources
- OAuth2/OIDC with JWKS: Local token validation to minimize latency
- OpenTelemetry: Distributed tracing for latency monitoring

## Rationale
[This component-level architecture enforces an Anti-Corruption Layer via the Normalization Service to seamlessly blend legacy mainframe and modern platform data. It meets strict non-functional constraints including high consistency, security via Active Directory SSO, and sub-2-second UI responses despite legacy latency.]