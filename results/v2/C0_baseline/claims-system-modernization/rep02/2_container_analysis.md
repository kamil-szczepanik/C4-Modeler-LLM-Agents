## Overview
[The Insurance Claims Modernization Platform gradually replaces an on-premise mainframe claims system with a hybrid cloud architecture in Azure West Europe. Its core purpose is to enable incremental claim migration while ensuring zero data loss and uninterrupted operations.]

## Key Elements
- Customers / Brokers
- Claims Adjusters
- Migration Product Managers
- Customer Support Agents
- Legacy Mainframe (COBOL/DB2)
- Microsoft Entra ID
- Azure API Management
- Customer Portal (React / Azure Static Web Apps)
- Adjuster Workspace (Angular / Azure App Service)
- Claims Core Engine (Java / Spring Boot / Azure Container Apps)
- Routing & Integration Service (Azure Functions)
- Business Analytics & Reporting (Azure SQL / Power BI)
- Azure SQL Database
- Azure Service Bus Topics

## Relationships
- Customers/Brokers interact with Customer Portal via HTTPS/TLS
- Claims Adjusters & Support Agents interact with Adjuster Workspace via HTTPS/TLS
- API Gateway routes traffic and validates OIDC tokens from Microsoft Entra ID
- Adjuster Workspace queries Azure SQL Database via ADO.NET/TLS for sub-2s reads
- Claims Core Engine publishes claim events to Azure Service Bus Topics using AMQP over TLS
- Routing & Integration Service evaluates claim types via Azure Functions
- Azure environment connects to Legacy Mainframe via Azure ExpressRoute with IPsec VPN

## Technology Stack
- Azure API Management: API Gateway and OIDC validation for secure tenant entry
- React & Angular: Frontend frameworks for portal and adjuster UI development
- Azure App Service & Azure Container Apps: Hosting for web apps and Java/Spring Boot microservices
- Azure SQL Database: CQRS read-model storage ensuring sub-2 second adjuster screen loads
- Azure Service Bus Topics: Reliable asynchronous messaging with session IDs for data consistency and rollback management
- Azure ExpressRoute & Managed Identities: Secure hybrid connectivity and credential-less authentication via Azure Key Vault

## Rationale
[The hybrid architecture isolates the expensive, slow legacy mainframe behind secure Azure ExpressRoute connections while leveraging Azure managed services to offset the team's low cloud experience. CQRS patterns, Azure SQL read-models, and Service Bus queues successfully meet strict performance, consistency, and one-day rollback requirements.]