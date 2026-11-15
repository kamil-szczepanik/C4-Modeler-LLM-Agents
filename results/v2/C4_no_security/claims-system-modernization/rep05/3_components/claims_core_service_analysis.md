## Overview
The system is a hybrid cloud insurance claims modernization platform that gradually replaces a legacy COBOL/DB2 mainframe. Its core purpose is to enable incremental claim migration while ensuring zero data loss and business continuity.

## Key Elements
- **Claims Core Service**: .NET 8 / C# container running on Azure Kubernetes Service (AKS).
- **Routing & Orchestration Component**: Evaluates dynamic flags to route requests.
- **Claim Domain Model Component**: Implements core business logic for migrated claim types via DDD.
- **ACL Component**: Anti-Corruption Layer translating modern commands to legacy formats.
- **Outbox Processor Component**: Ensures transactional consistency for event publishing.
- **Claim Status & Audit Projection Component**: Aggregates state changes into read-optimized models using CQRS.
- **Integration & Sync Engine**: Azure Service Bus managing asynchronous events.
- **Modern Claims Database**: Azure SQL Database persisting state and projections.

## Relationships
- **API Gateway -> Claims Core Service**: Routes HTTP/REST requests [Internal REST/gRPC]
- **Claims Core Service -> Modern Claims Database**: Persists write and read models [SQL protocol]
- **Claims Core Service -> Integration & Sync Engine**: Publishes asynchronous domain events [AMQP / Azure Service Bus SDK]
- **Claims Core Service -> Legacy Mainframe**: Fallback communication via Anti-Corruption Layer [Legacy Protocol]

## Technology Stack
- **.NET 8 / C#**: Primary application framework chosen for team familiarity and performance.
- **Azure Kubernetes Service (AKS)**: Container orchestration platform for cloud scalability.
- **Entity Framework Core**: ORM for data persistence and projections.
- **Azure App Configuration**: Low-latency feature flagging for claim routing.
- **Azure Service Bus**: Message broker for asynchronous, reliable event-driven messaging.

## Rationale
This architecture decouples the modern platform from legacy constraints using an Anti-Corruption Layer and Outbox pattern, ensuring robust transactional consistency and fast UI performance. The internal CQRS decomposition and feature-flagged routing enable safe, incremental claim migration with rapid one-day rollback capabilities.