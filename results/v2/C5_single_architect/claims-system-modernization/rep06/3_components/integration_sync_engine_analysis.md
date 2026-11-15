## Overview
The Insurance Claims Modernization system gradually replaces a legacy COBOL/DB2 mainframe with a hybrid Azure platform. The Integration & Sync Engine ensures reliable, zero-loss data synchronization and bridging between modern cloud services and the legacy system.

## Key Elements
- Inbound Event Consumer (Azure Function)
- Mainframe Batch Staging Repository (Azure SQL / Cosmos DB)
- Outbound Sync Orchestrator (Azure Function / Durable Functions)
- Reconciliation & Dead Letter Monitor (Azure Function / Timer Trigger)
- Legacy Mainframe (COBOL/DB2, On-Premises)
- Core Domain Service (Azure Container Apps)

## Relationships
- Core Domain Service -> Inbound Event Consumer [AMQP / Azure Service Bus]
- Inbound Event Consumer -> Mainframe Batch Staging Repository [Entity Framework Core / SQL]
- Outbound Sync Orchestrator -> Mainframe Batch Staging Repository [Entity Framework Core / SQL]
- Outbound Sync Orchestrator -> Legacy Mainframe COBOL/DB2 [SFTP / IBM MQ]
- Reconciliation & Monitor -> Mainframe Batch Staging Repository [SQL]
- Reconciliation & Monitor -> Legacy Mainframe COBOL/DB2 [SFTP/Query - Read-Only]

## Technology Stack
- Azure Functions / Durable Functions: Serverless execution for event consumption and stateful orchestration.
- Azure Service Bus: Reliable messaging infrastructure supporting AMQP for zero claim loss.
- Azure SQL / Cosmos DB: Local buffering to decouple real-time events from the rigid mainframe batch window.
- SFTP / IBM MQ: Secure legacy integration protocols respecting quarterly interface constraints.

## Rationale
This component architecture decouples real-time cloud operations from the legacy mainframe's strict batch window and limited interface change capacity. It guarantees zero claim loss and rapid rollback capabilities despite the hybrid cloud-mainframe constraints.