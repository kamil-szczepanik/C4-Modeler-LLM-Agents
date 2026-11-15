## Overview
This system gradually replaces a legacy COBOL/DB2 mainframe claims platform with a modern, hybrid cloud architecture. Its core purpose is to enable online claim submission and adjuster workflows while maintaining seamless integration with the legacy system during a multi-year migration.

## Key Elements
* Customer Portal (React/TypeScript SPA)
* Web Frontend (React/TypeScript SPA)
* API Gateway / BFF (Node.js/Express)
* Claims Core Service (.NET 8 / C#)
* Integration & Sync Worker (Python/C# Azure Function)
* Claims Database (Azure SQL Database Managed Instance)
* Integration Event Broker (Azure Service Bus)
* Distributed Cache / State Store (Azure Cache for Redis)
* Configuration & Feature Store (Azure App Configuration)
* Legacy Mainframe (COBOL/DB2 on-premises)

## Relationships
* Customer Portal & Web Frontend -> API Gateway / BFF via HTTPS/REST and WSS (JSON)
* API Gateway / BFF -> Claims Core Service via gRPC / HTTP/2
* Claims Core Service -> Claims Database via TDS over TLS (TCP 1433)
* Claims Core Service -> Integration Event Broker via AMQP over TLS (TCP 5671)
* Integration & Sync Worker -> Legacy Mainframe via secure SFTP/MQ
* API Gateway / BFF and SPAs -> Azure AD / Entra ID via OpenID Connect (OIDC) over HTTPS
* Claims Core Service -> Configuration & Feature Store via HTTPS/REST

## Technology Stack
* Azure Static Web Apps: Hosts frontend SPAs for regional users
* Azure Container Apps: Runs containerized microservices and BFF to simplify cloud operations
* .NET 8 / C# and Node.js: Core backend and API runtime technologies
* Azure SQL Database: Provides relational persistence and ACID consistency for migrated claims
* Azure Service Bus: Asynchronously decouples services to prevent data loss and protect legacy batch limits
* Azure Cache for Redis: Handles distributed session caching and idempotency keys
* Azure App Configuration: Enables dynamic feature flagging for rapid claim-type switch-backs

## Rationale
Fully managed Azure PaaS services compensate for the team's limited cloud experience while lowering operational overhead. Asynchronous messaging and dynamic configuration routing successfully isolate expensive mainframe dependencies and satisfy strict migration, performance, and consistency constraints.