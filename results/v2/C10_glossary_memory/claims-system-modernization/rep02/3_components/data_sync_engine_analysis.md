## Overview
[The system modernizes a regional insurer's claims platform via a hybrid architecture, gradually replacing the legacy mainframe while ensuring continuous operations.]
[The Data Sync Engine uses Azure Functions and Azure Service Bus to reliably synchronize claims between the cloud and the on-premises mainframe.]

## Key Elements
- Data Sync Engine [container] (Azure Service Bus & Azure Functions)
- Sync Ingestion Function [component] (Azure Functions (.NET))
- Mainframe Adapter Component [component] (Azure Functions (.NET))
- Dead-Letter & Reconciliation Handler [component] (Azure Functions (.NET))
- Idempotency Store [component] (Azure SQL Database)
- Legacy Mainframe System [externalSystem] (COBOL/DB2)
- Operations and Support Staff [person]
- Azure Monitor / Application Insights [externalSystem]
- Azure Key Vault [externalSystem]

## Relationships
- Sync Ingestion Function -> Idempotency Store (TDS (Tabular Data Stream) with encryption)
- Mainframe Adapter Component -> Legacy Mainframe System (Encrypted TCP/MQ with mTLS via Enterprise Service Bus)
- Dead-Letter & Reconciliation Handler -> Azure Monitor / Application Insights (HTTPS/TLS (REST))
- Mainframe Adapter Component -> Azure Key Vault (HTTPS/TLS (REST))

## Technology Stack
- Azure Functions (.NET): Chosen for serverless execution, minimizing infrastructure management for a team with limited cloud experience.
- Azure Service Bus: Provides reliable messaging, queuing, and dead-letter handling to prevent data loss (R-04).
- Azure SQL Database: Powers the Idempotency Store for deduplication and exactly-once processing.
- Azure Key Vault: Secures mTLS client certificates and encryption keys for compliance and security.
- Azure Monitor / Application Insights: Delivers native observability without custom UI maintenance overhead.

## Rationale
[The component architecture ensures strict data consistency (R-04) and rapid rollback capabilities (R-06) through idempotency, circuit breaking, and dead-letter handling.]
[Leveraging managed Azure serverless services reduces operational complexity and matches the team's existing cloud capability profile.]