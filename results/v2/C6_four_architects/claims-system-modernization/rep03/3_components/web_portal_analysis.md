## Overview
- Modernizes a legacy insurance claims platform by introducing a cloud-based web portal while keeping the mainframe system of record.
- Provides a secure, performant, and localized interface for customers and brokers to submit and track claims.

## Key Elements
- Web Portal Container (React / TypeScript on Azure Static Web Apps)
- Authentication Context / SSO Module (MSAL.js)
- Claim Submission Wizard (React Hook Form and Zod)
- Claim Tracking Dashboard
- Local State & Cache Manager (TanStack Query / React Query)
- BFF API Client Layer (Axios/Fetch)
- Localization Provider (`i18next`)
- Security Headers & CSP Enforcer (`staticwebapp.config.json`)
- External Active Directory (Azure AD)
- API Gateway / BFF (Azure API Management and Node.js)

## Relationships
- Customer / Broker -> Web Portal Container: Interacts with unified web interface [HTTPS]
- Authentication Context -> External Active Directory: Authenticates via OIDC [HTTPS via Azure AD]
- Claim Submission Wizard & Claim Tracking Dashboard -> Local State & Cache Manager: Manages server state [TypeScript Module Call]
- Local State & Cache Manager -> BFF API Client Layer: Fetches data [TypeScript Module Call]
- Web Portal Container -> API Gateway / BFF: Sends requests to BFF [HTTPS]
- Web Portal Container -> Azure Static Web Apps Runtime: Applies security headers [HTTP Security Headers / CSP]

## Technology Stack
- React 18 with TypeScript: Ensures fast SPA routing and maintainability for teams with limited cloud experience.
- Azure Static Web Apps: Delivers global low latency with zero server infrastructure management.
- TanStack Query: Caches server state locally to maintain sub-second UI responsiveness despite slow backend/mainframe responses.
- MSAL.js & Azure AD: Implements single sign-on for enterprise security compliance.
- `i18next`: Provides lightweight multi-language support for regional compliance.

## Rationale
- This architecture isolates the complex legacy mainframe behind an API gateway while delivering a responsive, secure frontend experience.
- It leverages managed cloud services to accommodate the team's limited cloud expertise while meeting strict performance and security requirements.