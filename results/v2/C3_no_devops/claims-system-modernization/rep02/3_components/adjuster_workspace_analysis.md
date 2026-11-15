## Overview
The Adjuster Workspace is a modern web application providing claims adjusters and support agents with a unified interface to process insurance claims during a hybrid cloud migration. It shields users from legacy mainframe latency and hybrid data complexity while maintaining strict sub-second response times.

## Key Elements
- Adjuster UI (React SPA)
- Adjuster BFF / API Gateway (Node.js / Express)
- Claim View Cache (Azure Redis Cache)
- Integration Client (gRPC / HTTP Client)

## Relationships
- Claims Adjusters & Customer Support Agents -> Adjuster UI: HTTPS
- Adjuster UI -> Adjuster BFF: HTTPS / REST
- Adjuster BFF -> Azure API Management: HTTPS / gRPC with OAuth 2.0
- Adjuster BFF -> Claim View Cache: Redis Protocol over TLS

## Technology Stack
- React SPA: Frontend framework hosted on Azure Static Web Apps for responsive UI rendering
- Node.js / Express: Backend-for-Frontend (BFF) handling session management, aggregation, and security
- Azure Redis Cache: In-memory caching layer to meet strict performance targets by pre-fetching data
- OAuth 2.0 / OpenID Connect: Authentication protocols integrated with Azure Active Directory

## Rationale
This component-based BFF and caching architecture successfully decouples the modern UI from slow 5-second legacy mainframe responses to achieve required sub-2s screen loads. It secures sensitive PII while delivering a seamless, unified case-management experience across hybrid cloud boundaries.