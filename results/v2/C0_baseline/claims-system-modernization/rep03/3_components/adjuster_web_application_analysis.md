## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a hybrid Azure-hosted cloud platform. It ensures seamless claim processing and data consistency while minimizing legacy operational disruption.

## Key Elements
- End Customers & Brokers
- Claims Adjusters
- Migration Operations Lead
- Legacy Mainframe System
- Corporate Active Directory
- Third-Party Payment Gateway
- Customer Portal (React SPA, Azure Static Web Apps)
- Adjuster Web Application (React SPA, Azure Static Web Apps)
- Claims API Gateway / BFF (Node.js/.NET Core, Azure Container Apps)
- Integration & Sync Service (Azure Container Apps worker, Azure Service Bus)
- Audit & Event Store (Azure Cosmos DB)
- Operational Datastore (Azure SQL Database / PostgreSQL)
- Claim Workspace Shell, Triage & Queue Manager, Dynamic Form Engine, BFF Client Adapter (Adjuster Web Application components)

## Relationships
- End Customers & Brokers -> Customer Portal: Accesses via [HTTPS (REST)]
- Claims Adjusters -> Adjuster Web Application: Interacts via [HTTPS (REST)]
- Adjuster Web Application -> Claims API Gateway / BFF: Communicates via [HTTPS/JSON, TLS 1.3]
- Claims API Gateway / BFF -> Operational Datastore & Audit Store: Queries via [TCP/IP, Connection Pooling]
- Integration & Sync Service -> Legacy Mainframe System: Synchronizes via [MQ / Batch Protocols]

## Technology Stack
- Azure Static Web Apps: Hosts React SPAs for fast global content delivery and simple static deployments.
- React & TypeScript: Powers dynamic UI components with client-side caching (React Query) for sub-2-second performance.
- Azure Container Apps: Runs containerized BFF and microservices with minimal cloud expertise required.
- Azure Service Bus: Handles asynchronous, decoupled event messaging between platform and legacy systems.
- Azure Entra ID & OAuth 2.0 / PKCE: Secures single sign-on (SSO) and RBAC integrated with corporate Active Directory.
- Azure Application Insights: Provides Real User Monitoring (RUM) and error telemetry.

## Rationale
This hybrid architecture isolates expensive mainframe dependencies while delivering modern, high-performance web experiences for adjusters. It satisfies strict compliance, consistency, and sub-second performance constraints using managed Azure cloud services suited for teams with limited cloud experience.