## Overview
The system provides a modern hybrid cloud platform that gradually replaces a 30-year-old mainframe while ensuring continuous claim processing. It delivers secure portals for customers, brokers, and adjusters while maintaining seamless interoperability with legacy backends.

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Azure Static Web Apps (Customer Portal & Adjuster Web Apps)
- Authentication Handler Component
- Dynamic Form Engine Component
- API Client & Caching Component
- Broker Context Manager Component
- Local Persistence Queue Component
- Telemetry & RUM Component
- Azure API Gateway with Rate Limiter
- Azure Active Directory / Entra ID
- Azure App Configuration
- Azure Application Insights

## Relationships
- Customers & Brokers -> Azure Static Web Apps: Accesses portal via [HTTPS/OIDC with MFA]
- Claims Adjusters -> Azure Static Web Apps: Accesses web app via [HTTPS/OIDC with MFA]
- Azure Static Web Apps -> Azure API Gateway with Rate Limiter: Routes requests via [HTTPS REST APIs]
- Azure Static Web Apps -> Azure Active Directory / Entra ID: Authenticates users via [OIDC / OAuth 2.0]
- Dynamic Form Engine -> Azure App Configuration: Fetches feature flags via [HTTPS/TLS]
- Telemetry & RUM Component -> Azure Application Insights: Streams performance metrics via [HTTPS]

## Technology Stack
- Azure Static Web Apps: Hosts the Single Page Application with global CDN for instant rollbacks
- .NET 8 / Container Apps: Powers underlying APIs and processing services
- IndexedDB: Provides local persistence queue for offline-resilient claim submissions
- Azure Application Insights: Enables Real User Monitoring (RUM) and distributed tracing
- Playwright: Executes automated synthetic monitoring tests

## Rationale
The architecture decouples the legacy mainframe using an API-driven frontend with aggressive caching and offline queuing to meet strict performance targets (<2s load times). It uses feature flags and atomic CDN deployments to enable gradual claim type migration and rapid 1-day rollbacks.