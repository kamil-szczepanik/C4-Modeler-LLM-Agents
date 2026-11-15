## Overview
[The system modernizes a 30-year-old regional insurer mainframe by gradually migrating claim types to a hybrid cloud platform. The architecture uses Azure services alongside the legacy on-premise system to ensure uninterrupted claim processing.]

## Key Elements
- End Customers and Brokers
- Claims Adjusters and Claims Managers
- Legacy Mainframe
- Corporate Active Directory / Azure AD
- Analytics & Reporting System
- Customer/Broker Portal
- Adjuster Workstation
- Integration & Routing Engine
- Azure API Management Gateway
- Observability & Audit Logging
- Secret Management

## Relationships
- End Customers and Brokers -> Customer/Broker Portal [HTTPS]
- Claims Adjusters and Claims Managers -> Adjuster Workstation [HTTPS]
- Customer/Broker Portal -> Integration & Routing Engine [HTTPS / AMQP]
- Adjuster Workstation -> Integration & Routing Engine [HTTPS / AMQP]
- Integration & Routing Engine -> Azure API Management Gateway [HTTPS]
- Azure API Management Gateway -> Legacy Mainframe [Azure ExpressRoute, mTLS]
- New Claims Platform -> Analytics & Reporting System [Azure Event Hubs, TLS 1.3]

## Technology Stack
- Azure API Management: Gateway for rate-limiting, token validation, and mainframe protection
- Azure App Service & React/Angular: UI hosting for portals and workstations
- Azure Service Bus & Azure Functions: Asynchronous queuing, routing, and deduplication
- Azure Key Vault: Managed identities and automated rotation for secrets
- Azure Application Insights & Azure Cosmos DB: Distributed tracing and state tracking

## Rationale
[This hybrid architecture protects the fragile, expensive-to-change mainframe while enabling rapid cloud-native feature delivery. It guarantees zero data loss and meets strict performance constraints during the multi-year migration.]