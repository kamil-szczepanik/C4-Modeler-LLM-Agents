## Overview
The Insurance Claims Modernization platform gradually replaces a legacy COBOL/DB2 mainframe with a modern Azure-hosted cloud solution while maintaining continuous claims processing. It utilizes a hybrid cloud architecture to ensure data consistency, rapid UI performance, and secure Active Directory authentication.

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Legacy Mainframe (COBOL/DB2)
- Active Directory
- Claims Web Application (React, Azure Static Web Apps)
- API Gateway / BFF (Azure Container Apps, .NET Core)
- Migration Router / Anti-Corruption Layer (Azure Container Apps, .NET Core)
- Mainframe Integration Adapter (Azure Container Apps, .NET Core)
- Azure Service Bus
- Azure Cache for Redis
- Azure SQL Managed Instance
- Message Listener Component (.NET Background Service)
- Translation & Mapping Engine (AutoMapper, C# Domain Logic)
- Legacy Protocol Client (IBM MQ .NET Client)
- Resiliency & Circuit Breaker Component (Polly)
- Audit & Reconciliation Logger (Entity Framework Core)

## Relationships
- Customers & Brokers -> Claims Web Application [HTTPS]
- Claims Adjusters -> Claims Web Application [HTTPS]
- Claims Web Application -> API Gateway / BFF [HTTPS/REST]
- API Gateway / BFF -> Migration Router / Anti-Corruption Layer [gRPC/HTTPS]
- Migration Router -> Azure SQL Managed Instance [T-SQL]
- Migration Router -> Azure Service Bus [AMQP]
- Azure Service Bus -> Mainframe Integration Adapter [AMQP]
- Message Listener -> Translation & Mapping Engine [In-memory]
- Translation & Mapping Engine -> Legacy Protocol Client [In-memory]
- Legacy Protocol Client -> Legacy Mainframe (COBOL/DB2) [TCP/IBM MQ]
- Translation & Mapping Engine -> Audit & Reconciliation Logger [In-memory]
- Audit & Reconciliation Logger -> Azure SQL Managed Instance [T-SQL]

## Technology Stack
- Azure Container Apps (.NET Core): Scalable container hosting for microservices.
- Azure Service Bus (AMQP): Asynchronous messaging for decoupling systems.
- Azure SQL Managed Instance (T-SQL): Relational database for state and audit logging.
- IBM MQ .NET Client (TCP): Reliable protocol for legacy mainframe integration.
- Polly (.NET): Resilience and circuit breaking for fault tolerance.
- AutoMapper / C# (.NET): Payload transformation for legacy copybooks.
- React (Azure Static Web Apps): Responsive frontend for claims adjusters.

## Rationale
This hybrid architecture isolates expensive mainframe interactions behind an Anti-Corruption Layer and Integration Adapter, ensuring strict zero-loss consistency and rapid UI response times. Leveraging Azure Container Apps with .NET Core provides a maintainable, cloud-native path forward despite the team's limited initial cloud experience.