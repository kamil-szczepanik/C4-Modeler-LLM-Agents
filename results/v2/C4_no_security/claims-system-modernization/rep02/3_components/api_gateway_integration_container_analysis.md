## Overview
The system is a hybrid insurance claims platform that modernizes a 30-year-old mainframe by migrating claim types gradually to Azure. It processes customer submissions and adjuster workflows while maintaining strict consistency and legacy interoperability.

## Key Elements
- API Gateway / Integration Container (Azure API Management)
- Web Application Container (React / Node.js on Azure App Service)
- Claims Core Service Container (Java / Spring Boot on Azure Container Apps)
- Mainframe COBOL/DB2 System (On-premise system of record)
- Data & Caching Container (Azure Cosmos DB + Redis)
- Mainframe Adapter Container (Azure Service Bus with Dead Letter Queues)
- Configuration (Azure App Configuration)
- Identity Provider (Active Directory / Azure AD)

## Relationships
- Web Application Container -> API Gateway / Integration Container [HTTPS / REST]
- API Gateway / Integration Container -> Claims Core Service Container [HTTPS / REST]
- API Gateway / Integration Container -> Mainframe COBOL/DB2 System [TCP]
- API Gateway / Integration Container -> Data & Caching Container (Redis) [TCP / RESP]
- API Gateway / Integration Container -> Mainframe Adapter Container (Azure Service Bus) [AMQP / HTTPS]
- API Gateway / Integration Container -> Configuration (Azure App Configuration) [HTTPS]
- API Gateway / Integration Container -> Identity Provider (Azure AD) [HTTPS / OIDC/JWKS]

## Technology Stack
- Azure API Management: Acts as the intelligent API gateway enforcing routing, security, and resilience policies.
- Azure Service Bus: Handles asynchronous message offloading and dead-letter queues to prevent lost claims.
- Azure Cosmos DB + Redis: Provides high-performance caching to meet sub-2-second UI performance requirements.
- Azure App Configuration: Stores dynamic routing rules to support rapid one-day fallback to the mainframe.
- Terraform / Bicep: Enforces Infrastructure-as-Code for reliable hybrid deployments.

## Rationale
This hybrid architecture isolates the expensive, fragile mainframe behind an anti-corruption gateway while incrementally migrating functional workloads to Azure. It guarantees strict transactional consistency, high availability, and operational resilience despite the team's limited cloud experience.