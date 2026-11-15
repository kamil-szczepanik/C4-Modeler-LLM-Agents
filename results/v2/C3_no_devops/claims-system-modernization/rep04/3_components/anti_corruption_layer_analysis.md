## Overview
[The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure-based platform. It ensures seamless hybrid operations, zero data loss, and incremental claim type migration over a three-year period.]

## Key Elements
[• Anti-Corruption Layer (ACL): Azure Functions & Azure Service Bus container insulating modern services from legacy structures.
• Translation Component: Azure Function mapping domain models to legacy COBOL schemas using Mapster/AutoMapper.
• Buffering & Routing Component: Azure Service Bus Topics/Queues managing asynchronous ingestion.
• Audit & Reconciliation Component: Cosmos DB and Azure Function capturing immutable payloads.
• Reconciliation & Alerting Component: Timer-triggered Azure Function executing discrepancy checks.]

## Relationships
[• Claims Processing Engine -> Translation Component: Publishes and consumes events via [Azure Service Bus, AMQP].
• Translation Component -> Legacy Mainframe: Synchronizes data via [HTTPS/SOAP, SFTP, and mTLS].
• Translation Component -> Audit & Reconciliation Component: Writes execution logs via [Internal .NET SDK / Cosmos DB API].
• Reconciliation & Alerting Component -> Azure Monitor: Emits operational alerts via [HTTPS / Azure Monitor API].]

## Technology Stack
[• Azure Functions (.NET 8 Isolated Worker Model): Chosen for serverless, event-driven scalability.
• Azure Service Bus: Selected for reliable asynchronous messaging and buffering.
• Cosmos DB: Utilized for immutable, high-performance audit log storage.
• Azure Key Vault & Managed Identities: Implemented for secure credential management and zero-trust authentication.]

## Rationale
[This hybrid architecture mitigates high mainframe modification costs by isolating legacy interfaces within an auditable, secure Anti-Corruption Layer. It guarantees strict consistency and rapid rollback capabilities without disrupting core business operations.]