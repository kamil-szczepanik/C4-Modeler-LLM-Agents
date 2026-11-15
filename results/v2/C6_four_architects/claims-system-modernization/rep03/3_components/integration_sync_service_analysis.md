## Overview
The system modernizes a 30-year-old regional insurer mainframe claims platform by gradually migrating claim types to an Azure cloud architecture. It maintains hybrid operations while ensuring zero data loss, strict compliance with legacy batch windows, and fast rollbacks.

## Key Elements
- Message Consumer (Spring Cloud Stream)
- Idempotency & Deduplication Filter (Spring Boot Filter)
- Sync Orchestrator (Spring Boot / Saga Pattern)
- Mainframe Adapter (Camel / Spring Boot)
- Feature Flag & Routing Switcher (Spring Cloud Config)
- Batch Rate Limiter (Resilience4j)
- Audit & Reconciliation Ledger (Spring Batch / JPA)
- Event Relay (Azure Service Bus SDK)

## Relationships
- External Azure Service Bus -> Message Consumer: Delivers asynchronous domain events [AMQP]
- Message Consumer -> Idempotency Filter: Passes raw deserialized events [In-memory]
- Idempotency Filter -> Sync Orchestrator: Forwards verified messages [In-memory]
- Sync Orchestrator -> Mainframe Adapter: Dispatches outbound requests via Batch Rate Limiter [In-memory]
- Feature Flag & Routing Switcher -> Mainframe Adapter: Routes fallback payloads during rollback [gRPC/Direct]
- Audit & Reconciliation Ledger -> Mainframe Adapter: Fetches legacy state snapshots [AMQP/MQ]
- Audit & Reconciliation Ledger -> Observability & Audit Container: Exports audit logs [OpenTelemetry/HTTPS]

## Technology Stack
- Java / Spring Boot: Standardizes the entire service to minimize polyglot overhead for a team with low cloud experience
- Apache Camel: Implements battle-tested enterprise integration patterns for legacy IBM MQ and SFTP protocols
- Resilience4j: Throttles outbound traffic to protect the rigid mainframe batch window (23:00-05:00)
- Spring Batch & JPA: Enables automated state reconciliation and drift detection between modern and legacy databases
- Azure Service Bus: Provides scalable, reliable asynchronous pub/sub messaging

## Rationale
The Java/Spring Boot component architecture bridges modern cloud technology with rigid legacy mainframe constraints by utilizing battle-tested integration patterns. It mitigates the team's low cloud experience while fully guaranteeing consistency, fast rollbacks, and batch window protection.