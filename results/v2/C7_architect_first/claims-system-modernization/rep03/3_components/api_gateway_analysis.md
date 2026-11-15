## Overview
[The system is a hybrid cloud-and-on-premises Insurance Claims Modernization platform that gradually migrates claim types from a 30-year-old COBOL/DB2 mainframe to Azure while maintaining uninterrupted legacy processing. Its core purpose is to deliver modern online claim submission and adjuster workspaces while strictly shielding the legacy mainframe and ensuring zero loss or duplication of data during the 3-year migration.]

## Key Elements
- **Users**: Customers, Brokers, Claims Adjusters
- **External Systems**: Legacy Mainframe System (COBOL/DB2), Corporate Active Directory
- **Gateways & Security**: Azure API Management (APIM), Azure Web Application Firewall (WAF), Azure Key Vault, Azure Monitor & Application Insights
- **Containers**: Customer Portal (Azure App Service, React), Adjuster Workspace (Azure App Service, React, Node.js BFF), Integration / ACL Service (Azure Container Apps, .NET)
- **Data & Messaging**: Azure Database for PostgreSQL, Azure Service Bus
- **APIM Components**: Authentication & Token Validator, Routing & Path Dispatcher, Rate Limiting & Throttling, API Versioning & Transformation, Circuit Breaker

## Relationships
- Customer Portal / Adjuster Workspace -> Azure WAF: Sends incoming traffic [HTTPS]
- Azure WAF -> API Management: Inspects and forwards traffic [HTTPS]
- API Management -> Integration / ACL Service: Routes requests using mutual TLS [HTTPS, mTLS]
- Integration / ACL Service -> Legacy Mainframe System: Queries and synchronizes legacy data [SNA/MQ/TCP]
- API Management -> Azure Key Vault: Retrieves secrets and mTLS certificates [Internal/Managed Identity]
- API Management -> Azure Monitor: Exports telemetry and circuit breaker state [HTTPS]

## Technology Stack
- **Cloud Provider**: Azure (westeurope) & On-Premises Hybrid
- **Compute & Hosting**: Azure App Service (React frontends, Node.js BFF), Azure Container Apps (.NET Integration/ACL Service)
- **API & Integration**: Azure API Management (APIM), Azure Service Bus
- **Security**: Azure Active Directory (OIDC/JWT), Azure Key Vault, Azure WAF, mTLS
- **Database & Observability**: Azure Database for PostgreSQL, Application Insights, Azure Monitor
- **Infrastructure & Deployment**: Terraform/Bicep via Azure DevOps (GitOps) for rapid R-06 rollbacks despite low cloud experience

## Rationale
[This hybrid architecture decouples modern user experiences from fragile legacy infrastructure by placing Azure API Management and .NET Integration services as a protective anti-corruption layer. It guarantees business continuity, security, and sub-two-second adjuster response times while respecting strict mainframe batch windows and enabling risk-free, one-day claim-type rollbacks.]