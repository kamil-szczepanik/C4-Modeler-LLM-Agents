## Overview
[A hybrid cloud platform gradually modernizing a 30-year-old regional insurer mainframe claims system while maintaining business continuity.]

## Key Elements
- Claims Web Application (React SPA / Azure App Service)
- BFF Routing & Session Controller (Node.js/Express)
- Claim Workspace UI (React/TypeScript)
- Local State & Sync Manager (IndexedDB / Workbox / Web Crypto API)
- Client-Side Validation & Mapping Engine (TypeScript / Zod)
- Telemetry & Error Boundary Component (React / OpenTelemetry Web)
- External Systems: Microsoft Entra ID, API Gateway, Legacy Mainframe

## Relationships
- Claims Adjusters -> Claims Web Application: HTTPS/REST
- Claim Workspace UI -> BFF Routing & Session Controller: HTTPS/REST
- BFF Routing & Session Controller -> API Gateway: HTTPS/REST
- Claim Workspace UI -> Client-Side Validation & Mapping Engine: In-memory TS

## Technology Stack
- Azure App Service: Unified hosting for React SPA and Node.js BFF to minimize operational complexity for cloud-novice teams.
- React / TypeScript: Modern UI framework supporting WCAG 2.1 AA accessibility and rapid adjuster workflows.
- Web Crypto API & IndexedDB: Client-side storage with encrypted payload caching to handle intermittent connectivity.
- Azure App Configuration: Dynamic feature flagging for rapid claim-type migration and one-day switch-backs.
- OpenTelemetry & Application Insights: Distributed tracing and proactive health monitoring across hybrid lag.

## Rationale
[This hybrid architecture securely accelerates claims processing and phased migration while protecting legacy data constraints and minimizing operational overhead for a cloud-novice team.]