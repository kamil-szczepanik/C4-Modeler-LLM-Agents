## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern Azure-based platform while ensuring zero data loss. The hybrid architecture maintains uninterrupted operations, supporting customers, brokers, and claims adjusters through incremental claim-type migrations.

## Key Elements
- Claims Web Application (Azure Static Web Apps / React)
- API Gateway & BFF (Azure Container Apps / .NET 8), containing YARP API Router, Claims BFF Service, and Routing Dispatcher Component
- Integration & Anti-Corruption Layer (Azure Functions & Service Bus)
- New Claims Database (Azure SQL Database)
- Legacy Mainframe (COBOL/DB2)
- Azure Active Directory, Azure App Configuration, Azure Key Vault, and Azure Application Insights

## Relationships
- Claims Web Application -> API Router: Requests data via HTTPS/JSON [HTTPS/JSON]
- API Router -> Claims BFF Service: Routes verified requests [In-process / gRPC]
- Claims BFF Service -> Routing Dispatcher: Orchestrates routing [In-process]
- Routing Dispatcher -> New Claims Database / Integration & ACL: Fetches claim data [mTLS and HTTPS/JSON]
- Integration & ACL -> Legacy Mainframe: Synchronizes batch data [COBOL/DB2 batch protocols]
- API Gateway & BFF -> Active Directory: Authenticates users [OpenID Connect/OAuth2]
- API Gateway & BFF -> Azure Key Vault: Retrieves secrets [Managed Identities]
- API Gateway & BFF -> Azure Application Insights: Forwards telemetry [OpenTelemetry headers]

## Technology Stack
- Azure Container Apps: Hosts containerized microservices with KEDA scaling based on HTTP concurrency.
- .NET 8: Provides high-throughput runtime performance for the BFF under strict latency constraints.
- YARP (Yet Another Reverse Proxy): Manages cross-cutting routing, rate limiting, and JWT validation.
- Azure App Configuration: Dynamically controls feature flags for claim-type migrations and rollbacks.
- Polly: Implements circuit breakers and fallback handlers to manage legacy mainframe latency spikes.
- Azure SQL Database: Serves as the persistence layer for migrated claim types.

## Rationale
This hybrid architecture isolates the expensive legacy mainframe behind an Anti-Corruption Layer while empowering a modern, scalable Azure platform to deliver sub-2-second response times. Dynamic feature flagging and YARP routing enable seamless 1-day rollbacks of migrated claim types without risking data consistency or violating the strict 3-year migration constraint.