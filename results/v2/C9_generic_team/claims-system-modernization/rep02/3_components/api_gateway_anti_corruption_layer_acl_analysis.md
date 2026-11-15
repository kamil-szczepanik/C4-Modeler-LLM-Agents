## Overview
[The system modernizes a regional insurer's 30-year-old mainframe by introducing a cloud-based claims platform while preserving the legacy system of record. It uses a hybrid Azure-to-mainframe architecture to ensure zero claim loss and sub-second adjuster responsiveness.]

## Key Elements
* API Gateway / Anti-Corruption Layer (ACL) (Custom microservices on Azure)
* Azure Redis Cache
* Azure Service Bus
* Azure Functions / WebJobs
* Backend-for-Frontend (BFF) Azure web applications
* COBOL/DB2 Mainframe (On-premises system of record)
* Active Directory (IAM / Token Service)

## Relationships
* Customers & Brokers -> API Gateway / Anti-Corruption Layer (ACL): Submit claims online [HTTPS / REST]
* Backend-for-Frontend (BFF) -> API Gateway / Anti-Corruption Layer (ACL): Internal data retrieval and orchestration [HTTPS / gRPC]
* API Gateway / Anti-Corruption Layer (ACL) -> Azure Redis Cache: Read-through/write-behind caching and rate limiting [TCP / Redis Protocol]
* API Gateway / Anti-Corruption Layer (ACL) -> Azure Service Bus: Asynchronous event messaging and queueing [AMQP / HTTPS]
* API Gateway / Anti-Corruption Layer (ACL) -> COBOL/DB2 Mainframe: System of record updates and batch synchronization [Legacy Protocols / Batch]

## Technology Stack
* Azure API Management / Custom Microservices: Chosen as the API Gateway and Anti-Corruption Layer to decouple modern models from rigid mainframe contracts.
* Azure Redis Cache: Selected for read-through/write-behind caching to meet the sub-2s performance SLA despite slow mainframe responses.
* OpenAPI / Swagger & Contract-First Design: Implemented for strict API contracts and decoupled frontend routing.
* Azure Service Bus & Azure Functions: Utilized for asynchronous queueing, dead-letter queues, and background processing to prevent claim loss.
* Configuration-as-Code & Adapter Pattern: Deployed to support rapid 1-day fallback requirements and incremental claim migration.

## Rationale
[This architecture successfully bridges the hybrid gap by isolating legacy mainframe rigidities behind a resilient, cached Anti-Corruption Layer. It strictly enforces data consistency, idempotency, and rapid fallback mechanisms to satisfy all migration constraints despite the team's limited cloud experience.]