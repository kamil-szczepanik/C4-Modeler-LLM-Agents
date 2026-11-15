## Overview
The Insurance Claims Modernization system gradually replaces a legacy COBOL/DB2 mainframe with a hybrid cloud platform. It enables online claims submission and adjuster workflows while maintaining synchronization with the legacy system of record.

## Key Elements
* Customer Portal (Azure Static Web Apps / React)
* Adjuster Workspace (Azure Container Apps / .NET Core)
* API Gateway (Azure Container Apps / .NET Yit)
* Claims Core Service (Azure Container Apps / .NET Core)
* Anti-Corruption Layer (ACL) (Azure Container Apps / Camel or .NET)
* Integration Message Broker (Azure Service Bus)
* Database (Azure SQL Database / EF Core)
* Legacy Mainframe (COBOL/DB2 on-premise)
* Identity Provider (Microsoft Entra ID / OpenID Connect)

## Relationships
* Customer Portal & Adjuster Workspace $\rightarrow$ API Gateway via HTTPS/WSS
* API Gateway $\rightarrow$ Claims Core Service & Adjuster Workspace via gRPC/HTTP
* API Gateway $\leftrightarrow$ Identity Provider via OpenID Connect
* Claims Core Service $\leftrightarrow$ Integration Message Broker via AMQP
* Integration Message Broker $\rightarrow$ ACL via AMQP
* ACL $\rightarrow$ Legacy Mainframe via MQ/File Transfer

## Technology Stack
* Azure West Europe: Primary cloud region chosen for the modern platform containers.
* .NET Core / C#: Core application runtime chosen to balance enterprise standards with team capabilities.
* Azure Container Apps: Container hosting platform to simplify cloud deployment for an inexperienced team.
* Azure Service Bus: Message broker ensuring reliable at-least-once message delivery.
* Azure SQL Database / EF Core: Relational storage supporting the CQRS read models.
* Microsoft Entra ID: Single sign-on integration with on-premise Active Directory.

## Rationale
This hybrid architecture isolates the expensive-to-change legacy mainframe behind an Anti-Corruption Layer while using asynchronous messaging to guarantee consistency and sub-second performance. The chosen Azure and .NET technologies lower the adoption barrier for a team with limited cloud experience.