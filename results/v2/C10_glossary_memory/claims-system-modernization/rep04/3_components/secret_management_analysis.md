## Overview
The system modernizes a regional insurer's 30-year-old mainframe claims system via a hybrid architecture. It securely routes claims, manages authentication, and gradually migrates claim types.

## Key Elements
- End Customers and Brokers
- Claims Adjusters and Claims Managers
- Legacy Mainframe
- Corporate Active Directory / Azure AD
- Analytics & Reporting System
- New Claims Platform
- Azure API Management Gateway
- Customer/Broker Portal
- Adjuster Workstation
- Integration & Routing Engine
- Observability & Audit Logging
- Secret Management (Azure Key Vault)

## Relationships
- End Customers and Brokers -> Customer/Broker Portal (HTTPS)
- Claims Adjusters and Claims Managers -> Adjuster Workstation (HTTPS)
- Customer/Broker Portal -> Integration & Routing Engine (HTTPS / AMQP)
- Adjuster Workstation -> Integration & Routing Engine (HTTPS / AMQP)
- Integration & Routing Engine -> Azure API Management Gateway (HTTPS)
- Azure API Management Gateway -> Legacy Mainframe (Azure ExpressRoute, mTLS)
- Integration & Routing Engine -> Analytics & Reporting System (Azure Event Hubs, TLS 1.3)
- Consuming containers -> Secret Management (HTTPS / Azure SDK)

## Technology Stack
- Azure App Service & React/Angular: Hosts portal and workstation containers for fast, modern UI delivery.
- Azure Service Bus & Azure Functions: Powers asynchronous queuing and routing to protect fragile mainframe interfaces.
- Azure API Management: Provides rate-limiting, token validation, and mTLS protection for mainframe integration.
- Azure Key Vault & Managed Identities: Eliminates hardcoded credentials and secures sensitive keys and certificates.

## Rationale
The hybrid architecture protects fragile legacy systems while gradually migrating workloads to the cloud. Managed identities and robust API gateways ensure enterprise-grade security and maintainability without disrupting the strict batch window.