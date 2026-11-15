## Overview
[The React Single-Page Application serves as the primary modern web interface for policyholders, brokers, and claims adjusters within a hybrid cloud claims modernization platform. It enables digital claim submissions, dynamic form rendering for phased claim type migrations, and high-performance adjuster processing workflows.]

## Key Elements
- React Single-Page Application (SPA): Main user interface container
- React Router: View orchestration and client-side routing component
- Dynamic Form Renderer: Schema-driven component for adaptive claim forms
- TanStack Query: Data fetching, caching, and optimistic update component
- Auth Hook: Authentication and PKCE validation component using Web Crypto API

## Relationships
- Policyholders and Brokers -> React SPA: Submits digital claims and tracks status [HTTPS]
- Claims Adjusters -> React SPA: Processes claims via fast UI workflows [HTTPS]
- React SPA -> Azure API Management Gateway: Sends API requests via OpenAPI client SDKs [HTTPS, OAuth2/OIDC]
- React SPA -> Azure Blob Storage / Azure CDN: Static asset delivery and immutable deployment [HTTPS]

## Technology Stack
- React: Frontend UI library chosen for component-based architecture and ecosystem maturity
- TypeScript: Ensures end-to-end type safety with backend BFF contracts
- TanStack Query: Selected for aggressive client-side caching to meet sub-2s performance requirements
- Azure Blob Storage & Azure CDN: Scalable, low-maintenance static hosting fitting the team's cloud skill level
- Azure Application Insights: Real User Monitoring (RUM) and synthetic transaction tracking

## Rationale
[This architecture uses a dynamic schema-driven React SPA to support phased claim migrations without frequent client deployments. Client-side caching and optimized state management overcome slow legacy backend latencies to achieve required performance.]