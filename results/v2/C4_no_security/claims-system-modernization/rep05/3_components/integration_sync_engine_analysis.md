## Overview
The Integration & Sync Engine synchronizes the modern cloud platform with the legacy mainframe via batch file transfers and secure messaging. It ensures zero data loss and supports a gradual strangler-fig migration over three years.

## Key Elements
- Ingestion Router (.NET 8 Worker on AKS)
- Mainframe Batch Staging Store (Azure SQL Database Ledger)
- SFTP Sync Agent (AKS container)
- Dead-Letter & Reconciliation Monitor (Azure Monitor)
- Azure Service Bus

## Relationships
- Ingestion Router -> Azure Service Bus: Consumes events [AMQP]
- Ingestion Router -> Mainframe Batch Staging Store: Persists payloads [ADO.NET / SQL]
- SFTP Sync Agent -> Mainframe Batch Staging Store: Queries pending batches [ADO.NET / SQL]
- SFTP Sync Agent -> Legacy Mainframe: Transfers bulk files [SFTP]
- Dead-Letter & Reconciliation Monitor -> Observability Platform: Exports metrics [OpenTelemetry / HTTPS]

## Technology Stack
- Azure Service Bus: Asynchronous event ingestion and message buffering
- Azure SQL Database Ledger: Tamper-evident, 90-day immutable audit staging
- AKS (.NET 8): Container hosting for ingestion and sync agents
- Terraform & GitHub Actions: Infrastructure-as-Code and automated deployments
- Azure Monitor: Operational observability and alerting

## Rationale
The architecture decouples real-time cloud operations from rigid legacy batch windows using reliable message queues and staging stores. Azure SQL Ledger and AKS simplify operations for a team with limited cloud experience while guaranteeing strict data consistency.