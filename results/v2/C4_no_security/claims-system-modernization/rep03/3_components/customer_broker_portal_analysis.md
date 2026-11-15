## Overview
Modernizes a regional insurer's claims platform by replacing a 30-year-old mainframe via a gradual, hybrid cloud migration. Maintains system integrity and zero-downtime processing while migrating claim types one by one.

## Key Elements
* Customers & Brokers
* Claims Adjusters
* Customer & Broker Portal (React SPA / Azure Static Web Apps)
* Adjuster Web Application (React SPA / Azure Static Web Apps)
* API Gateway / BFF (Node.js / NestJS)
* Claims Core Processing Service (.NET Core / C# on Azure App Service)
* Mainframe Integration Adapter (Azure Functions / App Service)
* Azure Service Bus with DLQ
* Azure SQL Database
* Legacy COBOL/DB2 Mainframe (On-premises)
* Insurer's Active Directory / Azure AD

## Relationships
* Customers & Brokers -> Customer & Broker Portal: Submits and manages claims [HTTPS/JSON]
* Customer & Broker Portal -> API Gateway / BFF: Communicates for data and operations [HTTPS/REST]
* Customer & Broker Portal -> Azure AD: Authenticates users [OAuth2/OpenID Connect]
* Customer & Broker Portal -> Azure Blob Storage: Uploads attachments directly [HTTPS/SAS Tokens]
* Adjuster Web Application -> API Gateway / BFF: Manages claims [HTTPS/REST]
* API Gateway / BFF -> Claims Core Processing Service: Invokes core logic [gRPC/HTTPS]
* Claims Core Processing Service -> Azure SQL Database: Persists state [T-SQL/TCP]
* Claims Core Processing Service -> Azure Service Bus: Publishes domain events [AMQP]
* Mainframe Integration Adapter -> Legacy COBOL/DB2 Mainframe: Syncs legacy claims [Batch/MQ]

## Technology Stack
* Frontend: React SPA hosted on Azure Static Web Apps for rapid, cloud-simple delivery
* Backend API: Node.js with NestJS and .NET Core / C# for robust business logic
* Integration & Messaging: Azure Service Bus with Dead Letter Queues for reliable event streaming
* Database: Azure SQL Database for relational transactional storage
* Cloud Provider: Hybrid architecture spanning On-Premises Mainframe and Azure West Europe

## Rationale
The hybrid architecture balances strict legacy constraints with modern cloud capabilities by keeping the mainframe as the system of record while offloading new workloads to Azure. Using managed services like Azure Static Web Apps and Azure App Service minimizes operational overhead for a team with limited cloud experience.