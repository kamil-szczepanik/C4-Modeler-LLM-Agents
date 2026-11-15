## Overview
The system is a hybrid cloud insurance claims modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure-based architecture. Its core purpose is to enable online claim submission and adjuster workflows while maintaining seamless data consistency and zero downtime during the multi-year migration.

## Key Elements
- Claims API Gateway: Azure API Management (APIM)
- JWT Validation Policy Component: Validates tokens against Azure AD / Entra ID
- Rate Limiting & Throttling Component: APIM Policy enforcing persona-based quotas
- Claims-Based Authorization Policy Component: Enforces RBAC separation
- mTLS & Secure Connector Component: Manages certificate-based outbound trust
- Distributed Tracing Injector Component: Injects OpenTelemetry correlation headers
- Health Probing & Automated Failover Component: APIM backend probes and circuit breaker
- API Security Gateway Policies: OWASP Top 10 payload validation and sanitization
- Upstream Systems: Core Claims Service (Azure Container Apps) and Mainframe ACL (Azure Event Hubs)

## Relationships
- Web Frontend (SPA) -> Claims API Gateway: Sends API requests via [HTTPS / REST]
- Claims API Gateway -> Core Claims Service: Routes authenticated requests via [gRPC / internal HTTPS with mTLS]
- Claims API Gateway -> Mainframe ACL: Forwards fallback requests via [HTTPS with mTLS]
- Claims API Gateway -> Azure AD / Entra ID: Validates tokens via [OAuth2 / OpenID Connect]
- Claims API Gateway -> Azure App Configuration: Evaluates cached feature flags via [HTTPS]

## Technology Stack
- Azure API Management (APIM): Core gateway container for centralized routing and security policies
- Azure AD / Entra ID: Identity provider for Single Sign-On and JWT validation
- Azure App Configuration: Backs dynamic feature flags for claim type routing and 1-day fallback
- OpenTelemetry: Distributed tracing standard for cross-boundary observability
- Bicep: Infrastructure-as-Code for reproducible deployments and automated config rollbacks
- gRPC / HTTPS: Secure protocols for high-performance service-to-service and hybrid communication

## Rationale
This architecture uses an API Gateway pattern to abstract the hybrid migration complexity, ensuring the UI remains decoupled from backend shifts between the mainframe and Azure. Persona-based routing, automated failovers, and rigorous Infrastructure-as-Code enforce the strict 1-day rollback and sub-2-second performance requirements while mitigating the team's low cloud experience.