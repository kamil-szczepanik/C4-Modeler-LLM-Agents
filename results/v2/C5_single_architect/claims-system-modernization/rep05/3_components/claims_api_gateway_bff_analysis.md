## Overview
The Claims API Gateway / BFF system modernizes a regional insurer's legacy mainframe by providing secure, low-latency API orchestration and routing. It enables incremental claim type migration and sub-second adjuster screen performance via hybrid cloud deployment.

## Key Elements
- **API Router Component**: Azure API Management / .NET Core for rate limiting and token validation.
- **BFF Orchestrator Component**: .NET Core minimal API on Azure Container Apps for client data aggregation.
- **Routing Proxy Component**: .NET Core middleware for dynamic traffic splitting between modern and legacy systems.
- **Response Caching & Transformation Component**: .NET Core with Azure Cache for Redis for payload optimization.
- **External Systems**: Active Directory, Legacy Mainframe System, Integration Gateway, Web App Portal, Feature Flag / Routing Service, Core Claims Service, Claims Database.

## Relationships
- Web App Portal -> Claims API Gateway / BFF: Communicates via HTTPS/JSON.
- Claims API Gateway / BFF -> Active Directory: Authenticates users via OIDC/OAuth2.
- Claims API Gateway / BFF -> Feature Flag / Routing Service: Routes requests dynamically via gRPC/HTTPS.
- BFF Orchestrator Component -> Response Caching & Transformation Component: Uses in-process gRPC/HTTP with Azure Cache for Redis.
- Routing Proxy Component -> Integration Gateway / Core Claims Service: Directs traffic via HTTPS.

## Technology Stack
- **Azure API Management & Container Apps**: Selected for managed cloud infrastructure reducing cloud experience overhead.
- **.NET Core**: Chosen for robust API development, minimal APIs, and team familiarity.
- **Azure Cache for Redis**: Implemented to meet sub-2s performance requirements (R-05) by caching slow mainframe responses.
- **OIDC / OAuth2 & Active Directory**: Enforced for secure enterprise single sign-on (R-07).

## Rationale
This architecture isolates legacy dependencies through explicit proxy and caching components, ensuring zero data loss during incremental migration. It guarantees sub-2s UI responses while meeting strict mainframe integration constraints.