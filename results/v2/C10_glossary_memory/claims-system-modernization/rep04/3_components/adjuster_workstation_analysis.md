## Overview
[The system is a modern hybrid claims processing platform designed to gradually replace a 30-year-old mainframe while ensuring continuous operations. Its core purpose is to enable seamless online claim submissions and sub-second adjuster workflows while maintaining strict data consistency.]

## Key Elements
- End Customers and Brokers
- Claims Adjusters and Claims Managers
- Legacy Mainframe
- Corporate Active Directory / Azure AD
- Analytics & Reporting System
- New Claims Platform
- Azure API Management (APM) Gateway
- Customer/Broker Portal
- Adjuster Workstation
- Integration & Routing Engine
- Observability & Audit Logging
- Secret Management

## Relationships
- End Customers and Brokers -> Customer/Broker Portal: [HTTPS]
- Claims Adjusters and Claims Managers -> Adjuster Workstation: [HTTPS]
- Customer/Broker Portal -> Integration & Routing Engine: [HTTPS / AMQP]
- Adjuster Workstation -> Integration & Routing Engine: [HTTPS / AMQP]
- Integration & Routing Engine -> Azure API Management Gateway: [HTTPS]
- Azure API Management Gateway -> Legacy Mainframe: [Azure ExpressRoute, mTLS]
- New Claims Platform -> Analytics & Reporting System: [Azure Event Hubs, TLS 1.3]
- End Customers and Brokers -> Corporate Active Directory / Azure AD: [OAuth 2.0 / OIDC]

## Technology Stack
- Azure App Service & React: Used for Customer/Broker Portal SPA hosting.
- Azure App Service & Angular: Used for Adjuster Workstation UI to achieve sub-2s performance.
- Azure Service Bus & Azure Functions: Powers the Integration & Routing Engine for asynchronous messaging.
- Azure API Management: Secures and protects legacy mainframe interfaces.
- Azure SQL Database: Provides local read-model caching for sub-2s UI responses.
- Azure Application Insights & Azure Cosmos DB: Handles distributed tracing and audit logging.
- Azure Key Vault: Manages secrets, TLS certificates, and managed identity authentication.

## Rationale
[This hybrid architecture decouples the modern Azure-based UI and routing layer from fragile legacy systems to meet strict performance and maintainability SLAs. It ensures zero claim loss and rapid rollback capabilities despite the team's limited cloud experience.]