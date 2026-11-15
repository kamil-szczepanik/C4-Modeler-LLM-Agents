## Overview
The Claims Adjuster Web App provides a modern interface for claims handlers to process policies within a hybrid cloud architecture. It bridges legacy mainframe systems with Azure services while maintaining sub-second performance.

## Key Elements
- Claims Adjuster Web App (Azure Container Apps)
- API Gateway (Azure Container Apps)
- Integration/Messaging Container (Azure Service Bus)
- Audit & Reconciliation Container (Azure Container Apps)
- Azure Active Directory (Entra ID)
- On-Premises COBOL/DB2 Mainframe

## Relationships
- Claims Adjuster -> Claims Adjuster Web App: Authenticates and accesses adjuster workflows via [HTTPS / TLS 1.3]
- Claims Adjuster Web App -> Azure Active Directory (Entra ID): Validates OIDC / OAuth 2.0 authentication tokens [HTTPS]
- Claims Adjuster Web App -> API Gateway: Routes claims processing requests via [mTLS / Azure Entra Managed Identities]
- Claims Adjuster Web App -> Integration/Messaging Container: Publishes asynchronous claim events via [Azure Service Bus Protocol]
- Claims Adjuster Web App -> Audit & Reconciliation Container: Streams tamper-evident audit logs via [HTTPS / TLS 1.3]

## Technology Stack
- Azure Container Apps: Chosen for scalable containerized hosting, accommodating the team's low cloud experience via declarative Bicep IaC.
- Azure Key Vault: Utilized with Managed Identities for secure runtime secret management without hardcoded credentials.
- OpenTelemetry & Azure Application Insights: Implemented for distributed tracing and correlation ID generation to isolate hybrid performance bottlenecks.
- JWT & RBAC: Applied for fine-grained application-level authorization and access control based on adjuster permissions.

## Rationale
This architecture ensures seamless hybrid operation and strict data consistency during the 3-year migration from the legacy mainframe. It provides enterprise-grade security and observability while mitigating the team's limited cloud experience through managed Azure services and Infrastructure as Code.