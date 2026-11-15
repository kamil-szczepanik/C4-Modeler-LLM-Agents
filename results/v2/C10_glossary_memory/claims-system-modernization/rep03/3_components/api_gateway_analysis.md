## Overview
The system modernizes a 30-year-old regional insurance claims platform by gradually migrating claim types to a hybrid cloud architecture. It replaces legacy components while maintaining uninterrupted processing via an on-premise mainframe system of record.

## Key Elements
- Customers, Brokers, Claims Adjusters
- New Insurance Claims Platform
- Legacy Mainframe (COBOL/DB2)
- Identity Provider (Active Directory / Azure AD)
- Notification Service (SendGrid/Twilio)
- Customer Portal SPA (Azure Static Web Apps, React/TypeScript)
- API Gateway (Azure API Management)
- Claims Processing Core & BFF (Azure Kubernetes Service)
- Routing & Reconciliation Service (Azure Kubernetes Service + Azure Cosmos DB)

## Relationships
- Customers, Brokers, Claims Adjusters -> New Insurance Claims Platform [HTTPS/WSS]
- New Insurance Claims Platform -> Identity Provider [OpenID Connect / OAuth 2.0]
- New Insurance Claims Platform -> Legacy Mainframe [Azure Service Bus over Azure ExpressRoute/VPN]
- New Insurance Claims Platform -> Notification Service [HTTPS REST API]
- Customer Portal SPA -> API Gateway [HTTPS REST/GraphQL]
- API Gateway -> Claims Processing Core & BFF [HTTPS / mTLS]
- Claims Processing Core & BFF -> Routing & Reconciliation Service [Internal gRPC/REST]
- Routing & Reconciliation Service -> Legacy Mainframe [Azure Service Bus over Azure ExpressRoute/VPN]

## Technology Stack
- Azure West Europe: Primary cloud region for scalability and managed services.
- Azure Kubernetes Service (AKS): Hosts backend microservices, optimizing operational efficiency for teams with limited cloud experience.
- Azure API Management (APIM): Enforces rate limiting, JWT validation via JWKS, WAF, and RFC 7807 error mapping.
- Azure Cosmos DB: Manages high-performance claims state and reconciliation data for zero-loss guarantees.
- Azure Static Web Apps: Hosts the React/TypeScript Customer Portal SPA.
- Azure Key Vault: Centralized secret management utilizing managed identities.

## Rationale
This hybrid architecture decouples modern web clients from the legacy mainframe, ensuring sub-second adjuster screens and secure single sign-on without overloading fragile on-premise batch windows. Claim types can migrate incrementally while maintaining zero-loss consistency and rapid one-day fallback capabilities.