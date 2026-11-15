## Overview
[The Insurance Claims Modernization Platform gradually replaces a 30-year-old COBOL/DB2 mainframe with a cloud-native Azure platform while maintaining uninterrupted legacy claims processing. It provides a secure, high-performance hybrid architecture ensuring zero data loss and business continuity during iterative migrations.]

## Key Elements
- Adjuster Portal (SPA): React-based single-page application hosted on Azure Static Web Apps.
- Routing & Shell Component: React Router / TypeScript component managing OIDC navigation and Azure AD SSO.
- Feature Toggle Context: Dynamic module consuming routing and feature metadata from the BFF.
- Claims Management Module: React Query/Zustand reactive forms handling optimistic UI updates and local caching.
- API Client Layer: REST/JSON communication module injecting correlation IDs for OAuth 2.0 / OIDC bearer tokens.
- Error Boundary Component: Global component capturing API timeouts and mainframe degradation events.
- Claims API (BFF) & Mainframe Adapter: Node.js / TypeScript containers running in Azure Kubernetes Service (AKS).

## Relationships
- Claims Adjusters -> Adjuster Portal (SPA): Interact via HTTPS [HTTPS (TLS 1.3)]
- Adjuster Portal (SPA) -> Claims API (BFF): Communicate via REST [REST over HTTPS with OAuth 2.0 / OIDC (Azure AD)]
- Claims API (BFF) -> Mainframe Adapter: Coordinate claims processing [Internal REST / gRPC]
- Mainframe Adapter -> Legacy Mainframe System: Access legacy database [SNA / IBM MQ / DB2 Direct]

## Technology Stack
- Azure Static Web Apps: Global CDN and pre-rendered edge capabilities for sub-2-second load performance.
- React & TypeScript: Frontend framework for component-driven UI development and type safety.
- React Query / Zustand: State management and client-side caching to decouple UI from slow backend latencies.
- Azure App Configuration: Centralized runtime configuration for dynamic feature flags and rapid rollback management.
- Azure Application Insights: Real-user monitoring (RUM) and end-to-end tracing via correlation IDs.
- GitHub Actions: Automated CI/CD pipeline tied to staging environments for safe PR previews.

## Rationale
[This hybrid architecture bridges legacy mainframe constraints with modern cloud capabilities by using a BFF pattern and client-side caching to mask high backend latencies. Centralized feature flags and rigorous security controls ensure seamless iterative claim migration and strict compliance without risking operational continuity.]