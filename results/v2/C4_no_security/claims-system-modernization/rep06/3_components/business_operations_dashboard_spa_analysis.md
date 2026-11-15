## Overview
[The Business Operations Dashboard SPA provides real-time visibility into the migration of insurance claim types from a legacy mainframe to Azure. It enables operations managers to monitor transaction volumes, ensure data consistency, and execute rapid switchbacks if anomalies occur.]

## Key Elements
- Operations Managers and Migration Leads (Users)
- Business Operations Dashboard SPA (Azure Static Web Apps)
- Dashboard Router & State Manager (React Router, TanStack Query)
- Migration Metrics View & Switchback Alert Monitor (React Components)
- Audit & Reconciliation Inspector (React Component)
- API Client Service & Telemetry Service (Axios, Azure Application Insights JS SDK)

## Relationships
- Operations Managers -> Business Operations Dashboard SPA: Accesses migration metrics and switchback alerts [HTTPS / Browser]
- API Client Service -> Azure API Management: Fetches operational telemetry and reconciliation data [HTTPS / REST, JWT-secured]
- Telemetry Service -> Azure Application Insights: Streams client-side errors and performance logs [HTTPS]

## Technology Stack
- Azure Static Web Apps: Hosts the SPA with built-in global CDN distribution and staging slots to minimize cloud management complexity
- React / TypeScript: Provides robust typing and rich data visualization libraries for migration tracking
- TanStack Query: Manages server state and polling intervals for real-time health checks
- Azure Application Insights JS SDK: Captures unhandled exceptions and client-side error visibility

## Rationale
[This architecture provides lightweight, decoupled observability specifically tailored for monitoring hybrid cloud migration risks. It empowers management with real-time health indicators to safely maintain dual-platform operations and execute rapid switchbacks within required SLAs.]