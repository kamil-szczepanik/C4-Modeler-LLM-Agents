## Overview
[The system is a modern hybrid cloud platform that gradually replaces a 30-year-old mainframe insurance claims system. It provides an online portal and adjuster workspace to modernize claims processing while maintaining legacy data consistency.]

## Key Elements
- Claims Adjusters (Users)
- Insurer’s Active Directory (External System)
- Adjuster Workspace (React SPA on Azure Static Web Apps)
- Authentication Component (MSAL.js)
- Claim Management Module (React Router & Form Libraries)
- Local State & Caching Component (TanStack Query)
- API Client (Axios)
- Claims BFF (Node.js/Express on Azure App Service)
- Application Insights (Azure Monitoring)

## Relationships
- Claims Adjusters -> Authentication Component: Authenticates via [HTTPS/OIDC]
- Authentication Component -> Insurer’s Active Directory: Validates credentials via [HTTPS]
- Claim Management Module -> Local State & Caching Component: Reads/writes cached claim data via [In-Memory]
- Local State & Caching Component -> API Client: Requests fresh data on cache miss via [Async/Await]
- API Client -> Claims BFF: Sends REST requests via [HTTPS/REST]

## Technology Stack
- React SPA: Chosen for modern web application capabilities.
- Azure Static Web Apps: Hosts the frontend SPA with zero-downtime deployment capabilities.
- MSAL.js: Implements OIDC/OAuth2 authentication with secure in-memory token storage.
- TanStack Query: Manages server-state caching and volatile in-memory data persistence.
- Application Insights: Provides Real-User Monitoring (RUM), distributed tracing, and telemetry masking.

## Rationale
[This architecture meets the strict performance and security requirements by utilizing client-side caching to bypass slow mainframe latencies. It supports the team's low cloud experience with managed Azure services and robust automated CI/CD pipelines.]