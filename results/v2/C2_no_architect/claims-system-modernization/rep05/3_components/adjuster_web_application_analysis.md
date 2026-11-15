## Overview
[Modern Claims Platform that gradually replaces a 30-year-old on-premises COBOL/DB2 mainframe claims system with a hybrid cloud architecture in Azure West Europe while ensuring zero downtime.]

## Key Elements
- Claims Adjusters (Primary internal users)
- Adjuster Web Application (React SPA container)
- Backend-For-Frontend (BFF) Container (Node.js)
- Azure Front Door with WAF (Edge routing and security)
- Azure Active Directory / Entra ID (Identity provider)
- Azure Monitor (Observability and audit logging)

## Relationships
- Claims Adjusters -> Adjuster Web Application: Manages claims via UI [HTTPS / TLS 1.3]
- Adjuster Web Application -> Azure Front Door: Accesses web interface [HTTPS]
- Azure Front Door -> BFF Container: Routes API requests and static assets [HTTPS]
- BFF Container -> Azure Active Directory / Entra ID: Authenticates and manages sessions [OAuth2/OIDC]
- BFF Container -> Azure Monitor: Ships audit logs and telemetry [HTTPS / OpenTelemetry]

## Technology Stack
- React: Powers the Adjuster Web Application for high-performance UI rendering
- Node.js: Implements the BFF container for secure session and token management
- Azure Front Door with WAF: Provides edge security, TLS termination, and DDoS protection
- Azure Active Directory (Entra ID): Manages single sign-on and RBAC authorization
- Azure Monitor: Handles distributed tracing and cryptographically verifiable audit logging

## Rationale
[This architecture securely separates frontend presentation from legacy backend complexity while leveraging managed Azure services to compensate for the team's limited cloud experience. Backend-driven session management and edge security protect sensitive PII and financial data without disrupting multi-tab adjuster workflows.]