## Overview
[The system is a hybrid cloud Insurance Claims Modernization platform that gradually migrates claim types from a 30-year-old COBOL/DB2 mainframe to Azure while maintaining uninterrupted business operations. It ensures zero data loss, sub-2-second UI performance via caching, and rapid one-day fallback capabilities for low cloud experience teams.]

## Key Elements
- Customers and Brokers (External Users)
- Claims Adjusters (Internal Users)
- COBOL/DB2 Mainframe (On-premises System of Record)
- Active Directory (Identity Provider)
- API Gateway / Anti-Corruption Layer (ACL) (Custom microservices on Azure)
- Backend-for-Frontend (BFF) (Azure web applications)
- Caching / State Store (Azure Redis Cache)
- Event Broker (Azure Service Bus)
- Data Synchronization / Reconciliation (Azure Functions / WebJobs)
- Centralized Logging & Monitoring (Azure Monitoring)

## Relationships
- Customers / Brokers -> API Gateway / ACL: Online claim submission [HTTPS / REST]
- Claims Adjusters -> BFF: Manage claims via web application [HTTPS]
- BFF -> Caching / State Store: Low-latency read models & session state [TCP / Redis Protocol]
- API Gateway / ACL -> COBOL/DB2 Mainframe: Batch & synchronous fallback processing [SNA / MQ / DB2 Connect]
- BFF -> API Gateway / ACL: Dynamic claim routing [HTTPS / gRPC]
- Data Synchronization / Reconciliation -> COBOL/DB2 Mainframe & Azure Service Bus: Incremental claim migration and state sync [JDBC / AMQP]

## Technology Stack
- Azure Redis Cache: Caching / State Store layer for ephemeral read models, idempotency keys, and stampede prevention to meet sub-2-second latency targets (R-05).
- Azure Service Bus: Event broker ensuring reliable, asynchronous messaging across the hybrid boundary.
- Azure Functions / WebJobs: Serverless compute for data synchronization, reconciliation, and background processing.
- Azure Key Vault and App Configuration: Centralized secret management and dynamic configuration to reduce operational overhead for an inexperienced cloud team.
- Azure Identity Services: Enterprise Single Sign-On (SSO) integrated with the insurer's Active Directory.

## Rationale
[This hybrid architecture bridges the 30-year-old on-premises mainframe with modern Azure cloud components, satisfying strict constraints regarding batch windows and expensive legacy interfaces. By utilizing an Anti-Corruption Layer, cache-aside read patterns, and explicit fallback mechanisms, the system guarantees zero data loss and rapid one-day rollbacks while minimizing complexity for a team with limited cloud experience.]