## Overview
The Integration & Sync Engine manages reliable, secure data synchronization between the modern Azure-hosted cloud platform and the legacy on-premise mainframe. It ensures zero data loss and prevents duplicate processing during the gradual 3-year migration of insurance claim types.

## Key Elements
- **Message Broker Interface**: Azure Service Bus Premium handling pub/sub, partitioning, and dead-lettering.
- **Idempotency & Reconciliation Worker**: Spring Boot microservice enforcing deduplication and business-level reconciliation.
- **Azure SQL Database**: Persistent store for transaction hashes and state tracking.
- **Azure Key Vault**: Secure storage for tokenized PII and sensitive claim field values.
- **Business-Facing DLQ Dashboard & Metrics**: Operational visibility tools for tracking failed syncs and migration progress.

## Relationships
- Claims Core Service -> Message Broker Interface: Publishes domain events [AMQP over TLS]
- Message Broker Interface -> Anti-Corruption Layer (ACL): Relays sync messages to mainframe [AMQP over ExpressRoute/mTLS]
- Idempotency & Reconciliation Worker <-> Azure SQL Database: Enforces deduplication [JDBC/TLS]
- Claims Core Service -> Azure Key Vault: Tokenizes and retrieves high-risk PII [HTTPS/REST]

## Technology Stack
- **Azure Service Bus Premium**: Selected over Kafka to reduce operational complexity for a team with limited cloud experience while supporting pub/sub and queues natively.
- **Spring Boot (Java)**: Used for the reconciliation worker to maintain consistency with the core claims service stack.
- **Azure Managed Identities**: Enforces zero-standing-privilege access and RBAC authorization instead of connection strings.
- **AES-256 / Payload Tokenization**: Secures PII across the hybrid cloud boundary.

## Rationale
Consolidating on Azure Service Bus Premium and Azure Managed Identities minimizes operational overhead and security exposure for a cloud-beginner team. This architecture satisfies stringent zero-loss (R-04) and maintainability requirements while bridging modern cloud components with the legacy mainframe.