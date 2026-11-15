## Overview
The Insurance Claims Modernization system replaces a 30-year-old COBOL/DB2 mainframe with a cloud-native Azure platform. It enables gradual claim type migration while maintaining hybrid synchronization and zero data loss.

## Key Elements
- **Customer Portal**: React SPA hosted on Azure Static Web Apps for customers and brokers.
- **Authentication Component**: MSAL.js with PKCE and Azure Active Directory / Entra ID.
- **Claim Submission Module**: Multi-step React form for online claims (R-01).
- **Claim Status Tracker**: Real-time status display via BFF.
- **API Client Layer**: Axios-based communication module.
- **Telemetry Component**: Azure Application Insights React plugin with PII masking.
- **State & Routing Core**: React Router for protected route guarding.
- **Error Boundaries**: Top-level React crash fallback handlers.

## Relationships
- **Customer / Broker** -> **Authentication Component**: Authenticates via [HTTPS]
- **State & Routing Core** -> **Claim Submission Module**: Coordinates navigation via [Internal React Context]
- **API Client Layer** -> **Claims API Gateway**: Sends REST payloads via [HTTPS/REST]
- **Telemetry Component** -> **Azure Monitor / Application Insights**: Streams sanitized traces via [HTTPS]

## Technology Stack
- **React SPA**: Frontend UI framework for modular user interfaces.
- **Azure Static Web Apps**: Hosting platform providing global CDN distribution and automated GitHub Actions preview environments.
- **MSAL.js**: Authentication library implementing Authorization Code Flow with PKCE and in-memory token storage.
- **Azure Application Insights**: Telemetry and error tracking tool with custom PII scrubbing interceptors.
- **Azure API Management & App Service**: Backend integration tier supporting legacy migration constraints.

## Rationale
This architecture ensures secure, low-overhead cloud adoption for a team with limited cloud experience by leveraging managed Azure PaaS services. Client-side security hardening and strict telemetry sanitization protect sensitive PII while supporting reliable hybrid claims processing.