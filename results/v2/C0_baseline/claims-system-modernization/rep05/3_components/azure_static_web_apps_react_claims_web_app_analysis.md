## Overview
Modernizes a regional insurer's legacy mainframe claims system via a gradual hybrid migration platform. Replaces aging infrastructure while ensuring continuous operations for policyholders, brokers, and adjusters over a 3-year rollout.

## Key Elements
- Policyholders / Brokers & Claims Adjusters (Users)
- Azure API Management / Migration Router
- Azure Static Web Apps / React Claims Web App
- Azure Container Apps (Adjuster Backend & Mainframe Integration Adapter)
- Azure App Service & Azure Cosmos DB (Migration Control Service)
- Azure Service Bus & Azure Functions (Integration & Sync Service)
- Legacy COBOL/DB2 Mainframe & Active Directory / Entra ID

## Relationships
- Claims Adjusters -> Azure Static Web Apps: Accesses SPA via HTTPS / OAuth 2.0 / OIDC
- Azure Static Web Apps -> Azure API Management: Routes API requests via HTTPS / REST
- Azure API Management -> Azure Container Apps: Forwards backend traffic via HTTPS / gRPC
- Azure Container Apps -> Legacy Mainframe: Synchronizes data via TCP/IP / MQ
- Azure App Service -> Active Directory: Validates SSO tokens via OpenID Connect

## Technology Stack
- React & TypeScript: Frontend SPA framework for responsive adjuster and broker interfaces (<2s load time requirement).
- Azure Static Web Apps: Global CDN hosting for static assets with built-in GitHub Actions CI/CD.
- Azure API Management: Unified gateway routing traffic between modern microservices and the legacy mainframe.
- Azure Container Apps: Serverless container runtime hosting backend adapters without requiring deep cloud expertise.
- Azure Cosmos DB & App Service: Migration control and feature flag management enabling 1-day fallback capabilities.
- MSAL.js & Azure AD: Secure single sign-on authentication enforcing strict token memory-only storage.

## Rationale
The hybrid architecture decouples modern React frontends from the 30-year-old mainframe using API management and asynchronous messaging. This isolates expensive mainframe constraints, supports phased claim-type migration, and accommodates low team cloud experience via managed Azure services.