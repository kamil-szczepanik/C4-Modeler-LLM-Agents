## Overview
[The system modernizes a 30-year-old regional insurance claims mainframe by gradually migrating claim types to a cloud-native platform while ensuring zero data loss and maintaining the legacy system of record. It uses a hybrid architecture spanning on-premises infrastructure and Azure West Europe.]

## Key Elements
- Claims API Gateway / BFF
- Integration & Sync Service (Azure Container Apps worker)
- Sync Orchestrator Component (.NET 8)
- Mainframe Adapter Component (.NET 8 with Polly)
- Reconciliation & DLQ Manager Component (.NET 8 / Azure Functions)
- Business Rule Validator Component (.NET 8)
- Messaging Consumer/Publisher Component (Azure Service Bus SDK)
- Audit & Event Store (Azure Cosmos DB)
- Legacy Mainframe System (COBOL/DB2 on-prem)
- Corporate Active Directory

## Relationships
- Claims API Gateway / BFF -> Integration & Sync Service: Communicates via [HTTPS/JSON and Azure Service Bus]
- Sync Orchestrator -> Mainframe Adapter: Internal [In-Process / C# interface calls]
- Sync Orchestrator -> Business Rule Validator: Internal [In-Process / C#]
- Sync Orchestrator -> Messaging Consumer/Publisher: Enqueues/Deconstructs events via [Azure Service Bus SDK]
- Reconciliation & DLQ Manager -> Azure Service Bus: Inspects and replays failed messages via [AMQP]
- Reconciliation & DLQ Manager -> Audit & Event Store: Reads/Writes reconciliation states via [TCP / Cosmos DB SDK]
- Mainframe Adapter -> Legacy Mainframe System: Synchronizes data via [IPsec VPN or Azure ExpressRoute using mTLS / TLS 1.3]

## Technology Stack
- .NET 8: Core framework for internal service components due to robustness and team alignment
- Azure Container Apps: Hosting environment for worker and sync containers, providing managed scaling
- Azure Service Bus: Asynchronous messaging backbone ensuring reliable delivery and queue management
- Azure Cosmos DB: Audit and event store for immutable logging and reconciliation tracking
- Polly: Resilience framework implementing circuit breakers and rate-limiting to protect the legacy mainframe
- Azure Key Vault: Secure secret and certificate management using managed identities

## Rationale
[This hybrid architecture protects the 3-year migration timeline by isolating fragile mainframe interactions behind resilient adapters and rate-limiters. It guarantees consistency and rapid rollback capabilities for migrated claim types while accommodating the team's low initial cloud experience through managed Azure services.]