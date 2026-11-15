## Overview
[The Customer Portal container is a React-based single-page application deployed on Azure Static Web Apps, enabling online claim submission and tracking for customers and brokers. It acts as the modern frontend interface for the hybrid cloud Insurance Claims Modernization platform.]

## Key Elements
* Authentication Controller (React Router / OIDC client library)
* Claim Submission Form (React Component)
* Claim Status Viewer (React Component with Broker Workspace View)
* Draft Management Component (React / Encrypted IndexedDB)
* API Gateway Client (TypeScript / Axios)
* Application Insights Frontend SDK
* Azure Static Web Apps
* Microsoft Entra ID
* Azure API Management

## Relationships
* Customer / Broker -> Customer Portal: Accesses web interface via HTTPS/REST
* Authentication Controller -> Microsoft Entra ID: Authenticates users via OpenID Connect (OIDC)
* Claim Submission Form, Claim Status Viewer, Draft Management Component -> API Gateway Client: Sends/retrieves data locally
* API Gateway Client -> Azure API Management: Communicates securely via HTTPS/REST

## Technology Stack
* React: Frontend component architecture for team familiarity and rapid UI delivery
* Azure Static Web Apps: Minimizes operational overhead for a cloud-inexperienced team
* IndexedDB with Web Crypto API (PBKDF2): Secure local offline draft persistence for R-01 resilience
* Application Insights (Frontend SDK): Real User Monitoring (RUM) and synthetic testing for reliability (R-04)

## Rationale
[This architecture minimizes operational complexity for a team with limited cloud experience by leveraging managed serverless hosting on Azure Static Web Apps. It balances strict security and compliance controls with robust offline and performance features required for modern claim submissions.]