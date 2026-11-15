## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern hybrid cloud platform. It enables online claims submission and adjuster workflows while maintaining synchronization with the legacy system of record.

## Key Elements
- Customer / Broker (Person)
- Claims Adjuster (Person)
- Customer Portal (Azure Static Web Apps / React)
- Adjuster Workspace (Azure Container Apps / .NET Core)
- API Gateway (Azure Container Apps / .NET Yit)
- Claims Core Service (Azure Container Apps / .NET Core)
- Integration Message Broker (Azure Service Bus with Claim Routing Topic, Session Processor, and Dead-Letter Subsystem)
- Anti-Corruption Layer (ACL) (On-premise / Azure)
- Database (Azure SQL Database / EF Core)
- Legacy Mainframe (On-prem-mainframe / COBOL/DB2)
- Identity Provider (Azure Active Directory)

## Relationships
- Customer / Broker -> Customer Portal: Submits claims [HTTPS]
- Claims Adjuster -> Adjuster Workspace: Manages claims [HTTPS/SSO]
- Customer Portal -> API Gateway: Forwards online claims [HTTPS/REST]
- Adjuster Workspace -> API Gateway: Executes adjuster operations [HTTPS/REST]
- API Gateway -> Claims Core Service: Routes API requests [gRPC/Internal]
- Claims Core Service -> Database: Reads/writes claim state [ADO.NET/EF Core]
- Claims Core Service -> Claim Routing Topic: Publishes domain events [AMQP over TLS]
- Claim Routing Topic -> Session Processor: Enforces ordered delivery per session ID [AMQP]
- Session Processor -> Anti-Corruption Layer (ACL): Forwards synchronized events [AMQP]
- ACL -> Legacy Mainframe: Synchronizes claim data [Batch/Interface]

## Technology Stack
- Azure Service Bus: Chosen for native persistent messaging, duplicate detection, and dead-lettering to satisfy zero-data-loss requirements (R-04).
- Azure Container Apps & .NET Core: Provides scalable, maintainable microservices with low cloud-experience overhead.
- Azure SQL Database with EF Core: Delivers reliable relational persistence for the modern platform.
- Azure Active Directory: Enables seamless Single Sign-On (R-07) across internal user workspaces.

## Rationale
This hybrid architecture isolates expensive mainframe changes while allowing incremental claim-type migration via Azure Service Bus routing and sessions. It decouples the sub-second modern UI from slower legacy responses, ensuring high performance and maintainability.