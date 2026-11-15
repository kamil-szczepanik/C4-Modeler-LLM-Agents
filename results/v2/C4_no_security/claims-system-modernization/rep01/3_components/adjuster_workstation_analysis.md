## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe claims platform with a modern cloud-native solution. It ensures seamless, hybrid claims processing for policyholders, brokers, and internal adjusters over a three-year migration period.

## Key Elements
- Claims Adjusters (Internal Users)
- Adjuster Workstation (React SPA, Azure Static Web Apps)
- Adjuster BFF (.NET / C#, Azure App Service)
- Microsoft Entra ID (Identity Provider)
- Azure API Management (API Gateway)
- Claims Dashboard Component
- State & Real-Time Sync Component
- Claim Action & Form Engine Component
- Auth & Session Manager Component

## Relationships
- Claims Adjusters -> Adjuster Workstation: Interacts with UI via HTTPS
- Adjuster Workstation -> Azure API Management: Routes web requests via HTTPS
- Azure API Management -> Adjuster BFF: Forwards internal domain API traffic via HTTPS
- Adjuster Workstation -> Adjuster BFF: Receives real-time updates via Server-Sent Events (SSE)
- Auth & Session Manager -> Microsoft Entra ID: Authenticates users via OIDC/OAuth2 over HTTPS

## Technology Stack
- React SPA: Frontend framework for high-performance rendering
- Azure Static Web Apps: Global CDN hosting for the SPA to optimize performance and reduce cold starts
- .NET / C#: Backend BFF framework
- Server-Sent Events (SSE): Real-time migration status updates without polling overhead
- Azure Application Insights: Real User Monitoring (RUM) for Core Web Vitals tracking
- Microsoft Entra ID: Single Sign-On integration for enterprise security

## Rationale
This architecture utilizes a React SPA hosted on Azure Static Web Apps to guarantee sub-2-second adjuster screen loads despite legacy backend latency. Decoupling the frontend via an asynchronous BFF and SSE sync isolates the cloud team from expensive mainframe changes and ensures a reliable one-day fallback capability.