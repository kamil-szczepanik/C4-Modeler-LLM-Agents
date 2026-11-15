## Overview
[This system modernizes a 30-year-old regional insurance mainframe claims platform through a gradual, claim-type-by-claim-type migration to a hybrid cloud architecture. It ensures seamless business continuity while maintaining strict data consistency, security, and sub-minute operational rollbacks.]

## Key Elements
- Users: Customers & Brokers, Claims Adjusters
- External Systems: Legacy Mainframe System, Azure Active Directory / Entra ID, Azure API Gateway with Rate Limiter
- Containers: Customer Portal & Adjuster Web Apps (Azure Static Web Apps), Claim Management API, Claim Router / Anti-Corruption Layer, Audit & Reconciliation Service (Azure Container Apps, .NET 8)
- Supporting Services: Azure Service Bus, Azure App Configuration, Azure SQL Database, Azure Key Vault

## Relationships
- Customers/Brokers interact with Customer Portal via HTTPS (TLS 1.3)
- Claims Adjusters interact with Adjuster Web Apps via HTTPS (TLS 1.3)
- Web Apps communicate with Claim Management API and Claim Router via HTTPS/REST
- Claim Router interacts with Legacy Mainframe System via SNA/MQ and Azure Service Bus via AMQP
- Services authenticate using Azure Active Directory / Entra ID via OAuth2/OIDC

## Technology Stack
- Hosting: Azure Container Apps & Azure Static Web Apps for modern serverless container execution
- Backend Runtime: .NET 8 for high-performance microservices
- Messaging: Azure Service Bus for asynchronous event processing
- Configuration & Secrets: Azure App Configuration and Azure Key Vault for centralized metadata and secure secret management
- Database: Azure SQL Database for relational state management

## Rationale
[The hybrid Azure cloud architecture isolates complex legacy mainframe dependencies while providing scalable .NET 8 containerized services to meet strict performance and security mandates. Centralized feature toggles via Azure App Configuration guarantee the rapid one-day rollback capability required for incremental claim-type migrations.]