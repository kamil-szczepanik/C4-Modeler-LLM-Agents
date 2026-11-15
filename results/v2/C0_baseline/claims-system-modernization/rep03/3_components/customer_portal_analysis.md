## Overview
[The Customer Portal is a React single-page application hosted on Azure Static Web Apps that enables 24/7 digital claim submissions for customers and brokers. It modernizes the legacy insurance workflow while integrating securely with the backend claims platform.]

## Key Elements
- Customer Portal (React / TypeScript SPA, Azure Static Web Apps)
- Claim Submission Wizard Component (Multi-step form with Dexie.js / IndexedDB)
- Status Tracker View Component (Real-time WebSocket / SSE connection)
- Auth Integration Module (MSAL.js for OpenID Connect)
- Claims API Gateway / BFF (Node.js / .NET Core, Azure Container Apps)
- Azure Storage Blob (Cloud object storage for media binaries)

## Relationships
- End Customers & Brokers -> Customer Portal: Accesses via [HTTPS (REST)]
- Customer Portal -> Claims API Gateway / BFF: Communicates via [HTTPS/JSON]
- Customer Portal -> Azure Storage Blob: Uploads media via [HTTPS with SAS tokens]
- Claims API Gateway / BFF -> Corporate Active Directory: Authenticates via [OIDC]

## Technology Stack
- React & TypeScript: Core UI framework for a lightweight SPA footprint
- Azure Static Web Apps: Global hosting and rapid CI/CD deployment
- IndexedDB via Dexie.js: Client-side storage for offline drafts and resilience
- Web Crypto API: Browser-level encryption for local draft data protection
- MSAL.js: OpenID Connect token management for secure SSO

## Rationale
[This component-level architecture keeps the frontend decoupled and resilient for offline field use while minimizing backend complexity. It directly addresses the team's low cloud experience through managed Azure services and standard web protocols.]