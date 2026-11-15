## Overview
The Core Business Service manages circulation, cataloging, and policy enforcement for the Library Management System. It ensures secure, performant operations while maintaining strict EU-only data residency.

## Key Elements
- **Cataloging Component**: Manages physical and digital item inventories using Spring Data JPA.
- **Circulation Component**: Handles lending, returns, and holds logic via JDBC.
- **Event Publisher Component**: Decouples domain events using Spring Events and RabbitMQ.
- **Policy Evaluation Component**: Evaluates variable institutional loan policies and rules.
- **Catalog Indexer Component**: Pushes asynchronous inventory updates to Elasticsearch.

## Relationships
- **API Gateway -> Core Business Service**: Routes business requests via internal REST/gRPC secured with mTLS.
- **Core Business Service -> Database (PostgreSQL)**: Reads and writes data via JDBC with application-level encryption for PII.
- **Core Business Service -> Message Broker (RabbitMQ)**: Publishes asynchronous events via AMQP.
- **Core Business Service -> Search Service (Elasticsearch)**: Updates search indices via AMQP to meet the < 800 ms response requirement (R-05).
- **Core Business Service -> Audit Logging Service**: Emits structured security events synchronously.

## Technology Stack
- **Spring Boot (Java)**: Core framework providing robust dependency injection and enterprise stability.
- **Spring Security**: Enforces method-level RBAC/ABAC to segregate patron and librarian actions.
- **Spring Data JPA**: Simplifies database persistence operations via JDBC.
- **RabbitMQ (AMQP)**: Message broker utilizing transactional outbox patterns for reliable asynchronous messaging.
- **TLS 1.3 / mTLS**: Secures all transport-layer and internal network communications.

## Rationale
This component-based architecture isolates transactional integrity, asynchronous messaging, and policy evaluation within the Core Business Service. It guarantees EU data compliance, high security, and performance.