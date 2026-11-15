## Overview
[Component-level architecture summary for the Customer Portal within the hybrid cloud claims modernization platform.]
[Ensures secure, observable, and reliable online claim submissions for customers and brokers.]

## Key Elements
- Authentication Component (MSAL.js)
- Claim Submission UI Component (React Components)
- API Client Component (Axios/Fetch)
- Telemetry & Error Boundary Component (Application Insights React SDK)

## Relationships
- Claim Submission UI Component -> API Client Component: Invoke API calls [In-memory / JS]
- API Client Component -> API Gateway: Submit claim data [HTTPS/JSON]
- Claim Submission UI Component -> Telemetry & Error Boundary Component: Report errors/telemetry [In-memory / JS]
- Authentication Component -> API Client Component: Provide Bearer token [In-memory / JS]

## Technology Stack
- Azure Static Web Apps: Hosts React SPA with global CDN distribution and staging environments.
- MSAL.js / OpenID Connect: Integrates SSO with Active Directory.
- Application Insights React SDK: Captures client-side exceptions and performance metrics.
- Bicep/Terraform & GitHub Actions: Manages infrastructure-as-code and automated pipelines.

## Rationale
[Adheres to limited cloud experience via managed PaaS services and robust telemetry.]
[Enforces strict security policies like memory-only token storage to protect sensitive PII.]