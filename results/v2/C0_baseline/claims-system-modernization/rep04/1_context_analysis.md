## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure-hosted platform while maintaining continuous legacy operations. It ensures zero data loss, supports incremental claim migrations, and enables rapid rollbacks within a hybrid cloud architecture.

## Key Elements
- **Customers (Policyholders):** External users submitting claims online.
- **Brokers:** External partners submitting and tracking claims.
- **Claims Adjusters:** Internal users processing claims via the web application.
- **Insurance Claims Modernization Platform:** Core containerized system hosted in Azure West Europe using PaaS/Serverless.
- **Legacy Mainframe:** On-premises COBOL/DB2 system of record.
- **Identity Provider:** Active Directory / Microsoft Entra ID for authentication.

## Relationships
- **Customer / Broker / Claims Adjuster -> Modernization Platform:** HTTPS / TLS 1.3 via Azure Front Door and Web UI.
- **Modernization Platform <-> Identity Provider:** OIDC / OAuth 2.0 for Single Sign-On (SSO).
- **Modernization Platform <-> Legacy Mainframe:** Azure ExpressRoute and mutual TLS (mTLS) with an internal Anti-Corruption Layer (ACL).

## Technology Stack
- **Azure App Service / Azure SQL:** Managed PaaS chosen to reduce operational burden for a team with limited cloud experience.
- **Azure Front Door:** Global load balancing and HTTPS termination ensuring UI performance.
- **Microsoft Entra ID:** OAuth 2.0 / OIDC provider meeting enterprise security and SSO requirements.
- **Azure DevOps & ArgoCD:** GitOps tooling ensuring automated deployments and contract testing.
- **Azure Key Vault:** Secret management with automated key rotation across the hybrid boundary.
- **Azure Application Insights:** Distributed tracing for performance and latency isolation.

## Rationale
The hybrid architecture protects business continuity by keeping the stable mainframe as the system of record while incrementally migrating claim types. Azure PaaS mitigates the team's limited cloud experience while satisfying stringent performance, security, and rollback requirements.