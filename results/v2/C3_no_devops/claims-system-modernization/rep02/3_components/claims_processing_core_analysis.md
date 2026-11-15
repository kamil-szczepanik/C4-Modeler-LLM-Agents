## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe claims platform with a modern hybrid cloud architecture. It ensures seamless online claims processing while maintaining business continuity during a three-year migration window.

## Key Elements
- **Claim Ingestion & Validation Component**: Spring Boot container handling payload validation against domain schemas.
- **Workflow Orchestrator**: Manages multi-step claim lifecycles and idempotent processing.
- **Claim State Service**: Spring Data JPA service managing domain aggregates and exposing transaction state markers.
- **Legacy Adapter Component**: Apache Camel and Spring Integration component for translating domain models and synchronizing with the Enterprise Service Bus.

## Relationships
- **Claim Ingestion & Validation Component** -> **Workflow Orchestrator**: Triggers process initiation [gRPC with mTLS]
- **Workflow Orchestrator** -> **Claim State Service**: Persists and queries domain aggregates [JPA / JDBC]
- **Claim State Service** -> **Audit & Reconciliation Ledger**: Emits immutable state transition events [Database Write / Transaction Log]
- **Workflow Orchestrator** -> **Legacy Adapter Component**: Dispatches asynchronous synchronization payloads [Azure Service Bus via AMQP with digital signatures]

## Technology Stack
- **Java / Spring Boot**: Chosen for enterprise maturity to mitigate the team's limited cloud experience.
- **gRPC**: Provides low-latency internal component communication.
- **Azure Container Apps**: Hosts modern microservices within an internal Virtual Network (VNet).
- **Azure Service Bus & Apache Camel**: Manages decoupled asynchronous legacy bridging.
- **Azure Key Vault & Managed Identities**: Secures secrets and eliminates hardcoded credentials.

## Rationale
This architecture balances aggressive performance and security requirements—such as sub-500ms internal responses and zero-trust VNet isolation—while safely bridging modern cloud components with the legacy mainframe. The modular Spring Boot design guarantees zero data loss and supports rapid one-day rollbacks per claim type.