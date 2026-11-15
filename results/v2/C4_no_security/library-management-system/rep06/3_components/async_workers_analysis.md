## Overview
The Library Management System provides catalogue management, circulation, and self-service portals for public and academic libraries. The system ensures EU-only data residency and meets strict performance and compliance requirements.

## Key Elements
- **Users**: Library Patrons, Library Staff and Circulation Clerks, Library Administrators
- **External Systems**: Payment Gateway, Third-Party Identity Provider/LDAP, Third-Party Digital Content Providers, Notification Service, Centralized Log/Audit Aggregator, APM and Synthetic Monitoring Tool
- **Containers**: API Gateway (Kong / NGINX), Self-Service Portal & Staff Dashboard (React / TypeScript), Core API Application (Spring Boot / Java), Search Engine (OpenSearch), Primary Database (Managed PostgreSQL), Message Broker (Kafka / RabbitMQ), Async Workers (Spring Boot / Java)
- **Async Workers Components**: Event Consumer Engine, Notification Dispatcher Component, Index Synchronizer Component, Fine & Payment Processor Component

## Relationships
- Event Consumer Engine -> Message Broker: Consumes asynchronous events [Kafka Protocol / AMQP]
- Index Synchronizer Component -> Search Engine: Updates index data [HTTPS/REST]
- Notification Dispatcher Component -> Notification Service: Dispatches alerts [HTTPS/REST]
- Fine & Payment Processor Component -> Primary Database: Persists financial updates [JDBC/TCP]
- Fine & Payment Processor Component -> Centralized Log/Audit Aggregator: Emits immutable audit logs [Syslog/HTTPS]

## Technology Stack
- **Spring Boot / Java**: Core application and async worker runtime providing robust enterprise integration.
- **Kafka / RabbitMQ**: Message broker for asynchronous event distribution and queue management.
- **OpenSearch**: Search engine for sub-800ms catalogue queries and fast indexing.
- **Managed PostgreSQL**: Primary relational database ensuring persistent transactional storage.
- **KEDA**: Kubernetes Event-driven Autoscaling for dynamic worker scaling based on Kafka lag.
- **Resilience4j**: Circuit breakers for graceful degradation on external outbound calls.

## Rationale
This architecture uses event-driven asynchronous processing to maintain search freshness and notification SLAs without degrading user-facing workflows. Strict operational guards, autoscaling, and data isolation satisfy EU residency and financial compliance mandates.