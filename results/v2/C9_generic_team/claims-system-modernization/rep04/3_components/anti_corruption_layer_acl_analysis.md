## Overview
The system is an Anti-Corruption Layer (ACL) container running on Azure Container Apps that securely bridges a modern cloud platform with an on-premises COBOL/DB2 mainframe. Its core purpose is to facilitate the gradual, incremental migration of insurance claim types while protecting the legacy system from traffic spikes and ensuring data consistency.

## Key Elements
* Anti-Corruption Layer (ACL): Core component containerized in Azure Container Apps.
* Transactional Outbox & De-duplication Engine: Internal modules managing reliable messaging and idempotency via Redis.
* Data Transformation & Mapping Layer: Module translating legacy COBOL copybooks into modern domain events.
* Resilience & Routing Manager: Implements Circuit Breakers, Feature Flags, and declarative routing rules.
* Monitoring & Diagnostics: Distributed tracing, health check probes, and Dead Letter Queue (DLQ) handlers.

## Relationships
* Anti-Corruption Layer (ACL) -> On-Premises COBOL/DB2 Mainframe: Integrates via legacy protocols over secure VPN/ExpressRoute [HTTPS/TCP]
* Anti-Corruption Layer (ACL) -> Azure Service Bus: Publishes and consumes asynchronous domain events [AMQP]
* Anti-Corruption Layer (ACL) -> Azure Cosmos DB / Redis: Stores idempotency keys, cached responses, and outbox state [Redis Protocol / HTTPS]
* Anti-Corruption Layer (ACL) -> Azure Key Vault: Retrieves secrets, connection strings, and certificates securely [HTTPS]

## Technology Stack
* Azure Container Apps: Hosts the ACL container with declarative routing and health probes for operational simplicity.
* Redis: Provides fast in-memory storage for idempotency keys and de-duplication tracking.
* Azure Service Bus: Handles reliable asynchronous messaging and Dead Letter Queue (DLQ) management.
* Azure Key Vault: Centralizes management of secrets and hybrid connection strings.
* Pact & Automated Contract Testing: Enforces strict payload validation to prevent breaking legacy mainframe interfaces.

## Rationale
This architecture decouples the modern Azure platform from unstable mainframe response times using caching, outbox patterns, and circuit breakers. It strictly enforces data consistency and low-effort rollbacks while accommodating a team with limited cloud experience.