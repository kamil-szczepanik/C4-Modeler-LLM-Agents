## Overview
This hybrid system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern Azure-based cloud platform. It enables online claim submissions and adjuster workflows while maintaining zero data loss and seamless fallback capabilities.

## Key Elements
- **Users**: Policyholders, Insurance Brokers, Claims Adjusters
- **External Systems**: COBOL/DB2 Mainframe, On-Premise Active Directory / Entra ID
- **Containers**: Azure API Gateway & WAF, Azure Container Apps / App Service, Azure SQL Database, Azure Active Directory / Entra ID, Azure Application Insights, Azure Key Vault, Azure Blob Storage
- **Components**: Azure SQL Database (Primary operational data store)

## Relationships
- Azure API Gateway & WAF -> Azure Container Apps: Forwards HTTP/HTTPS traffic [TLS]
- Azure Container Apps -> Azure SQL Database: Data persistence and queries [TLS 1.2+]
- Azure Container Apps -> Azure Active Directory / Entra ID: Single Sign-On and authentication [OAuth 2.0 / OIDC]
- Azure SQL Database -> Azure Key Vault: Transparent Data Encryption key retrieval [HTTPS]
- Azure SQL Database -> Azure Blob Storage: Historical claim data offloading [HTTPS]

## Technology Stack
- **Azure SQL Database**: Hyperscale/Serverless tiers chosen for automatic scaling and built-in HA/DR.
- **Azure AD (Entra ID)**: Enforces SSO and centralized RBAC to secure access.
- **Azure Key Vault**: Secures Customer-Managed Keys (CMK) for data encryption at rest.
- **Bicep / Terraform**: Implements Infrastructure-as-Code for repeatable cloud deployments.
- **Azure DevOps**: Automates CI/CD pipelines with rollback capabilities for quick fallbacks.

## Rationale
This architecture fits requirements by isolating complex migration risks behind a hybrid boundary while ensuring sub-2-second adjuster response times via Azure SQL caching. Strict automated backups and geo-replication guarantee zero data loss and satisfy all compliance and security constraints.