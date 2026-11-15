## Overview
The Customer Web Portal is a React-based single-page application enabling end customers and brokers to submit and manage claims. It integrates with Azure Container Apps and Azure Static Web Apps to modernize access while supporting gradual backend migration.

## Key Elements
- End Customers and Brokers
- Customer Web Portal (SPA/React)
- Authentication Component (TypeScript/MSAL.js)
- Claim Submission Form Component (React/Formik)
- Claim Status & Dashboard Component (React)
- API Gateway Client Component (Axios/Fetch)
- Resilience & Fallback Component
- Corporate Active Directory / Entra ID
- Claims Core API Service (Modular Monolith/.NET)
- Azure Application Insights

## Relationships
- End Customers and Brokers -> Customer Web Portal: Accesses portal UI [HTTPS/REST]
- Customer Web Portal -> Corporate Active Directory / Entra ID: Authenticates users [OIDC/SAML]
- Claim Submission Form Component -> API Gateway Client Component: Sends claim payload [HTTPS/REST]
- Customer Web Portal (Components) -> Claims Core API Service: Submits and retrieves claim data via BFF [HTTPS/REST]
- API Gateway Client Component -> Azure Application Insights: Tracks frontend performance and errors [RUM/Telemetry]

## Technology Stack
- React / TypeScript: Frontend framework for dynamic UI rendering and component architecture
- Backend-for-Frontend (BFF) Pattern: Secures token handling and eliminates browser local storage risks
- Azure Static Web Apps & Azure Container Apps: Hosts static assets and BFF services for operational simplicity
- Azure Application Insights: Provides real user monitoring (RUM) and synthetic transaction logging
- MSAL.js: Implements authentication flows with OIDC/SAML protocols

## Rationale
This component architecture secures user sessions via a BFF pattern, shielding a cloud-inexperienced team from token management risks. It dynamically adapts UI components to support gradual claim type migrations without disrupting users.