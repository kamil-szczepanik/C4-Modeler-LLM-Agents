## Overview
This hybrid cloud architecture modernizes a regional insurer's claims platform by migrating claim types from a 30-year-old mainframe to Azure while maintaining strict data consistency. A dedicated Migration Analytics Container provides executive visibility, automated reconciliation, and discrepancy triage to de-risk the 3-year migration.

## Key Elements
- Claims Operations Director and Migration Program Manager (Users)
- Migration Analytics Container (Azure Container Apps)
- Reconciliation Engine Component (Node.js/TypeScript)
- Metrics Aggregator Component (Python/Pandas)
- Discrepancy Triage Service Component (Node.js)
- Analytics API & UI Component (Express/React)
- Anti-Corruption Layer (ACL) and Azure Service Bus

## Relationships
- Migration Analytics Container to Anti-Corruption Layer via gRPC over mTLS
- Reconciliation Engine to Azure Service Bus via AMQP for event consumption
- Analytics API to Management Clients via HTTPS/REST
- Reconciliation Engine to legacy DB2 via Anti-Corruption Layer for data comparison

## Technology Stack
- Azure Container Apps: Container hosting chosen for simplicity
- Node.js/TypeScript & Python/Pandas: Component runtimes for reconciliation and telemetry
- Azure Database for PostgreSQL: State store with AES-256 encryption at rest
- KEDA (Kubernetes Event-driven Autoscaling): Scales analytics workloads to respect the 23:00-05:00 batch window
- Azure Managed Identities & Azure RBAC: Zero-trust authentication and authorization

## Rationale
The architecture isolates legacy interactions behind an Anti-Corruption Layer and enforces automated reconciliation to guarantee zero data loss. Utilizing managed Azure services minimizes operational overhead for a team with limited cloud experience.