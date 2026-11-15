## Overview
Modernizes a regional insurer's legacy mainframe claims platform by introducing a cloud-based Adjuster Workspace while maintaining the mainframe as the system of record. It enables gradual, risk-controlled claim type migrations with fast, reliable adjuster operations.

## Key Elements
- SPA Client (React, TypeScript)
- BFF Routing & Session Controller (Node.js, Express)
- Claims Orchestration Service (Node.js)
- Local View Cache Manager (Node.js)
- Feature Flag & Routing Adapter (Node.js)
- Audit Logging Interceptor (Node.js)
- Claims Read/Write Database (Azure Database for PostgreSQL)
- API Gateway (Azure API Management)
- Corporate Active Directory

## Relationships
- SPA Client -> BFF Routing & Session Controller: Renders UI and invokes BFF APIs [HTTPS/REST]
- Claims Orchestration Service -> API Gateway: Fetches domain data [HTTPS/REST]
- Local View Cache Manager -> Claims Read/Write Database: Queries local read models [TCP/PostgreSQL]
- SPA Client -> Feature Flag & Routing Adapter: Evaluates active claim types [HTTPS/REST]
- BFF Routing & Session Controller -> Corporate Active Directory: Authenticates via SSO [OIDC/SAML]

## Technology Stack
- React & TypeScript: Delivers responsive client-side rendering for fast adjuster UI loads (<2s)
- Node.js & Express: Powers the Backend-For-Frontend (BFF) and internal routing components
- Azure Database for PostgreSQL: Stores local claim read models and audit logs
- Azure API Management: Routes and secures traffic between cloud and on-premise mainframe
- OpenTelemetry: Provides unified distributed tracing across hybrid boundaries

## Rationale
The BFF pattern and local caching layer isolate the frontend from slow legacy mainframe responses, ensuring sub-2-second screen loads. Dynamic feature-flag routing enables rapid 24-hour claim type rollbacks to the mainframe while maintaining strict data consistency and security.