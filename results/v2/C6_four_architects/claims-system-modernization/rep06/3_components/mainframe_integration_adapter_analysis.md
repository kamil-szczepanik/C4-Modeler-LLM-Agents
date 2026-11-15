## Overview
The system is a hybrid cloud insurance claims modernization platform that gradually replaces a legacy COBOL/DB2 mainframe while maintaining continuous claims processing. It provides online claims submission and adjuster management while ensuring zero data loss and rapid legacy fallback capabilities.

## Key Elements
- Azure API Management (Azure API Management)
- Mainframe Integration Adapter (.NET 8, Azure Container Apps)
- Adapter API Controller (.NET 8 component)
- Mainframe Message Translator with Versioning & Feature Flags (.NET 8 component)
- Outbox Pattern Processor (.NET 8 + Entity Framework Core component)
- Circuit Breaker & Fallback Manager (.NET 8 + Polly component)
- IBM MQ / CICS Client (.NET 8 component)
- On-Premises COBOL/DB2 Mainframe
- Azure Service Bus (Azure Service Bus)

## Relationships
- Azure API Management -> Adapter API Controller: Forward integration requests [HTTP/2]
- Adapter API Controller -> Mainframe Message Translator: Transform payloads [In-Memory]
- Mainframe Message Translator -> Outbox Pattern Processor: Persist transaction state [In-Memory]
- Outbox Pattern Processor -> IBM MQ / CICS Client: Queue dispatch [In-Memory]
- IBM MQ / CICS Client -> Circuit Breaker Manager: Execute legacy calls [TCP/IP via Azure Hybrid Connections]
- Circuit Breaker Manager -> Azure Service Bus: Publish fallback events [AMQP]

## Technology Stack
- .NET 8 on Azure Container Apps: Powers the integration container with modern, maintainable code suited for the team's skillset.
- Entity Framework Core: Manages reliable outbox pattern state persistence to guarantee zero data loss (R-04).
- Polly: Implements circuit breaking and fallback management to handle high mainframe latency (up to 5s).
- IBM MQ / CICS Client via Azure Hybrid Connections: Secures persistent TCP/IP socket communication to the on-premise mainframe.
- Azure Service Bus: Decouples asynchronous messaging and fallback events across the hybrid architecture.

## Rationale
This architecture isolates fragile and expensive-to-change mainframe logic behind a robust, fault-tolerant .NET 8 integration adapter. It satisfies strict hybrid constraints, ensuring transactional consistency and 1-day rollbacks while bridging on-premise systems with Azure.