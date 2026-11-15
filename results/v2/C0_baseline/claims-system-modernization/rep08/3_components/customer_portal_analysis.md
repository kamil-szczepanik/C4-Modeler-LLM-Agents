## Overview
- Modernizes a 30-year-old mainframe claims system via a hybrid cloud platform while ensuring uninterrupted legacy processing.
- Delivers secure online claim submissions and self-service tracking for customers and brokers.

## Key Elements
- Customers and Brokers
- Customer Portal (React, TypeScript, Azure CDN)
- API Gateway / Backend-for-Frontend (.NET 8 Web API)
- Corporate Active Directory & Azure Entra ID
- Azure Application Insights (Browser SDK)
- Azure Web Application Firewall (WAF)

## Relationships
- Customers and Brokers -> Customer Portal: Accesses portal to submit and track claims [HTTPS / Azure CDN]
- Customer Portal -> API Gateway / Backend-for-Frontend: Makes API requests [HTTPS / REST]
- Customer Portal -> Corporate Active Directory & Azure Entra ID: Authenticates via Single Sign-On [OAuth 2.0 / OIDC / MSAL.js]
- Customer Portal -> Azure Application Insights: Sends client-side telemetry [HTTPS]
- Azure WAF -> Customer Portal: Inspects and filters incoming traffic [HTTPS]

## Technology Stack
- React with TypeScript: Chosen for building a responsive, maintainable single-page application within the team's skillset.
- Azure CDN: Selected for globally distributing static assets with low latency.
- MSAL.js: Utilized for secure OAuth 2.0 / OIDC single sign-on integration.
- Azure Application Insights: Deployed for client-side error and performance observability.
- Azure WAF: Implemented for edge protection against bots and web attacks.

## Rationale
- Isolates complex legacy mainframe dependencies behind an API Gateway to maintain stable 3-year migration timelines.
- Employs lightweight cloud-native components matching the team's experience while ensuring robust security and performance.