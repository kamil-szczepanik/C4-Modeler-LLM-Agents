## Overview
[The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern hybrid cloud platform. It enables online claim submissions and adjuster workflows while ensuring continuous legacy operation.]

## Key Elements
- Claims Adjusters (Users)
- Adjuster Workspace (Web Application / BFF Container)
- Workspace Shell Component (React, TypeScript)
- Claim Processing Dashboard (React, TanStack Query)
- Integration Client Layer (Axios, OpenAPI client)
- State & Offline Manager Component (Zustand, IndexedDB, Web Crypto API)
- Telemetry & Tracing Interceptor (OpenTelemetry JS)
- API Gateway / Router (YARP reverse proxy)
- Claims Core Service (Spring Boot, Java, Azure Container Apps)
- Identity Provider (Active Directory)
- Azure Application Insights

## Relationships
- Claims Adjusters -> Workspace Shell Component: Interacts via [HTTPS]
- Claim Processing Dashboard -> State & Offline Manager Component: Uses [In-memory / IndexedDB]
- Integration Client Layer -> Telemetry & Tracing Interceptor: Uses [HTTPS]
- Integration Client Layer -> API Gateway / Router: Calls via [TLS 1.3 / REST / JSON]
- Workspace Shell Component -> Identity Provider: Authenticates via [OAuth 2.0 / OpenID Connect]

## Technology Stack
- React & TypeScript: Powers responsive frontend components for rapid UI development
- TanStack Query: Provides optimistic UI updates and local caching to mask legacy mainframe latency
- Zustand & IndexedDB: Manages local offline state and draft caching with client-side encryption
- Azure Container Apps: Hosts the BFF and backend services for low operational complexity
- OpenTelemetry JS: Captures distributed tracing headers (W3C Trace Context) while scrubbing PII

## Rationale
[This architecture satisfies the sub-2s performance requirement (R-05) despite 5s mainframe bottlenecks by using optimistic UI updates and local caching. It mitigates team cloud inexperience through managed serverless components while protecting sensitive PII via secure BFF token handling and encrypted local storage.]