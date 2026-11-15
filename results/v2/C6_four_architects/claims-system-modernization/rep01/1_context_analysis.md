## Overview
[The system modernizes a 30-year-old regional insurance mainframe by gradually migrating claim types to a hybrid cloud platform. It processes online claims and adjuster workflows while keeping the legacy COBOL/DB2 system as the system of record.]

## Key Elements
- [Customer & Broker Portal (Web/Mobile)]
- [Modern Claims Platform: API Management, Claims Web App, Claim Routing Service, Claims Processing Service]
- [Data Storage: Azure SQL Database]
- [Integration Gateway: Azure Service Bus, On-Premises Integration Service]
- [External Systems: Legacy Mainframe (COBOL/DB2, IBM MQ), Active Directory / Entra ID Connect]

## Relationships
- [Customer & Broker Portal -> Modern Claims Platform: HTTPS/REST]
- [Adjusters -> Modern Claims Platform: HTTPS/WebSockets]
- [Modern Claims Platform -> Active Directory: HTTPS (OIDC/SAML)]
- [Claim Routing Service -> Azure SQL Database: TDS via Entity Framework Core]
- [Modern Claims Platform -> Azure Service Bus -> On-Premises Integration Service: AMQP]
- [On-Premises Integration Service -> Legacy Mainframe: IBM MQ protocol]

## Technology Stack
- [Azure App Service & Azure Container Apps: Simplifies cloud operations for a team with limited cloud experience]
- [Azure SQL Database: Provides cloud data persistence with rollback capability for migrated claim types]
- [Azure Service Bus & IBM MQ: Enables asynchronous, decoupled hybrid messaging respecting batch windows]
- [Azure API Management & Key Vault: Secures ingress and manages secrets via Managed Identity]

## Rationale
[The hybrid architecture safely isolates fragile mainframe touchpoints while leveraging managed cloud services to reduce operational complexity. Asynchronous messaging and dynamic routing guarantee zero data loss and enable rapid fallback to the legacy system within one day.]