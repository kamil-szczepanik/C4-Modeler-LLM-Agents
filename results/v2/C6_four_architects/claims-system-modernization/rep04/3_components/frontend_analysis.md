## Overview
This system modernizes a 30-year-old regional insurer mainframe claims platform by gradually migrating claim types to a hybrid cloud architecture. It maintains business continuity, a strict nightly batch window, and zero claim loss during the transition.

## Key Elements
- Users: Customers, Brokers, Claims Adjusters
- Frontend Container: React Single Page Application hosted on Azure Static Web Apps
- Frontend Components: Auth Module (MSAL.js), Customer Portal UI, Adjuster Workspace UI, State Management Store (React Query), API Client (Axios), Feature Flag & Routing Engine, Error Boundary & Fallback Handler
- Edge Tier: Azure API Management, Node.js / TypeScript
- Application Tier: Java / Spring Boot, Azure Functions (Python/C#), Azure Container Apps
- Data & Integration Tier: Azure Database for PostgreSQL, Azure Service Bus, Azure Relay
- Legacy System: IBM DB2 / COBOL Mainframe (On-Premises System of Record)

## Relationships
- Customers, Brokers, Adjusters -> Frontend: Accesses claims system via browser [HTTPS]
- Frontend -> Edge Tier: Sends API requests and authenticates [HTTPS / OIDC]
- Frontend -> Azure Active Directory (Entra ID): Authenticates users [OAuth2 / OIDC]
- Application Tier -> Hybrid Bridge / Mainframe: Syncs transactional data [Azure Service Bus / Azure Relay]

## Technology Stack
- Frontend: React on Azure Static Web Apps for lightweight, globally distributed SPA hosting suited for cloud-inexperienced teams
- State Management: React Query to cache server state and enable optimistic UI updates
- Security: MSAL.js integrated with Azure AD for Single Sign-On (SSO)
- Integration: Azure API Management and Azure Service Bus for hybrid messaging and routing

## Rationale
The hybrid architecture protects high-cost legacy mainframe investments while enabling a gradual, low-risk migration of claim types. Local caching and optimistic UI updates mask legacy mainframe latency to meet strict performance targets.