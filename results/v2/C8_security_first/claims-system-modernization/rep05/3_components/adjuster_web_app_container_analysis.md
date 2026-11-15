## Overview
Modernizes a regional insurer's legacy mainframe claims platform by introducing a hybrid cloud architecture. Enables gradual, claim-type-by-claim-type migration while ensuring continuous processing.

## Key Elements
- **Users:** End Customers & Brokers, Claims Adjusters, Operations & Migration Team
- **External Systems:** Legacy Mainframe, Microsoft Entra ID, Notification Service
- **Containers:** Customer Portal Container, Adjuster Web App Container, API Gateway, Claims Orchestrator Container, Legacy Mainframe Adapter Container, Claims State Database
- **Internal Components (Adjuster Web App):** UI Presentation Layer, BFF API Route Handlers, Client-Side Cache & State Manager, Draft Persistence Manager

## Relationships
- Claims Adjusters -> Adjuster Web App Container: Review and process claims [HTTPS/REST over TLS 1.3]
- Adjuster Web App Container -> API Gateway: Proxies API requests with OIDC token validation [HTTPS/REST]
- Adjuster Web App Container -> Microsoft Entra ID: Validates OIDC tokens [OpenID Connect]
- UI Presentation Layer -> BFF API Route Handlers: Internal RPC [HTTPS]
- UI Presentation Layer -> Draft Persistence Manager: Save/Restore draft state [TypeScript Function Calls]
- Draft Persistence Manager -> BFF API Route Handlers: Sync draft state [HTTPS/REST]

## Technology Stack
- **Web Frontend:** Next.js / React 18 for dynamic adjuster views and optimistic UI patterns.
- **Backend for Frontend (BFF):** Next.js API Routes for session state and token-exchange proxying.
- **Cloud Platform:** Azure Container Apps (ACA) for container hosting with blue/green deployments.
- **Client State:** TanStack Query (React Query) and IndexedDB for memory-only ephemeral caching and draft persistence.
- **Security:** Microsoft Entra ID with OpenID Connect (OIDC) and httpOnly, same-site cookies.
- **Infrastructure:** Terraform or Bicep for Infrastructure as Code.
- **Observability:** Application Insights for Real User Monitoring (RUM) and distributed tracing.

## Rationale
The hybrid architecture decouples modern web interfaces from the 30-year-old COBOL/DB2 mainframe, complying with strict cost and batch-window constraints. The Next.js BFF and ephemeral client-side caching overcome high legacy backend latency to deliver sub-2-second screen loads.