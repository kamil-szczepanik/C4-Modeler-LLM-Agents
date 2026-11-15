## Overview
This architecture modernizes a regional insurer's claims platform using a hybrid cloud approach. It gradually replaces the legacy mainframe system while maintaining synchronous data consistency.

## Key Elements
- **Sync Orchestrator Function**: .NET 8 isolated durable functions coordinating claim state synchronization.
- **Mainframe Adapter Component**: .NET 8 component managing protocol translation.
- **Outbox Event Publisher**: .NET 8 component consuming Azure Service Bus topics.
- **Idempotency & Deduplication Filter**: .NET 8 middleware validating message uniqueness against Azure SQL.
- **Integration Gateway**: On-premises gateway interfacing with the legacy mainframe.

## Relationships
- *Sync Orchestrator* -> *Outbox Event Publisher*: Dispatches messages via **Azure Service Bus [AMQP]**.
- *Sync Orchestrator* -> *Idempotency & Deduplication Filter*: Validates message uniqueness via **In-memory / gRPC**.
- *Mainframe Adapter* -> *Integration Gateway*: Sends transactional payloads via **HTTPS [REST/JSON]** using mutual TLS (mTLS).

## Technology Stack
- **Azure Functions (.NET 8)**: Chosen for serverless scalability despite team's low cloud experience.
- **Azure Service Bus [AMQP]**: Chosen for reliable asynchronous messaging and batch window isolation.
- **Azure SQL Database**: Used for idempotency state storage ensuring exactly-once processing.
- **HTTPS [REST/JSON] with mTLS**: Ensures secure and standardized hybrid-cloud transport.

## Rationale
The hybrid architecture enables gradual, risk-mitigated migration of claim types while strictly adhering to legacy mainframe constraints. Robust messaging and deduplication patterns guarantee absolute consistency and prevent data loss during the transition.