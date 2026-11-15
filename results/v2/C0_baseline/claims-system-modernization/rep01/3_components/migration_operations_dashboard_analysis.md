## Overview
[The Migration Operations Dashboard provides real-time visibility, reconciliation alerts, and kill-switch controls to safely manage the multi-year transition from the legacy mainframe to the modern platform.]

## Key Elements
- Dashboard UI (React SPA)
- Dashboard API Controller (.NET Core Web API)
- Reconciliation Engine (.NET Core Component)
- Kill-Switch Orchestrator (.NET Core Component)
- Reconciliation Report Generator (.NET Core Component)
- Discrepancy Translation Service (.NET Core Component)

## Relationships
- Dashboard UI interacts with Dashboard API Controller via HTTPS/REST and SignalR
- Dashboard API Controller invokes Reconciliation Engine via MediatR domain events
- Reconciliation Engine queries PostgreSQL Read-Cache via EF Core and Legacy Mainframe via Anti-Corruption Layer (ACL)
- Kill-Switch Orchestrator publishes domain events to Azure Service Bus
- Reconciliation Report Generator stores/retrieves files in Azure Blob Storage

## Technology Stack
- React SPA: Chosen for modern UI capabilities while aligning with the team's skillset
- .NET Core: Selected for robust backend microservices and API controllers
- Azure Service Bus: Used for reliable asynchronous operational command dispatch
- Azure Blob Storage: Implemented for scalable asynchronous export file storage
- Microsoft Entra ID: Enforces strict Role-Based Access Control (RBAC)

## Rationale
- This architecture fits requirements by isolating complex migration logic into dedicated components while enforcing strict security, operational guardrails, and rapid 24-hour rollback capabilities.