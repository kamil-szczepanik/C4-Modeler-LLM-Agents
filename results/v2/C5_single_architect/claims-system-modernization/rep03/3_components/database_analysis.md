## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure-hosted hybrid platform. It ensures seamless claim processing, zero data loss, and sub-second adjuster UI response times during the multi-year migration.

## Key Elements
* Customer / Broker & Claims Adjuster (Users)
* Legacy Mainframe & Active Directory (External Systems)
* Customer Portal (Azure Static Web Apps / React)
* Adjuster Workspace (Azure Container Apps / .NET Core)
* API Gateway (Azure Container Apps / .NET Yit)
* Claims Core Service (Azure Container Apps / .NET Core)
* Anti-Corruption Layer (ACL)
* Integration Message Broker (Azure Service Bus)
* Database (Azure SQL Database / EF Core) containing:
  - Claim Write Model Component
  - Claim Read Model Component
  - Migration & Audit Log Component
  - Integration Staging Component

## Relationships
* Customer / Broker -> Customer Portal: Submits online claims [HTTPS / TLS]
* Claims Adjuster -> Adjuster Workspace: Manages claims [HTTPS / TLS]
* Customer Portal & Adjuster Workspace -> API Gateway: Routes requests [HTTPS / REST]
* API Gateway -> Claims Core Service: Dispatches business logic [gRPC / Internal Network]
* Claims Core Service -> Database: Reads/writes domain data [EF Core / TDS]
* Claims Core Service -> Integration Staging Component: Transforms staged payloads [Stored Procedures / TDS]
* Claims Core Service <-> Integration Message Broker: Publishes/consumes events [AMQP / Azure Service Bus]
* Anti-Corruption Layer <-> Legacy Mainframe: Syncs claim types [MQ / SNA]
* Adjuster Workspace -> Active Directory: Authenticates users [OpenID Connect / OAuth 2.0]

## Technology Stack
* Azure West Europe & On-Premises Mainframe: Hybrid cloud foundation meeting data residency and connectivity needs.
* Azure Container Apps & .NET Core: Scalable microservices architecture for APIs and workers.
* Azure SQL Database & EF Core: Relational storage using Temporal Tables, Row-Level Security, and JSON Support for CQRS, auditability, and rapid staging.
* Azure Service Bus: Asynchronous messaging guaranteeing reliable event-driven state synchronization.
* Azure Static Web Apps & React: High-performance frontend for customer interactions.

## Rationale
This hybrid architecture isolates expensive mainframe changes behind an Anti-Corruption Layer while modernizing the user experience in Azure. It leverages CQRS and database staging components to meet strict consistency, performance, and one-day rollback requirements.