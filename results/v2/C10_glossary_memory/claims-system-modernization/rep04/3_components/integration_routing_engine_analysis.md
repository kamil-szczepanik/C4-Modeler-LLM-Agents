## Overview
- This system gradually modernizes a 30-year-old mainframe claims system by introducing a hybrid cloud platform while the legacy system processes active claims.
- The core purpose is to migrate claim types incrementally with zero data loss, low adjuster latency, and a reliable mainframe fallback mechanism.

## Key Elements
- End Customers and Brokers [person]
- Claims Adjusters and Claims Managers [person]
- Legacy Mainframe [externalSystem]
- Corporate Active Directory / Azure AD [externalSystem]
- Analytics & Reporting System [externalSystem]
- Customer/Broker Portal [container] (Azure App Service, React)
- Adjuster Workstation [container] (Azure App Service, Angular)
- Integration & Routing Engine [container] (Azure Service Bus, Azure Functions)
- Claim Router Component [component] (.NET Isolated Azure Functions)
- Deduplication & State Component [component] (Azure Cosmos DB)
- Fallback Switch Component [component] (Azure App Configuration)
- Retry & DLQ Handler Component [component] (.NET Azure Functions)
- Azure API Management Gateway [container] (Azure API Management)
- Observability & Audit Logging [container] (Azure Application Insights, Azure Cosmos DB)
- Secret Management [container] (Azure Key Vault)

## Relationships
- End Customers and Brokers -> Customer/Broker Portal: Submit claims [HTTPS]
- Claims Adjusters and Claims Managers -> Adjuster Workstation: Manage claims [HTTPS]
- Customer/Broker Portal -> Integration & Routing Engine: Route claim submissions [HTTPS / AMQP]
- Adjuster Workstation -> Integration & Routing Engine: Route adjuster actions [HTTPS / AMQP]
- Integration & Routing Engine -> Azure API Management Gateway: Forward traffic [HTTPS]
- Azure API Management Gateway -> Legacy Mainframe: Access legacy records [Azure ExpressRoute, mTLS]
- Integration & Routing Engine -> Analytics & Reporting System: Stream event data [Azure Event Hubs, TLS 1.3]
- All Containers -> Observability & Audit Logging: Send telemetry [HTTPS]

## Technology Stack
- Azure App Service: Hosts user portals with managed infrastructure scaling.
- Azure Functions (Premium Plan): Provides serverless execution with pre-warmed instances to mitigate cold starts.
- Azure Service Bus: Manages asynchronous queuing, AMQP delivery, and Dead-Letter Queues.
- Azure Cosmos DB: Enforces idempotency and tracks state for deduplication.
- Azure App Configuration: Dynamically manages routing rules for the 1-day mainframe fallback.
- Azure API Management: Protects fragile mainframe interfaces with rate-limiting and validation.

## Rationale
- This hybrid architecture isolates expensive mainframe dependencies while delivering a modern, responsive user experience.
- Managed Azure services reduce operational overhead for a team with limited cloud experience while guaranteeing strict compliance with consistency and security requirements.