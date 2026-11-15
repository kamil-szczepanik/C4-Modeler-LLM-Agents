## Overview
The system is a modern, hybrid insurance claims platform that incrementally replaces a 30-year-old mainframe while ensuring zero downtime and continuous data consistency. Its core purpose is to modernize customer submissions and adjuster workflows while maintaining legacy integration.

## Key Elements
- **Users**: Customer & Broker, Claims Adjuster, IT Administrator
- **External Systems**: Legacy Mainframe (On-Premises), Insurer's Active Directory (Azure AD / Entra ID), Payment Gateway
- **Containers**: Web Portal, Adjuster Workspace, API Management Proxy, Claims Processing Service, Claim Routing Service, Primary Datastore, Claim Read Model Store, Mainframe Integration Adapter, Data Sync Worker, Audit and Reconciliation Service
- **Components (Claim Read Model Store)**: Claim Projection Container (Cosmos DB), Cosmos DB Access Control, Cosmos DB Change Feed, Cosmos DB Telemetry & Diagnostic Component

## Relationships
- `Customer & Broker` -> `Web Portal`: Submits claims [HTTPS]
- `Adjuster Workspace` -> `Claim Projection Container`: Queries read models directly [HTTPS / Cosmos DB SDK]
- `Adjuster Workspace` -> `Cosmos DB Access Control`: Validates scoped tokens [HTTPS]
- `Data Sync Worker` -> `Claim Projection Container`: Upserts denormalized read models [TCP / Cosmos DB SDK]
- `Claim Projection Container` -> `Audit and Reconciliation Service`: Streams mutation events [Change Feed API]
- `Claim Projection Container` -> `Cosmos DB Telemetry & Diagnostic Component`: Emits performance metrics [Azure Monitor Diagnostics]

## Technology Stack
- **Frontend**: React on Azure Static Web Apps / Azure App Service for responsive UI (<2s load time)
- **Backend Services**: Java / Spring Boot on Azure Container Apps for scalable microservices
- **Messaging & Routing**: Azure Service Bus for event-driven decoupled claim routing
- **Databases**: Azure SQL Database (Primary Datastore) and Azure Cosmos DB (Claim Read Model Store for low-latency queries)
- **Integration & Security**: IBM MQ (On-Premises Mainframe Adapter) and Microsoft Entra ID (Azure AD SSO)

## Rationale
This hybrid architecture isolates expensive mainframe changes while enabling rapid, cloud-native adjuster experiences that meet performance and security constraints. It leverages managed Azure services to mitigate the team's limited cloud experience while ensuring zero data loss during incremental migration.