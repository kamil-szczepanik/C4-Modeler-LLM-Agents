## Overview
[A hybrid insurance claims modernization platform that gradually replaces a legacy COBOL/DB2 mainframe with a modern Azure-hosted application using a Strangler Fig pattern. The system ensures seamless integration, zero data loss, and strict adherence to mainframe operational constraints.]

## Key Elements
- Hybrid Bridge Container (On-premise boundary container)
- Sync Router Component (Spring Boot)
- Mainframe Adapter Component (Spring Boot)
- Transaction Ledger Component (Local H2/PostgreSQL store)
- Configuration & Feature Toggle Component (Database-backed registry)
- Batch Co-ordination Component (Spring Boot)
- Schema & EBCDIC Translation Component (Apache Camel)
- Circuit Breaker & Retry Manager Component (Resilience4j)
- External Systems: Azure Relay, IBM DB2/COBOL Mainframe, IBM MQ

## Relationships
- Azure Service Bus / Azure Relay -> Sync Router Component: AMQP
- Sync Router Component -> Feature Toggle Component: In-memory Java API
- Batch Co-ordination Component -> Transaction Ledger Component: Local JPA/SQL
- Mainframe Adapter Component -> Schema & EBCDIC Translation Component: Internal Java Method Calls
- Mainframe Adapter Component -> Circuit Breaker & Retry Manager Component: Internal Java method decoration
- Schema & EBCDIC Translation Component -> Legacy Mainframe: IBM MQ / TCP raw sockets
- Hybrid Bridge -> Legacy Mainframe: IBM MQ and JDBC queries via Azure Relay / VPN Gateway

## Technology Stack
- Java / Spring Boot: Core runtime for all Hybrid Bridge components ensuring rapid implementation given team constraints.
- Apache Camel: Data translation framework for robust bi-ordinated JSON-to-EBCDIC mapping.
- Resilience4j: Fault tolerance library for circuit breaker and retry policies over hybrid networks.
- Azure Service Bus & Azure Relay: Cloud-to-on-premise messaging and secure hybrid connectivity.
- IBM MQ & JDBC: Protocols for legacy mainframe integration and DB2 querying.
- PostgreSQL / H2: Local transactional ledger database ensuring idempotency and zero data loss.

## Rationale
[This architecture successfully isolates the fragile, expensive-to-change on-premise mainframe while meeting stringent zero-data-loss and one-day rollback requirements. It respects the rigid nightly batch window through explicit traffic-shaping components without requiring extensive prior cloud experience.]