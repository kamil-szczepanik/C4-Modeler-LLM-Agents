## Overview
The system is an Insurance Claims Modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern hybrid cloud solution. Its core purpose is to ensure zero data loss and enable seamless incremental migration of claim types while maintaining continuous business operations.

## Key Elements
- **Users**: Customers & Brokers, Claims Adjusters
- **External Systems**: Legacy Mainframe System, Core Integration Hub, Insurer's Active Directory, Payment Gateway & Notification System
- **Frontend & API Tier**: Web Frontend (React, Azure App Service), BFF / API Gateway (Azure API Management, Node.js, Java Spring Boot)
- **Backend Services**: Claims Processing Service (Java Spring Boot, JPA, Azure Container Apps)
- **Messaging & Integration**: Integration & ACL (Azure Service Bus, Custom Routing & Circuit-Breaker Worker)
- **Data & Caching**: Azure Redis Cache, Azure SQL Database (Claims Core Schema, Audit & Reconciliation Log Store, Row-Level Security Engine, Temporal Tables, CDC)

## Relationships
- Customers & Brokers / Claims Adjusters -> Web Frontend [HTTPS / TLS 1.3]
- Web Frontend -> BFF / API Gateway [HTTPS / REST]
- BFF / API Gateway -> Claims Processing Service [gRPC / HTTPS]
- Claims Processing Service -> Azure SQL Database [JDBC / TLS 1.3, Azure Private Link]
- Claims Processing Service -> Integration & ACL (Azure Service Bus) [AMQP]
- Integration & ACL -> Legacy Mainframe System [SNA / Batch Files / Custom Protocol]
- Web Frontend / Services -> Insurer's Active Directory [OIDC / OAuth2 / Azure AD Managed Identity]

## Technology Stack
- **Compute**: Azure Container Apps, Azure App Service (Java Spring Boot, Node.js, React)
- **Database**: Azure SQL Database (Hyperscale/Serverless, Temporal Tables, CDC, TDE with CMK, Always Encrypted, Dynamic Data Masking)
- **Messaging**: Azure Service Bus (AMQP)
- **Caching**: Azure Redis Cache
- **Security & Identity**: Azure Active Directory, Azure Key Vault, Microsoft Defender for SQL
- **Infrastructure & Monitoring**: Terraform/Bicep, Azure Monitor, Log Analytics Workspace

## Rationale
This hybrid architecture isolates expensive mainframe changes behind an integration layer while leveraging Azure SQL Database to guarantee consistency and sub-2-second adjuster response times. The chosen technology stack ensures strict security compliance, incremental claim migration, and rapid fallback capabilities during the 3-year coexistence period.