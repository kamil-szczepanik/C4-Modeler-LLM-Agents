## Overview
[The Data Sync & Reconciliation Jobs component synchronizes data and reconciles state between the modern Azure platform and the legacy on-premise mainframe. It guarantees zero data loss or duplication during the hybrid migration of insurance claims.]

## Key Elements
- Data Sync & Reconciliation Jobs (Azure Container Apps - Jobs)
- COBOL/DB2 Mainframe System of Record
- Azure Service Bus & Dead-Letter Queues (DLQ)
- Azure Key Vault & Managed Identities
- Azure Monitor & Azure Sentinel

## Relationships
- Azure Service Bus -> Data Sync & Reconciliation Jobs: Triggers sync and processing queues [AMQP]
- Data Sync & Reconciliation Jobs -> COBOL/DB2 Mainframe System of Record: Syncs data and reconciles state across hybrid boundary [mTLS with certificate pinning]
- Data Sync & Reconciliation Jobs -> Azure Key Vault: Retrieves database credentials dynamically [HTTPS / Managed Identity]
- Data Sync & Reconciliation Jobs -> Azure Monitor: Streams drift metrics and reconciliation logs [HTTPS]

## Technology Stack
- Azure Container Apps (Jobs): Provides managed cron-based scheduling and simpler operational debugging for teams with low cloud experience
- Azure Service Bus: Enables reliable asynchronous messaging and dead-letter queueing for failed events
- Managed Identities & Azure Key Vault: Secures credentials without hardcoding secrets
- mTLS with Certificate Pinning: Secures hybrid network traffic across the on-premise boundary

## Rationale
[This architecture uses containerized jobs and managed Azure services to minimize operational complexity for a low-experience cloud team. Asynchronous staging and strict idempotency protect the fragile legacy mainframe within its mandatory batch window while guaranteeing strict data consistency.]