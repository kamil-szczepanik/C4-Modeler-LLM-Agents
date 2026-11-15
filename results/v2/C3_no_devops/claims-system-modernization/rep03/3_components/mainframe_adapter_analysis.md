## Overview
[The system modernizes a 30-year-old COBOL/DB2 mainframe claims system via a hybrid cloud platform while ensuring uninterrupted legacy operations. The core purpose is to migrate claim types incrementally without risking data loss or exceeding strict mainframe change budgets.]

## Key Elements
* Customer Portal & Adjuster Web App (Azure Container Apps / React)
* API Gateway (Azure API Management)
* Claims Domain Services (Azure Container Apps / .NET Core)
* Integration & Anti-Corruption Layer (Azure Service Bus)
* Mainframe Adapter Container (Azure Container Apps / .NET Core)
* Request Translator Component (.NET Core)
* LU6.2 Protocol Bridge Component (C#/.NET native sockets)
* Outbox & State Cache Component (Entity Framework Core / Redis)
* Telemetry & Audit Emitter Component (.NET Core / OpenTelemetry)
* Claims Audit Store (Azure Cosmos DB)
* Legacy Mainframe Claims System (COBOL/DB2 on-premise)
* Identity Provider (Active Directory)

## Relationships
* Adjuster Web App -> API Gateway: Forwards user actions [HTTPS/REST]
* API Gateway -> Claims Domain Services: Routes validated API requests [HTTPS/gRPC]
* Claims Domain Services -> Integration & Anti-Corruption Layer: Publishes claim events [AMQP]
* Integration & Anti-Corruption Layer -> Mainframe Adapter: Transfers integration messages [AMQP]
* Request Translator -> LU6.2 Protocol Bridge: Invokes in-memory message mapping [Direct]
* LU6.2 Protocol Bridge -> Legacy Mainframe Claims System: Transmits framed byte arrays [Custom TCP/LU6.2 over mTLS / ExpressRoute]
* Telemetry & Audit Emitter -> Claims Audit Store: Persists audit logs [HTTPS/Cosmos SDK]

## Technology Stack
* Azure Container Apps: Hosts microservices with low cloud experience overhead
* .NET Core: Powers backend domain services and mainframe adapter components
* Redis & Entity Framework Core: Implements transactional outbox pattern and state caching
* Azure Service Bus: Asynchronously decouples cloud services from the legacy mainframe
* Custom TCP/LU6.2 over ExpressRoute/IPsec VPN: Bridges modern cloud architecture to legacy mainframe
* Azure Cosmos DB: Stores tamper-evident transaction audits and compliance logs

## Rationale
[This hybrid architecture bridges modern cloud services with a legacy mainframe while strictly adhering to integration and performance constraints. Internal component decomposition guarantees high-performance adjuster UI responses despite slow legacy lag and provides a rapid rollback mechanism.]