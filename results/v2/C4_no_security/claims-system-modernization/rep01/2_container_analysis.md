## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old on-premises COBOL/DB2 mainframe with a modern Azure-hosted platform while ensuring uninterrupted legacy batch processing. It uses a hybrid architecture with an Anti-Corruption Layer (ACL) and isolated domain services to migrate claim types incrementally over three years.

## Key Elements
* **Users:** Policyholders, Brokers, and Claims Adjusters
* **External Systems:** Legacy COBOL/DB2 Mainframe, Microsoft Entra ID
* **Containers:** Azure API Management (API Gateway), Customer/Broker Portal, Adjuster Workstation, Adjuster BFF, Claim Migration Manager / Admin Portal, Core Claims Domain, Integration Worker, Operational Data Store (PostgreSQL), Observability Service

## Relationships
* **Users to API Gateway:** HTTPS / OIDC / OAuth2 for single sign-on and secure entry
* **API Gateway to BFFs/Portals:** HTTPS / gRPC for routing traffic to frontend containers
* **BFFs/Portals to Core Services:** HTTPS / gRPC for internal domain communication
* **Integration Worker to Mainframe:** ACL Gateway and Azure Service Bus for asynchronous event processing and data synchronization
* **Core Claims & BFFs to PostgreSQL:** TLS for operational data persistence and caching

## Technology Stack
* **Cloud Platform:** Azure (West Europe region) paired with on-premises infrastructure
* **Frontend/BFF:** Node.js/TypeScript and Azure App Service for sub-2s adjuster performance
* **Backend Domain & Integration:** .NET / C# and Azure Service Bus for reliable event-driven messaging
* **Database:** Azure Database for PostgreSQL as the operational data store
* **Security & Ingress:** Microsoft Entra ID and Azure API Management (APIM)
* **Operations:** Docker, Bicep/Terraform for IaC, and Azure Application Insights / Prometheus / Grafana for observability

## Rationale
This hybrid architecture isolates low-experience cloud developers from mainframe complexities by using asynchronous messaging and a dedicated BFF to meet strict performance and zero-data-loss constraints. Centralized API management, Infrastructure as Code, and modular domain containers ensure the system can safely execute incremental claim migrations and one-day rollbacks.