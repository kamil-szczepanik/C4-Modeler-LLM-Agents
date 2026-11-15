## Overview
[The Insurance Claims Modernization system gradually replaces a 30-year-old mainframe with a modern hybrid cloud platform. It ensures seamless parallel processing of claims while maintaining strict performance, security, and data consistency.]

## Key Elements
- Claims Adjusters & Customers/Brokers
- Adjuster Workspace (SPA React)
- API Gateway (Azure API Management)
- Claims Core Container (.NET / Azure Container Apps)
- Azure Active Directory & Azure Cosmos DB

## Relationships
- Claims Adjusters -> Adjuster Workspace: Interacts for internal workflows [HTTPS/REST]
- Adjuster Workspace -> Azure Active Directory: Authenticates users [OpenID Connect / OAuth 2.0 with PKCE]
- Adjuster Workspace -> API Gateway: Routes state-changing intents [HTTPS/TLS 1.3]
- Optimized Read Store Client -> Azure Cosmos DB: Queries cached projections directly using ephemeral resource tokens [HTTPS]

## Technology Stack
- React SPA: Chosen for responsive UI development within the Adjuster Workspace.
- Azure Cosmos DB: Provides low-latency storage for read projections to meet <2s load times.
- Azure API Management: Secures and routes backend communications.
- Azure Active Directory: Enables enterprise SSO integration (R-07).

## Rationale
[This architecture decouples the legacy mainframe from the modern UI, enabling high-performance adjuster workflows through dedicated read models while preserving system consistency. The hybrid approach allows incremental claim-type migration with minimal risk.]