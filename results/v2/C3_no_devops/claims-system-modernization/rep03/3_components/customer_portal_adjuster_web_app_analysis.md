## Overview
[The Customer Portal & Adjuster Web App modernizes user interactions for a regional insurer's claims platform. It provides responsive web interfaces for customers, brokers, and claims adjusters while hiding legacy mainframe latencies.]

## Key Elements
- SPA Shell & Routing Engine (React / TypeScript)
- Dynamic Form Engine (React Hook Form / JSON Schema)
- Optimistic UI & Local State Cache (TanStack Query)
- Telemetry & Error Boundary Handler (Azure Application Insights SDK)

## Relationships
- Browser to Azure API Management Gateway: Routes client traffic [HTTPS / TLS 1.3]
- SPA Shell to Azure Active Directory: Authenticates users and manages sessions [OpenID Connect / OIDC]
- Telemetry Handler to Azure Application Insights: Streams anonymized performance metrics and error logs [HTTPS]

## Technology Stack
- React with TypeScript: Chosen for team familiarity and rich ecosystem supporting component-driven UI.
- JSON Schema & React Hook Form: Enables dynamic, metadata-driven form rendering to support iterative claim type migration without frontend deployments.
- TanStack Query: Manages local state and caching to meet sub-2-second performance requirements despite mainframe lag.
- Azure Container Apps: Hosts the frontend application within the hybrid cloud architecture.

## Rationale
[This component-level architecture ensures sub-2-second UI performance and dynamic metadata rendering to support iterative claim migrations. It strictly enforces security, RBAC, and OIDC authentication against the insurer's Active Directory.]