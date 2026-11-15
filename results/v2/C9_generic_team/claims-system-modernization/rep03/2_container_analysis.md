## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old on-premises mainframe with a hybrid Azure cloud platform. It enables online claim submissions and modern adjuster workflows while maintaining transactional consistency and a 3-year coexistence strategy.

## Key Elements
- **Users**: Customers, Brokers, and Claims Adjusters
- **External Systems**: COBOL/DB2 On-Premises Mainframe (System of Record), Microsoft Entra ID (Azure AD)
- **Containers**: API Gateway, Azure App Service (Hosting the Azure Modular Monolith Platform and Anti-Corruption Layer), Azure SQL Database
- **Infrastructure Services**: Azure Service Bus, Azure Redis Cache, Azure Application Insights

## Relationships
- Customers and Brokers interact with the API Gateway via HTTPS for online claim submissions (R-01)
- Claims Adjusters interact with the Azure App Service via HTTPS for claims management (R-02)
- API Gateway authenticates users against Microsoft Entra ID using OpenID Connect/OAuth 2.0 (R-07)
- Azure App Service communicates asynchronously with the on-premises mainframe via Azure Service Bus and the Anti-Corruption Layer (ACL)
- Azure App Service reads/writes data to Azure SQL Database and caches read models in Azure Redis Cache (R-05)

## Technology Stack
- **Compute**: Azure App Service (PaaS) selected to minimize operational overhead given the team's low cloud experience
- **Database**: Azure SQL Database with strict per-module schema separation to support isolated claims migration and rollbacks (R-06)
- **Messaging & Caching**: Azure Service Bus for asynchronous decoupling and Azure Redis Cache for sub-2-second UI responses (R-05)
- **Observability**: Azure Application Insights for distributed tracing across hybrid boundaries

## Rationale
The hybrid architecture uses managed PaaS services on Azure to reduce operational risk for a team with low cloud experience while keeping the legacy mainframe as the system of record. Asynchronous messaging via Azure Service Bus, CQRS with Redis caching, and an Anti-Corruption Layer isolate legacy latency and constraints, ensuring high performance, zero data loss, and rapid one-day rollbacks.