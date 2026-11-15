## Overview
[The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern Azure-hosted platform while maintaining hybrid coexistence.]

## Key Elements
- Integration & Anti-Corruption Layer (Azure Service Bus)
- Message Router Component (.NET Core / Azure Service Bus Topics)
- Translation & Mapping Component (.NET Core)
- Crypto-Proxy Middleware (.NET Core)
- Dead Letter & Audit Store Component (Azure Cosmos DB)
- Replay & Reconciliation Component (.NET Core / Azure Functions)
- Mainframe Adapter (Azure Container Apps / .NET Core)

## Relationships
- Claims Domain Services -> Message Router: Publishes domain events [AMQP (Azure Service Bus)]
- Message Router -> Translation & Mapping: Transforms payloads [In-memory / .NET]
- Translation & Mapping -> Crypto-Proxy Middleware: Encrypts/decrypts sensitive payloads [In-memory / .NET]
- Translation & Mapping -> Mainframe Adapter: Dispatches legacy messages [AMQP]
- Replay & Reconciliation -> Message Router: Re-queues corrected messages [AMQP]

## Technology Stack
- Azure Service Bus: Handles asynchronous messaging and transactional outbox pattern to ensure zero data loss.
- Azure Cosmos DB: Provides immutable storage and customer-managed encryption keys for auditability and dead-letter management.
- .NET Core / Azure Functions: Powers routing, mapping, cryptographic proxying, and replay components.
- Azure Key Vault Managed HSMs: Secures cryptographic keys with automated rotation.

## Rationale
[This architecture ensures zero data loss and supports seamless one-day claim type rollbacks during the 3-year hybrid migration. It isolates legacy schemas while enforcing strict security and compliance controls.]