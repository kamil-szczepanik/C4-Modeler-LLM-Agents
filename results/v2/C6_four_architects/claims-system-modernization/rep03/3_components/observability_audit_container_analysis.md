## Overview
The Insurance Claims Modernization platform gradually replaces a legacy COBOL/DB2 mainframe claims system with a modern Azure cloud solution while maintaining continuous hybrid operations. It provides online claim submission, adjuster workflows, and incremental claim-type migrations without downtime or data loss.

## Key Elements
- **Users**: Customer, Broker, Claims Adjuster
- **External Systems**: Active Directory, Core Rating & Underwriting Engine, Payment Gateway, Notification Service, Legacy Mainframe
- **Frontends**: Web Portal, Adjuster Web Application (React / TypeScript on Azure Static Web Apps)
- **Gateways & Core Services**: API Gateway / BFF (Azure API Management / Node.js), Claims Management App, Claim Routing Service, Integration & Sync Service (Azure Container Apps)
- **Observability Container**: Telemetry Collector, Audit Log Processor, Alerting & Dashboard Engine, Migration Trace Correlator, Security & Access Auditor (Azure Application Insights / Azure Monitor)
- **Data & Storage**: Claims Database (Azure SQL Database), Notification & Document Store (Azure Blob Storage / Cosmos DB with WORM), Mainframe Data Ingestion Worker (Azure Functions / Data Factory)

## Relationships
- **Customer / Broker** -> **Web Portal**: Submits claims [HTTPS]
- **Claims Adjuster** -> **Adjuster Web Application**: Manages claims [HTTPS]
- **Web Portal / Adjuster App** -> **API Gateway / BFF**: Routes client requests [HTTPS/REST]
- **API Gateway** -> **Claims Management App & Services**: Dispatches domain commands [gRPC / HTTPS]
- **Integration & Sync Service** -> **Legacy Mainframe**: Synchronizes claims data [Batch / MQ / File Transfer]
- **All Platform Containers** -> **Observability Container (Telemetry Collector)**: Sends telemetry [OpenTelemetry / HTTPS]
- **Audit Log Processor** -> **Notification & Document Store**: Persists tamper-evident logs [Azure SDK / WORM Blob Storage]

## Technology Stack
- **Frontend**: React and TypeScript hosted on Azure Static Web Apps for rapid, modern UI delivery.
- **Backend Compute**: Azure Container Apps for scalable microservices and Azure Functions for lightweight ingestion tasks.
- **Integration & Messaging**: Azure Service Bus for reliable asynchronous messaging between services.
- **Databases**: Azure SQL Database for transactional claim data and Azure Cosmos DB / Blob Storage for documents and audit logs.
- **Observability**: Azure Monitor, Application Insights, and OpenTelemetry (OTLP) for distributed tracing and audit logging.

## Rationale
This hybrid architecture isolates expensive mainframe modifications by using an integration layer and Azure Container Apps to gradually migrate claim types while ensuring zero data loss (R-04). Fully managed Azure services reduce operational overhead for a team with limited cloud experience.