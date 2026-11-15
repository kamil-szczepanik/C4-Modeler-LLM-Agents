## Overview
[The system modernizes a 30-year-old mainframe claims system through a hybrid cloud platform using Azure services. Its core purpose is to gradually migrate claim types while ensuring data consistency and continuous legacy processing.]

## Key Elements
- Claims Core Processing Service (.NET Core / C# on Azure App Service)
- Mainframe Integration Adapter (Azure Functions / App Service)
- Azure Service Bus (Standard Tier with DLQ)
- `Claims.Events` Topic (AMQP 1.0)
- `Mainframe.Outbox` Queue (with FIFO sessions)
- Dead-Letter Queue (DLQ) with DLQ Reprocessing Handler
- Azure SQL Database

## Relationships
- Claims Core Processing Service -> `Claims.Events`: Publishes domain events with W3C trace context [AMQP 1.0]
- Mainframe Integration Adapter -> `Mainframe.Outbox`: Consumes sync commands with FIFO ordering [AMQP 1.0]
- DLQ -> DLQ Reprocessing Handler: Forwards poisoned messages for administrative review [AMQP / Event Grid]

## Technology Stack
- Azure Service Bus: Chosen for reliable asynchronous messaging, topics, and DLQ support to meet consistency requirements (R-04) and enable quick rollbacks (R-06).
- Terraform / Bicep: Used for Infrastructure as Code (IaC) to ensure repeatable, drift-free deployments given the team's low cloud experience.
- Azure Managed Identities: Enforces secure Azure RBAC instead of connection strings for enhanced security.
- Application Insights / Azure Monitor: Implements tracking, alerting, and metrics for DLQ and subscription lag.

## Rationale
[This architecture successfully decouples the modern cloud platform from the legacy COBOL/DB2 mainframe using reliable asynchronous messaging and strict metadata tracking. It minimizes expensive mainframe changes while guaranteeing strict data consistency and low operational risk during the 3-year migration.]