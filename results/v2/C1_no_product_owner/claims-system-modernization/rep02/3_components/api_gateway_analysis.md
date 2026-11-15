## Overview
- Replaces a legacy COBOL/DB2 mainframe claims system with a hybrid cloud platform on Azure while maintaining uninterrupted operations.
- Utilizes Azure API Management as a secure, managed edge gateway for online claims submission and adjuster workflows.

## Key Elements
- Azure API Management (APIM): Fully managed PaaS API Gateway enforcing security, routing, and rate limiting.
- Customer Portal & Adjuster Workspace: Frontend web applications built on React and Azure Container Apps/Static Web Apps.
- Adjuster Backend Service & Mainframe Integration Adapter: Internal Azure Container Apps handling business logic and legacy communication.
- Azure Key Vault: Secure storage for mTLS certificates and backend credentials using managed identities.
- Azure Redis Cache & Azure Application Insights: Distributed caching for rate-limiting and telemetry/distributed tracing.

## Relationships
- Customer Portal / Adjuster Workspace -> Azure API Management: Sends signed API requests [HTTPS/JSON]
- Azure API Management -> Identity Provider: Validates OAuth2/OIDC tokens [OAuth2/OIDC]
- Azure API Management -> Adjuster Backend Service: Forwards requests with injected user claims [HTTPS/mTLS]
- Azure API Management -> Mainframe Integration Adapter: Routes unmigrated traffic [HTTPS/mTLS]

## Technology Stack
- Azure API Management: Managed gateway providing JWT validation, rate limiting, and WAF to reduce custom infrastructure overhead.
- Azure Key Vault: Secures secrets and mTLS certificates via managed identities, preventing hardcoded credentials.
- Bicep / Terraform: Infrastructure as Code for defining APIM policies and routing to prevent configuration drift.
- Azure Application Insights: Provides distributed tracing and OpenTelemetry correlation to meet latency tracking requirements.

## Rationale
- The hybrid architecture leverages managed Azure services to minimize operational complexity for a team with limited cloud experience.
- API Management policies and mTLS ensure strict security and seamless traffic shifting between the cloud backend and the legacy mainframe.