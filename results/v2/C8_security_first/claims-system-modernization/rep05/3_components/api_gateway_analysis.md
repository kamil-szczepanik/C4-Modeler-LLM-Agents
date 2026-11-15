## Overview
[The system modernizes a regional insurer's 30-year-old mainframe claims platform using a hybrid cloud architecture. It gradually migrates claim types while maintaining business continuity and legacy integration.]

## Key Elements
- **API Gateway**: Azure API Management (APIM) acting as the entry point and trust boundary.
- **Configuration Store**: Azure App Configuration for dynamic routing rules.
- **Caching Layer**: Azure Cache for Redis for read-only reference data.
- **Backend Services**: Claims Orchestrator Container (Node.js/.NET Core) and Legacy Mainframe Adapter Container (Azure Container Apps).
- **Security Services**: Microsoft Entra ID for OIDC token validation.

## Relationships
- Customer Portal / Adjuster Web App -> API Gateway: API requests with OIDC token validation [HTTPS/REST]
- API Gateway -> Claims Orchestrator Container: Routes requests to core backend [HTTPS/REST and gRPC]
- API Gateway -> Legacy Mainframe Adapter Container: Routes unmigrated claim types [HTTPS/REST]
- API Gateway -> Azure App Configuration: Fetches routing rules [HTTPS]
- API Gateway -> Azure Cache for Redis: Reads/writes cached reference data [TCP]

## Technology Stack
- **Azure API Management**: Edge routing, policy enforcement, and WAF protection.
- **Azure App Configuration**: Externalized declarative routing rules for zero-downtime migrations.
- **Azure Cache for Redis**: Response caching to mitigate mainframe latency and achieve sub-2-second screen loads.
- **Microsoft Entra ID**: Single sign-on and OIDC token validation.
- **Terraform / Bicep**: Infrastructure-as-Code for GitOps-based deployments to support teams with limited cloud experience.

## Rationale
[This hybrid architecture decouples modern frontends from the legacy mainframe via a flexible API Gateway, enabling incremental claim type migration and rapid rollbacks. Externalized configuration and managed Azure services reduce operational risk for a team with limited cloud experience.]