## Overview
The Circulation Service is a core container of the Library Management System responsible for managing loans, renewals, and fines. It ensures deterministic transaction processing and real-time event synchronization while strictly enforcing regional data residency.

## Key Elements
- **Circulation API Resource**: Quarkus RESTEasy / gRPC Endpoint
- **Loan Management Component**: Quarkus CDI Bean
- **Fine & Fee Component**: Quarkus CDI Bean
- **Circulation Event Publisher**: SmallRye Reactive Messaging
- **Circulation Repository Layer**: Hibernate/Panache
- **External Dependencies**: Core API Gateway, RabbitMQ, PostgreSQL (regional), Centralized Observability Platform

## Relationships
- Core API Gateway -> Circulation API Resource [gRPC]
- Circulation API Resource -> Loan Management & Fine & Fee [In-process Method Invocation]
- Loan Management & Fine & Fee -> Circulation Repository Layer [JDBC over TLS]
- Loan Management & Fine & Fee -> Circulation Event Publisher [SmallRye Reactive Messaging]
- Circulation Event Publisher -> RabbitMQ [AMQP over TLS]
- Circulation Service -> Centralized Observability Platform [gRPC]

## Technology Stack
- **Quarkus**: Chosen for fast startup and low memory footprint in containerized deployments
- **PostgreSQL**: Selected for transactional reliability with strict EU-only data residency and encryption-at-rest
- **RabbitMQ**: Used with durable queues and AMQP over TLS for real-time, event-driven patron updates
- **SmallRye Fault Tolerance**: Implements circuit breakers for database and downstream resilience
- **OpenTelemetry**: Provides distributed tracing across API Gateway, components, and messaging

## Rationale
This architecture guarantees low latency and high availability to meet strict performance and staff efficiency goals during peak hours. Furthermore, isolated components and strict regional database constraints ensure absolute GDPR compliance for EU patron data.