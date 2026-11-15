## Overview
[Replaces the legacy mainframe claims system via a hybrid cloud modernization platform. Manages gradual claim type migration while ensuring zero data loss and strict consistency.]

## Key Elements
- Reconciliation Worker (Azure Container Apps Background Jobs)
- Mainframe Data Extractor (C# / .NET Worker Service)
- Platform State Comparator (C# / .NET Worker Service)
- Fallback Rule Evaluator (C# / .NET Worker Service)
- Discrepancy Notifier (Azure Service Bus)
- Audit & Reconciliation Ledger (Azure SQL Ledger)
- Legacy Mainframe System
- Operations/Migration Managers

## Relationships
- Reconciliation Worker -> Legacy Mainframe System: Pulls state snapshots [SFTP / Flat File / TLS 1.3]
- Mainframe Data Extractor -> Platform State Comparator: Streams raw records [In-Memory / Internal IPC]
- Platform State Comparator -> Audit & Reconciliation Ledger: Logs state comparisons [Entity Framework Core / TDS over TLS]
- Fallback Rule Evaluator -> Azure App Configuration: Fetches risk thresholds [HTTPS / Managed Identity]
- Fallback Rule Evaluator -> Discrepancy Notifier: Publishes enriched alerts [Azure Service Bus / AMQP]
- Reconciliation Worker -> Azure Key Vault: Retrieves encryption keys and secrets [HTTPS / Managed Identity]

## Technology Stack
- Azure Container Apps: Hosts background jobs without Kubernetes complexity, matching team skill levels.
- C# / .NET Worker Service: Provides lightweight, high-performance streaming compared to heavy frameworks like Apache Spark.
- Azure SQL Ledger: Guarantees tamper-resistant audit logs via cryptographic verification.
- Azure Service Bus: Asynchronously delivers enriched discrepancy alerts and automated rollback flags.
- Azure Key Vault: Centralizes cryptographic key management and secure secret rotation.

## Rationale
- Isolates complex reconciliation into automated background jobs to meet the strict 23:00-05:00 nightly batch window.
- Employs managed Azure services and standard .NET patterns to mitigate risks associated with the team's limited cloud experience.