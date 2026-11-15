## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure-based platform. It enables online claim submissions and adjuster workflows while maintaining legacy operations.

## Key Elements
- End Customers and Brokers [person, context]
- Claims Adjusters and Claims Managers [person, context]
- Customer/Broker Portal [container, container] (Azure App Service, React)
- Adjuster Workstation [container, container] (Azure App Service, Angular)
- Integration & Routing Engine [container, container] (Azure Service Bus, Azure Functions)
- Azure API Management Gateway [container, container] (Azure API Management)
- Observability & Audit Logging [container, container] (Azure Application Insights, Azure Cosmos DB)
- Secret Management [container, container] (Azure Key Vault)
- Legacy Mainframe [externalSystem, context]
- Corporate Active Directory / Azure AD [externalSystem, context]

## Relationships
- Customer/Broker Portal -> Integration & Routing Engine [HTTPS / AMQP, TLS 1.3]
- Adjuster Workstation -> Integration & Routing Engine [HTTPS / AMQP, TLS 1.3]
- Integration & Routing Engine -> Azure API Management Gateway [HTTPS]
- Azure API Management Gateway -> Legacy Mainframe [Azure ExpressRoute, mTLS]
- End Customers and Brokers -> Corporate Active Directory / Azure AD [OAuth 2.0 / OIDC]

## Technology Stack
- Azure App Service: Hosts public portals and internal workstations for managed hosting.
- React / Angular: Frontend frameworks for UI rendering and state management.
- ASP.NET Core: Powers BFF APIs for native Azure integration and security controls.
- Azure Service Bus: Handles asynchronous messaging, deduplication, and dead-letter queues.
- Azure API Management: Protects legacy mainframe endpoints with rate-limiting and token validation.

## Rationale
This hybrid architecture isolates the fragile legacy mainframe behind secure Azure integration layers while enabling gradual, low-risk claim type migration. Standardizing on managed Azure services reduces operational overhead for a team with limited cloud experience.