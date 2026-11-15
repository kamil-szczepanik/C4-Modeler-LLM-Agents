## Overview
[The system is an Insurance Claims Modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure-based cloud architecture. It ensures seamless hybrid operations for customer claim submissions and adjuster workflows while maintaining strict consistency and security.]

## Key Elements
- End Customers & Brokers
- Claims Adjusters
- API Gateway (Azure API Management / NGINX)
- Customer Portal (React / Node.js)
- Adjuster Workspace (React / .NET Core API)
- Integration & Anti-Corruption Layer (.NET Core / MassTransit)
- Configuration & Feature Store (Azure App Configuration / Redis)
- Corporate Active Directory
- Azure Key Vault
- Legacy Mainframe

## Relationships
- End Customers & Brokers -> API Gateway: Accesses portal and submits claims [HTTPS/REST]
- Claims Adjusters -> API Gateway: Accesses adjuster workspace and processes claims [HTTPS/REST]
- API Gateway -> Corporate Active Directory: Validates SSO and authentication [OIDC/OAuth2]
- API Gateway -> Configuration & Feature Store: Fetches active routing rules [Internal HTTPS/REST, cached locally]
- API Gateway -> Azure Key Vault: Retrieves certificates and OAuth secrets [Azure Managed Identity / HTTPS]
- API Gateway -> Integration Layer: Forwards traffic with injected W3C trace context [mTLS / gRPC]

## Technology Stack
- Azure API Management: Provides dynamic path-based routing, WAF integration, and rate limiting
- Azure App Configuration & Redis: Stores feature flags and cached routing rules for rapid claim rollbacks
- .NET Core & MassTransit: Powers backend APIs and the Integration/Anti-Corruption Layer
- Azure Key Vault: Manages secrets and certificates securely using Managed Identities

## Rationale
[This hybrid architecture isolates the expensive legacy mainframe behind an Anti-Corruption Layer while using dynamic API Gateway routing to migrate claim types incrementally. It satisfies non-functional requirements for low latency, secure SSO integration, zero data loss, and rapid one-day rollbacks.]