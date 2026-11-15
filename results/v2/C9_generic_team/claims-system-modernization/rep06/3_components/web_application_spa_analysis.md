## Overview
[Modernizes a 30-year-old regional insurer mainframe claims system by gradually migrating claim types to a cloud platform. The architecture ensures zero claim loss, high performance, and rapid one-day rollbacks.]

## Key Elements
- Customers and Brokers
- Claims Adjusters
- Web Application (SPA)
- Backend-for-Frontend (BFF)
- On-Premise COBOL/DB2 Mainframe
- On-Premise Active Directory
- Azure Application Insights

## Relationships
- Customers and Brokers -> Web Application (SPA): Interact via HTTPS/REST (SSO via Active Directory)
- Claims Adjusters -> Web Application (SPA): Interact via HTTPS/REST (SSO via Active Directory)
- Web Application (SPA) -> Backend-for-Frontend (BFF): Communicates via HTTPS/REST
- Web Application (SPA) -> On-Premise Active Directory: Authenticates via SSO [HTTPS]

## Technology Stack
- Azure App Service: Hosts the Web Application (SPA) and BFF due to simplicity for teams with limited cloud experience
- TypeScript & OpenAPI: Generates type-safe API clients to eliminate schema drift between frontend and backend
- Playwright: Executes automated end-to-end smoke tests for rapid claim type rollback verification
- Azure Application Insights: Provides real-time client-side telemetry and performance monitoring

## Rationale
[Optimistic UI updates, strict API contract generation, and feature-flagged routing decouple the modern frontend from slow legacy mainframe responses. This architecture satisfies strict performance, rapid rollback, and security requirements despite the team's limited cloud experience.]