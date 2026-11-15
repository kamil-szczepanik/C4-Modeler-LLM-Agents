## Overview
The system modernizes a regional insurer's 30-year-old legacy mainframe claims system by gradually migrating claim types to a hybrid Azure cloud platform. It ensures continuous processing, strict data consistency, and rapid one-day fallback capabilities without disrupting nightly batch windows.

## Key Elements
- End Customers and Brokers
- Claims Adjusters and Claims Managers
- Legacy Mainframe
- Corporate Active Directory / Azure AD
- Analytics & Reporting System
- Customer/Broker Portal
- Adjuster Workstation
- Integration & Routing Engine
- Observability & Audit Logging
- Azure API Management Gateway

## Relationships
- End Customers and Brokers -> Customer/Broker Portal (HTTPS)
- Claims Adjusters and Claims Managers -> Adjuster Workstation (HTTPS)
- Customer/Broker Portal & Adjuster Workstation -> Integration & Routing Engine (HTTPS / AMQP)
- Integration & Routing Engine -> Azure API Management Gateway (HTTPS)
- Azure API Management Gateway -> Legacy Mainframe (Azure ExpressRoute, mTLS)
- Integration & Routing Engine -> Analytics & Reporting System (Azure Event Hubs, TLS 1.3)
- End Customers and Brokers & Claims Adjusters -> Corporate Active Directory / Azure AD (OAuth 2.0 / OIDC)
- All Containers -> Observability & Audit Logging (HTTPS)

## Technology Stack
- Customer/Broker Portal: Azure App Service, React (Public SPA and BFF)
- Adjuster Workstation: Azure App Service, Angular (Internal UI optimized for sub-2s loads)
- Integration & Routing Engine: Azure Service Bus, Azure Functions (Asynchronous queuing, DLQ, and deduplication)
- Observability & Audit Logging: Azure Application Insights, Azure Cosmos DB (Distributed tracing and state tracking)
- Azure API Management Gateway: Azure API Management (Rate-limiting, token validation, and mainframe protection)
- Secret Management: Azure Key Vault (Managed identities and automated rotation)

## Rationale
This hybrid architecture isolates user interfaces and encapsulates migration routing logic within the integration layer to meet strict performance targets and guarantee a one-day mainframe fallback. Asynchronous queuing and centralized observability protect fragile on-premise components while preventing lost or duplicated claims during the incremental transition.