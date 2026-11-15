## Overview
[The system is an Insurance Claims Modernization Platform that gradually replaces a 30-year-old mainframe claims system with a modern hybrid cloud architecture. Its core purpose is to enable online claim submission and adjuster workflows while migrating claim types incrementally without downtime or data loss.]

## Key Elements
- End Customers & Brokers
- Claims Adjusters
- Migration Operations Lead
- Legacy Mainframe System
- Corporate Active Directory
- Third-Party Payment Gateway
- Customer Portal (React / TypeScript SPA, Azure Static Web Apps)
- Adjuster Web Application (React / TypeScript SPA)
- Claims API Gateway / BFF (.NET 8 / YARP, Azure Container Apps)
- Integration & Sync Service (Azure Container Apps worker, Azure Service Bus)
- Audit & Event Store (Azure Cosmos DB)
- Operational Datastore (Azure SQL Database / PostgreSQL on Azure)

## Relationships
- Customer Portal -> Claims API Gateway / BFF: Communicates via [HTTPS/JSON]
- Adjuster Web Application -> Claims API Gateway / BFF: Communicates via [HTTPS/JSON]
- Claims API Gateway / BFF -> Integration & Sync Service: Communicates via [HTTPS/JSON and Azure Service Bus]
- Corporate Active Directory -> Claims API Gateway / BFF: Authenticates users via [OpenID Connect (OIDC) / OAuth2]
- Claims API Gateway / BFF -> Legacy Mainframe System: Communicates via [gRPC / HTTPS]

## Technology Stack
- .NET 8 (C#): Chosen for robust enterprise patterns and strong typing to support a team with low cloud experience.
- YARP (Yet Another Reverse Proxy): Selected for dynamic claim-type routing and rate-limiting policies.
- Azure Container Apps: Used for containerized microservices deployment with a minimum replica count of 1.
- Polly: Integrated for circuit breaking, timeouts, and fallback resilience patterns.
- Azure Key Vault: Utilized with managed identities for secure runtime secret management.
- OpenTelemetry: Implemented for distributed tracing and observability.

## Rationale
[This architecture successfully bridges a fragile legacy mainframe with a modern cloud frontend through a resilient, secure .NET-based BFF. It guarantees high performance, strict data consistency, and rapid one-day rollback capabilities required for a safe, incremental migration.]