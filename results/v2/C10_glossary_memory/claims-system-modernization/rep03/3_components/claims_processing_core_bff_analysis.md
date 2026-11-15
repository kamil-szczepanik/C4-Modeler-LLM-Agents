## Overview
[The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure-based cloud platform. It enables online claim submissions and adjuster web workflows while maintaining zero-loss consistency and uninterrupted legacy operations.]

## Key Elements
- Customers [person, context]
- Brokers [person, context]
- Claims Adjusters [person, context]
- Legacy Mainframe [externalSystem, context] (COBOL/DB2)
- Identity Provider [externalSystem, context] (Active Directory / Azure AD)
- Notification Service [externalSystem, context] (SendGrid/Twilio)
- Customer Portal SPA [container] (Azure Static Web Apps, React/TypeScript)
- API Gateway [container] (Azure API Management)
- Claims Processing Core & BFF [container] (Azure Kubernetes Service)
- Routing & Reconciliation Service [container] (Azure Kubernetes Service + Azure Cosmos DB)

## Relationships
- Customers -> Customer Portal SPA [HTTPS/WSS]
- Brokers -> Customer Portal SPA [HTTPS/WSS]
- Claims Adjusters -> Customer Portal SPA [HTTPS/WSS]
- Customer Portal SPA -> API Gateway [HTTPS REST/GraphQL]
- API Gateway -> Claims Processing Core & BFF [HTTPS / mTLS]
- Claims Processing Core & BFF -> Routing & Reconciliation Service [Internal gRPC over TLS 1.3]
- Routing & Reconciliation Service -> Legacy Mainframe [Azure Service Bus over Azure ExpressRoute/VPN]
- New Insurance Claims Platform -> Identity Provider [OpenID Connect / OAuth 2.0]
- Claims Processing Core & BFF -> Notification Service [HTTPS REST API]

## Technology Stack
- Azure Static Web Apps: Hosts the React/TypeScript Customer Portal SPA for frontend delivery.
- Azure API Management: Acts as the API Gateway enforcing OAuth 2.0 validation and circuit breaking.
- Azure Kubernetes Service (AKS): Hosts backend containers (.NET 8) with strict Network Policies and HPA.
- Azure Cosmos DB: Provides managed persistence for the Routing & Reconciliation Service and transactional outbox patterns.
- Azure Service Bus: Manages asynchronous messaging across the hybrid boundary to the Legacy Mainframe.

## Rationale
[This hybrid architecture isolates expensive mainframe changes while using Azure-native managed services to bridge skill gaps. It satisfies strict performance and consistency constraints through BFF payload optimization and transactional outbox patterns.]