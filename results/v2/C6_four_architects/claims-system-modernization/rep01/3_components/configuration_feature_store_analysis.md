## Overview
[The system modernizes a 30-year-old mainframe claims platform through a hybrid cloud architecture, enabling gradual claim type migration while maintaining business continuity. It provides online claim submission and adjuster web portals backed by Azure cloud services and an on-premise mainframe system of record.]

## Key Elements
* Customer Portal and Web Frontend (React / TypeScript SPA)
* API Gateway / BFF (Node.js / Express)
* Claims Core Service (.NET 8 / C#)
* Integration & Sync Worker (Python / C# Azure Function)
* Claims Database (Azure SQL Database Managed Instance)
* Integration Event Broker (Azure Service Bus)
* Distributed Cache / State Store (Azure Cache for Redis)
* Configuration & Feature Store (Azure App Configuration)
* External Systems: Legacy Mainframe (COBOL/DB2) and Active Directory / Entra ID

## Relationships
* Customer Portal / Web Frontend -> API Gateway / BFF: Routes user requests [HTTPS/REST]
* API Gateway / BFF -> Claims Core Service: Forwards processed claims and UI requests [gRPC / HTTPS]
* Claims Core Service -> Claims Database: Persists modern claim records [T-SQL / TDS]
* Claims Core Service -> Integration Event Broker: Publishes and consumes domain events [AMQP / Azure Service Bus]
* Integration & Sync Worker -> Legacy Mainframe: Synchronizes data between cloud and legacy systems [Batch / MQ]
* Claims Core Service / BFF -> Configuration & Feature Store: Evaluates feature flags and dynamic routing rules [HTTPS/REST]

## Technology Stack
* Frontend: React with TypeScript for modern responsive user interfaces
* Backend Services: Node.js / Express for BFF and .NET 8 / C# for core domain processing
* Database: Azure SQL Database Managed Instance for relational claim data storage
* Integration & Messaging: Azure Service Bus for asynchronous messaging and Azure Event Grid for event routing
* Configuration: Azure App Configuration with Key Vault references for dynamic feature toggles and secure secrets

## Rationale
* The hybrid cloud approach isolates legacy mainframe constraints while incrementally migrating business capabilities to Azure. 
* Azure App Configuration and event-driven caching ensure sub-second feature toggles required for rapid rollback constraints.