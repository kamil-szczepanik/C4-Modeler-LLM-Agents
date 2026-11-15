## Overview
This system modernizes a regional insurer's 30-year-old mainframe claims platform using a hybrid cloud architecture. It gradually migrates claim types to a new Azure-hosted platform while maintaining operational continuity with the legacy system.

## Key Elements
* **Azure App Service (PaaS):** Hosts the Azure Modular Monolith Platform and Anti-Corruption Layer (ACL).
* **Azure SQL Database:** Stores transactional data utilizing a Transactional Outbox Pattern.
* **Azure Redis Cache:** Caches read models to support Command Query Responsibility Segregation (CQRS).
* **Azure Service Bus:** Handles asynchronous messaging between the cloud platform and the legacy mainframe.
* **Azure Key Vault:** Manages secure configuration, secrets, and Active Directory integration parameters.
* **Application Insights:** Provides centralized structured logging and distributed tracing via OpenTelemetry.
* **COBOL/DB2 On-Premises Mainframe:** Acts as the system of record.

## Relationships
* **Claims Adjusters -> Azure App Service:** Interacts via HTTPS for claims management and workflows.
* **Azure App Service -> Azure SQL Database:** Reads and writes claim data via Tabular Data Stream.
* **Azure App Service -> Azure Redis Cache:** Caches and retrieves read models via Redis Protocol.
* **Azure App Service -> COBOL/DB2 Mainframe:** Communicates asynchronously via Azure Service Bus and ACL adapters.
* **Azure App Service -> Azure Key Vault:** Retrieves secrets and configurations via HTTPS.
* **Azure App Service -> Application Insights:** Sends telemetry and trace data via HTTPS.

## Technology Stack
* **Azure App Service (Premium V3 Tier):** Chosen to reduce operational overhead for a team with limited cloud experience while guaranteeing dedicated compute performance.
* **Azure SQL Database:** Selected for reliable relational data storage supporting ACID transactions and outbox patterns.
* **Azure Redis Cache:** Implemented to decouple UI reads from mainframe latency, ensuring sub-2-second screen loads.
* **Azure Service Bus:** Utilized for reliable, asynchronous message delivery across the hybrid boundary.
* **OpenTelemetry & Application Insights:** Adopted for comprehensive distributed tracing across hybrid infrastructure components.

## Rationale
This architecture uses a PaaS-based modular monolith to minimize operational complexity for a cloud-novice team while meeting strict hybrid constraints. It ensures data consistency and rapid rollback capabilities via CQRS, transactional outboxes, and an anti-corruption layer.