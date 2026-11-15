## Overview
[The system modernizes a 30-year-old regional insurance mainframe platform by introducing cloud-based web portals while maintaining core legacy processing. It uses a hybrid architecture to gradually migrate claim types over three years without disrupting existing business operations.]

## Key Elements
* Customer & Broker Portal SPA (React.js)
* Adjuster Workspace SPA (React.js)
* Authentication & Session Manager (MSAL.js / OAuth2 / OIDC)
* API Client & Caching Layer (Axios / React Query)
* Azure Static Web Apps
* Azure API Management
* Azure Application Insights

## Relationships
* Customer & Broker Portal SPA -> Azure API Management via HTTPS / REST (JSON)
* Adjuster Workspace SPA -> Azure API Management via HTTPS / REST (JSON)
* SPAs -> Corporate Identity Provider via HTTPS / OpenID Connect
* SPAs -> Azure Application Insights via HTTPS (Telemetry)

## Technology Stack
* React.js: Selected for building modular, responsive single-page applications for users and adjusters.
* Azure Static Web Apps: Chosen for cost-effective global hosting, native GitHub Actions CI/CD, and staging environments supporting rapid rollbacks.
* React Query & Axios: Implemented for client-side state management, caching, and mitigating mainframe latency.
* MSAL.js: Utilized for secure Single Sign-On integration with Active Directory.
* Azure Application Insights: Deployed for Real User Monitoring and frontend error tracking.

## Rationale
[This architecture fits the requirements by decoupling the user experience from the legacy mainframe, using caching to meet strict performance targets. Furthermore, it leverages managed Azure services to compensate for the team's limited cloud experience while ensuring seamless gradual migration and rollback capabilities.]