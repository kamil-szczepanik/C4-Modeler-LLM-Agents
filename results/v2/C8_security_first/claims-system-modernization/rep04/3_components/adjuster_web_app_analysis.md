## Overview
The Adjuster Web App is a modern web interface hosted in Azure Container Apps that enables insurance claims adjusters to process claims efficiently during a hybrid mainframe migration. It communicates securely via Azure API Management and a Backend-for-Frontend to bridge modern cloud infrastructure with the legacy system of record.

## Key Elements
- Claims Adjuster (User)
- Adjuster Web App (Azure Container Apps / React SPA)
- Backend-for-Frontend (BFF) (Azure Container Apps)
- Azure Active Directory / Entra ID (Identity Provider)
- Azure Application Insights & Azure Monitor (Observability)
- Azure App Configuration (Feature Flags)

## Relationships
- Claims Adjuster -> Adjuster Web App: Reviews and processes claims [HTTPS]
- Adjuster Web App -> Backend-for-Frontend (BFF): Requests claim data and workflows [HTTPS / gRPC via Azure Managed Identities]
- Adjuster Web App -> Azure Active Directory / Entra ID: Authenticates users and manages SSO/OIDC lifecycle [OIDC / OAuth2]
- Adjuster Web App -> Azure Application Insights: Transmits distributed traces and client telemetry [HTTPS]

## Technology Stack
- React / TypeScript: Component architecture for high performance and maintainability
- Azure Container Apps: Container hosting chosen for ease of deployment given team's low cloud experience
- Azure App Configuration: Dynamic feature flagging for rapid R-06 rollback requirements
- Azure Application Insights: Distributed tracing to monitor R-05 sub-2-second load times

## Rationale
This component architecture separates the frontend presentation layer from backend complexity, enabling sub-second UI rendering despite slow legacy mainframe dependencies. It prioritizes operational simplicity for a team with low cloud experience while ensuring robust security and regulatory compliance.