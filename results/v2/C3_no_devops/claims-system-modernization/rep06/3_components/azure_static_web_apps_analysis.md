## Overview
[The system modernizes a 30-year-old regional insurance claims mainframe by gradually migrating claim types to a hybrid cloud platform while ensuring uninterrupted legacy processing.]

## Key Elements
- Azure Static Web Apps (Angular/React SPA frontend)
- SPA Router & View Modules
- Auth & Session Manager
- API Proxy / Fallback
- Configuration & Feature Flag Service
- Telemetry Client
- Azure API Management (APIM)
- Azure Entra ID / Active Directory

## Relationships
- End Customers, Brokers, Claims Adjusters, Operations Managers, Migration Admins -> Azure Static Web Apps [HTTPS]
- SPA Router -> Auth & Session Manager [In-memory / HTTPS]
- SPA Router -> API Proxy [HTTPS]
- API Proxy -> Azure API Management [HTTPS / REST APIs]
- Auth & Session Manager -> Azure Entra ID [OAuth / OIDC]
- Telemetry Client -> Azure Application Insights [HTTPS]

## Technology Stack
- Azure Static Web Apps: Manages frontend hosting and global delivery to reduce operational overhead for a low-cloud-experience team.
- Angular/React: Powers dynamic single-page application interfaces and role-based routing.
- Azure Entra ID: Provides single sign-on (SSO) integration using built-in SWA authentication.
- Azure Application Insights: Tracks real-user metrics (RUM) and performance for adjuster screens.

## Rationale
[This architecture uses managed cloud services to minimize infrastructure complexity for an inexperienced team while providing robust security controls and gradual migration paths. It guarantees low-latency user interfaces and strict data protection without altering the core mainframe processing window.]