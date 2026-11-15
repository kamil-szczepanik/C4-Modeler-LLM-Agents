## Overview
[The system modernizes a 30-year-old regional insurer mainframe claims platform by gradually migrating claim types to a hybrid cloud architecture. It enables online submissions and fast adjuster workflows while maintaining the legacy COBOL/DB2 system as the system of record.]

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Customer Portal (SPA React)
- Adjuster Workspace (SPA React)
- API Gateway (Azure API Management)
- Claims Core Container (.NET / Azure Container Apps)
- Read Model Projector (Azure Functions / .NET)
- Integration & ACL Container (Azure Functions)
- Adjuster Read Database (Azure Cosmos DB)
- Legacy Mainframe (COBOL/DB2 / CICS)
- Message Broker (IBM MQ)
- Identity Provider (Azure Active Directory)

## Relationships
- Customers & Brokers interact with Customer Portal via HTTPS/REST
- Claims Adjusters interact with Adjuster Workspace via HTTPS/REST
- Customer Portal & Adjuster Workspace authenticate via Azure Active Directory using OpenID Connect/OAuth 2.0
- API Gateway routes frontend traffic to Claims Core Container via HTTPS
- Claims Core Container reads/writes data and publishes events
- Read Model Projector updates Adjuster Read Database via internal messaging
- Integration & ACL Container communicates with Legacy Mainframe via IBM MQ with mTLS

## Technology Stack
- Azure App Service / Azure Container Apps: Runs frontend SPAs and backend .NET core services to offset team's low cloud experience
- Azure API Management: Secures and routes external traffic with OAuth 2.0 and RBAC
- Azure Cosmos DB / PostgreSQL: Provides low-latency CQRS read storage for sub-2s UI loads
- Azure Functions (.NET): Executes asynchronous event projections and ACL data translation
- IBM MQ: Manages asynchronous message exchange across the hybrid cloud-to-mainframe perimeter
- OpenTelemetry: Ensures centralized distributed tracing across hybrid Azure and on-premise boundaries

## Rationale
[This hybrid architecture isolates expensive mainframe changes behind an Anti-Corruption Layer while delivering sub-2-second adjuster response times via a CQRS pattern. It leverages managed Azure PaaS services to safely scale capabilities for a team with limited cloud experience.]