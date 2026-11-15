## Overview
The Adjuster Web Application modernizes the regional insurer's claims platform via a React single-page application hosted on Azure Static Web Apps. It interfaces with a Node.js API Gateway to process claims while safely coexisting with the legacy COBOL/DB2 mainframe.

## Key Elements
- Claim Workspace Router & State Manager (React Context / Zustand)
- Claim Details View Component (React)
- Auth Guard Component (MSAL.js)
- Inline Audit & Exception Flagging Component (React with React Hook Form & Zod)
- API Gateway / Backend-for-Frontend (Node.js / NestJS)
- Insurer's Active Directory / Azure AD

## Relationships
- Claims Adjusters -> Adjuster Web Application: Interacts with web app via HTTPS/JSON
- Adjuster Web Application -> API Gateway / BFF: Communicates for data/operations via HTTPS/REST and WebSockets
- Adjuster Web Application -> Insurer's Active Directory / Azure AD: Authenticates via OAuth2/OpenID Connect

## Technology Stack
- React SPA: Chosen for responsive UI components and developer familiarity.
- Azure Static Web Apps: Selected for globally distributed, zero-downtime deployments.
- Zustand & React Context: Utilized for high-performance local UI state management and optimistic updates.
- MSAL.js: Implements secure Single Sign-On via OAuth2/OIDC.
- Zod & React Hook Form: Ensures rigorous client-side validation for exception reports.
- Azure Application Insights & Playwright: Mandated for synthetic monitoring and telemetry to guarantee sub-2s load times.

## Rationale
This architecture decouples the responsive user interface from slow legacy backend responses using optimistic updates and caching. It ensures strict security, maintainability, and auditability during the hybrid migration phase.