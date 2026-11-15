## Overview
[The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a hybrid cloud platform on Azure West Europe, ensuring uninterrupted claims processing for customers, brokers, and adjusters.]

## Key Elements
- Customers [person, context]
- Brokers [person, context]
- Claims Adjuster [person, context]
- New Insurance Claims Platform [system, context] (Azure Cloud)
- Customer Portal SPA [container] (Azure Static Web Apps, React/TypeScript)
- API Gateway [container] (Azure API Management)
- Claims Processing Core & BFF [container] (Azure Kubernetes Service)
- Routing & Reconciliation Service [container] (Azure Kubernetes Service + Azure Cosmos DB)
- Legacy Mainframe [externalSystem, context] (COBOL/DB2, On-Premise)
- Identity Provider [externalSystem, context] (Corporate Active Directory / Azure AD)
- Notification Service [externalSystem, context] (SendGrid/Twilio)

## Relationships
- Customers -> Customer Portal SPA (HTTPS/WSS)
- Brokers -> Customer Portal SPA (HTTPS/WSS)
- Claims Adjuster -> Customer Portal SPA (HTTPS/WSS)
- Customer Portal SPA -> API Gateway (HTTPS REST/GraphQL)
- API Gateway -> Claims Processing Core & BFF (HTTPS / mTLS)
- Claims Processing Core & BFF -> Routing & Reconciliation Service (Internal gRPC/REST)
- Routing & Reconciliation Service -> Legacy Mainframe (Azure Service Bus over Azure ExpressRoute/VPN)
- New Insurance Claims Platform -> Identity Provider (OpenID Connect / OAuth 2.0)
- New Insurance Claims Platform -> Notification Service (HTTPS REST API)

## Technology Stack
- Azure Kubernetes Service (AKS): Standardizes backend compute for Claims Processing Core, BFF, and Routing Service to minimize operational overhead for a cloud-inexperienced team.
- Azure API Management (APIM): Enforces rate limiting, OAuth 2.0 token validation, and circuit breaking toward the mainframe.
- Azure Static Web Apps: Hosts the React/TypeScript Customer Portal SPA.
- Azure Cosmos DB: Tracks claims state and reconciliation data for zero-loss guarantees (R-04) and rapid 1-day fallbacks (R-06).
- Azure ExpressRoute / IPSec VPN: Secures hybrid transport between Azure West Europe and the on-premise mainframe.

## Rationale
[This hybrid architecture isolates complex claim-type logic within modular AKS services controlled by feature flags, enabling a seamless 1-day fallback to the legacy mainframe without violating strict batch windows or incurring excessive integration costs. Standardizing backend compute on AKS reduces operational complexity for a cloud-beginner team while leveraging managed Azure security and routing services to meet stringent performance and consistency requirements.]