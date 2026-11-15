## Overview
[The system is a hybrid Insurance Claims Modernization Platform that gradually replaces a legacy COBOL/DB2 mainframe with a modern Azure-based cloud architecture. Its core purpose is to enable online claim submission and modernized claims handling while ensuring continuous business operations during a multi-year migration.]

## Key Elements
* Anti-Corruption Layer (ACL) Container (Azure Container Apps)
* Modular Monolith Container (Azure App Service / Container Apps)
* Asynchronous Messaging & Caching Layer (Azure Service Bus and Redis)
* COBOL/DB2 Mainframe (On-Premises System of Record)
* Azure Key Vault (Configuration and Secrets Management)
* Azure Application Insights (Observability and Structured Logging)

## Relationships
* Modular Monolith Container -> Anti-Corruption Layer (ACL) Container [Internal REST/gRPC]
* Anti-Corruption Layer (ACL) Container -> COBOL/DB2 Mainframe [Secure VPN/TLS]
* Anti-Corruption Layer (ACL) Container <-> Asynchronous Messaging & Caching Layer [Azure Service Bus / Redis]
* Anti-Corruption Layer (ACL) Container -> Azure Key Vault [HTTPS / Managed Identity]

## Technology Stack
* Azure Container Apps: Simplifies deployment and scaling for a team with limited cloud experience.
* Redis & Azure Service Bus: Powers asynchronous write-behind caching and queuing to bridge mainframe latency gaps.
* Adapter, Outbox, & Circuit Breaker Patterns: Protects modern domain models from legacy breaking changes and ensures zero data loss.
* Structured JSON Logging & Correlation IDs: Provides unified tracing across hybrid infrastructure.

## Rationale
[This architecture successfully decouples modern Azure workloads from legacy mainframe latency and instability using asynchronous messaging and robust buffering patterns. It satisfies strict business constraints through isolated data-mapping strategies that enable rapid rollbacks and zero data loss during the 3-year migration.]