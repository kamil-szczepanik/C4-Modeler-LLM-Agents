## Overview
The Insurance Claims Modernization platform gradually replaces a legacy COBOL/DB2 mainframe with a modern Azure-based cloud system. The hybrid architecture ensures zero data loss and supports incremental claim type migration while maintaining the mainframe as the system of record.

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Customer Portal (Azure Static Web Apps)
- Adjuster Workspace (Azure App Service)
- Migration Router (Azure Container Apps)
- Claims Core API (Azure Container Apps, Azure SQL)
- Integration Gateway & Sync Worker (Azure Functions)
- Mainframe Adapter Component (C# Azure Functions)
- Sync Orchestrator Component (Azure Durable Functions)
- Outbox Processor Component (C# Azure Functions)
- Circuit Breaker & Fallback Handler Component (C# Azure Functions)
- Legacy Mainframe (COBOL/DB2)
- Azure Service Bus
- Active Directory

## Relationships
- Customers & Brokers -> Customer Portal: Submits online claims [HTTPS]
- Claims Adjuster -> Adjuster Workspace: Manages claims [HTTPS]
- Customer Portal & Adjuster Workspace -> Migration Router: Routes claim traffic [HTTPS/JSON]
- Migration Router -> Claims Core API: Processes migrated claim types [HTTPS/REST]
- Migration Router -> Mainframe Adapter: Forwards unmigrated claim traffic [HTTPS/JSON]
- Outbox Processor -> Azure Service Bus: Publishes transactional messages [AMQP]
- Mainframe Adapter -> Circuit Breaker & Fallback Handler: Delegates outbound legacy calls [HTTPS/SOAP]
- Circuit Breaker & Fallback Handler -> Legacy Mainframe: Invokes legacy endpoints with resilience policies [HTTPS/SOAP]
- Sync Orchestrator -> Legacy Mainframe: Bulk data synchronization and batch reconciliation [DB2 Direct / SFTP]

## Technology Stack
- Azure Functions (.NET/C#): Serverless compute for integration components, matching the team's skillset.
- Azure Durable Functions: Manages reliable state reconciliation sagas without complex orchestration frameworks.
- Azure Service Bus: Ensures reliable, asynchronous message delivery and transactional outbox processing.
- Azure Container Apps: Hosts modern APIs and routing microservices.
- Azure SQL: Provides relational data persistence for the modern platform.
- Active Directory: Enforces enterprise single sign-on security.

## Rationale
The hybrid serverless architecture minimizes operational overhead for a cloud-inexperienced team while strictly adhering to legacy mainframe constraints. Decoupled integration components guarantee transactional consistency and rapid fallback capabilities required during incremental migration.