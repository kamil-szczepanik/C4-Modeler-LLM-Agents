## Overview
This hybrid claims modernization platform gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure-hosted web application. It processes claims consistently and securely while keeping the mainframe as the system of record.

## Key Elements
- Policyholders and Insurance Brokers (External Users)
- Claims Adjusters and Operations Managers (Internal Users)
- COBOL/DB2 Mainframe (On-Premise System of Record)
- Azure API Gateway & WAF
- Azure Container Apps / App Service
- Azure SQL Database
- Azure Active Directory / Entra ID (with B2B/B2C and FIDO2 MFA)
- Azure Application Insights
- Azure Key Vault

## Relationships
- External Users to Azure API Gateway & WAF: HTTPS via TLS 1.3 for online claim submission (R-01)
- Internal Users to Azure API Gateway & WAF: HTTPS via TLS 1.3 for adjuster web application (R-02)
- Azure API Gateway & WAF to Azure Container Apps: Internal routing with JWT validation
- Azure Container Apps to Azure SQL Database: Entity Framework Core via encrypted connection strings
- Azure Container Apps to COBOL/DB2 Mainframe: Batch/sync interfaces via secure protocols
- Azure Container Apps to Azure Active Directory / Entra ID: OAuth 2.0 / OIDC for authentication (R-07)
- Azure Container Apps to Azure Key Vault: Managed Identities for secret retrieval

## Technology Stack
- Hybrid Cloud Architecture: Azure West Europe and On-Premise Mainframe to support incremental migration constraints
- Azure Active Directory / Entra ID & External ID: Single Sign-On (R-07) and user segmentation for internal staff and external brokers/policyholders
- Azure API Gateway & WAF: Local JWT validation via cached JWKS for performance and resilience
- Azure Container Apps: Hosting modern microservices with low cloud-experience overhead
- Azure SQL Database: Transactional persistence ensuring exactly-once processing (R-04)
- Azure Key Vault & Managed Identities: Secure credential and secret management

## Rationale
This hybrid architecture isolates expensive mainframe changes by abstracting migrated claim types behind an Azure API Gateway. It satisfies stringent security and performance constraints while mitigating the team's low cloud experience through managed Azure services.