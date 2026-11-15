## Overview
[The system is a hybrid insurance claims modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure-based cloud architecture. Its core purpose is to enable online claim submissions and adjuster workflows while maintaining zero data loss and strict performance standards.]

## Key Elements
- API Gateway Container (Azure API Management / Azure Container Apps)
- Customer BFF Container (Azure App Service / Container Apps)
- Adjuster BFF Container (Azure App Service / Container Apps)
- Modular Monolith Container (Azure App Service / Container Apps)
- Anti-Corruption Layer (ACL) Container (Azure Container Apps)
- Routing / Feature Flag Container (Container Apps)
- Asynchronous Messaging & Caching Layer (Azure Service Bus and Redis)
- COBOL/DB2 Mainframe (On-premises system of record)

## Relationships
- Customer BFF Container -> API Gateway Container: Communicates via internal APIs [Internal HTTPS/REST]
- Adjuster BFF Container -> API Gateway Container: Communicates via internal APIs [Internal HTTPS/REST]
- API Gateway Container -> Routing / Feature Flag Container: Evaluates rules [In-memory SDK with local Redis cache]
- API Gateway Container -> Anti-Corruption Layer (ACL) Container: Routes legacy traffic [HTTPS/REST]

## Technology Stack
- Azure API Management: Edge security, rate limiting, and declarative resilience policies
- Redis: Caching feature flags, idempotency keys, and edge response caching
- Azure Container Apps / App Service: Hosting modern microservices and BFFs
- RFC 7807 (Problem Details): Standardized error formatting
- OpenTelemetry / Azure Application Insights: Hybrid end-to-end tracing via correlation IDs

## Rationale
[The hybrid architecture utilizes an API Gateway with local caching and strict resilience policies to protect against mainframe latency and ensure sub-2-second adjuster screens. Centralized edge security, versioning, and an Anti-Corruption Layer enable iterative claim migration and rapid one-day rollbacks.]