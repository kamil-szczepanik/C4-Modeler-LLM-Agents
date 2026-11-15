## Overview
[The system modernizes a regional insurer's 30-year-old mainframe claims system through a hybrid cloud migration platform. It provides online claim submission and adjuster workspaces while maintaining consistency and zero data loss.]

## Key Elements
*   Azure Static Web Apps / Azure App Service (Hosting Platform)
*   Next.js SSR / API Routes Component (Frontend and BFF layer)
*   Claim Type Feature Flags Component (Dynamic UI routing)
*   OpenTelemetry Integration Component (Distributed tracing)
*   Azure API Management (API gateway)
*   Azure App Configuration (Feature flag and toggle management)
*   Azure Application Insights (APM and monitoring)

## Relationships
*   Next.js SSR Component -> Azure API Management: Forwards domain requests via HTTPS / REST
*   Claim Type Feature Flags Component -> Azure App Configuration: Fetches migration metadata via HTTPS / REST
*   Next.js SSR Component -> Azure Application Insights: Exports telemetry and tracing data via OpenTelemetry protocol

## Technology Stack
*   Next.js: Combines React frontend and server-side rendering for <2s adjuster screen loads
*   Azure Static Web Apps / Azure App Service: Managed PaaS to reduce infrastructure overhead for a cloud-inexperienced team
*   Azure App Configuration: Centralized store for instant claim type toggling and 1-day mainframe fallback
*   OpenTelemetry / Application Insights: Distributed tracing to isolate legacy mainframe latency

## Rationale
[This architecture minimizes operational complexity for a cloud-inexperienced team by leveraging managed Azure PaaS services and integrated Next.js capabilities. It guarantees the required sub-2-second performance and supports gradual, risk-controlled claim type migration with rapid fallback options.]