## Overview
The EMR & Scheduling Service manages patient admissions, electronic medical records, and appointment scheduling within the Clinic Management System. It provides secure, high-availability clinical workflows for healthcare professionals across hybrid cloud environments.

## Key Elements
- **API Gateway / Reverse Proxy**: NGINX / Envoy
- **EMR & Scheduling Service**: Node.js / NestJS container
- **Security & RBAC Middleware**: JWT/OAuth2 enforcement layer
- **Patient Admission Component**: NestJS demographic management module
- **Scheduling Engine Component**: Redis-backed appointment and clash-check module
- **EMR Core Component**: CQRS-pattern clinical records module
- **Notification Event Publisher**: Kafka event dispatch module
- **Outbox Pattern Handler**: Transactional messaging component
- **Data Tier**: PostgreSQL with read-replicas and WORM Object Storage
- **Message Broker**: Apache Kafka

## Relationships
- **API Gateway** -> **Security & RBAC Middleware**: Routes requests [gRPC / REST over TLS 1.3]
- **Security & RBAC Middleware** -> **Scheduling Engine / EMR Core**: Invokes internal methods [In-Memory]
- **EMR Core** -> **PostgreSQL**: Queries and persists records [SQL/TypeORM over TLS 1.3]
- **Scheduling Engine** -> **Apache Kafka**: Emits appointment mutation events [Kafka/Async]
- **Notification Event Publisher** -> **Integration Service**: Dispatches notification payloads [gRPC]

## Technology Stack
- **Node.js / NestJS**: Modular backend framework selected for fast execution and maintainable domain logic.
- **Redis**: In-memory data store for sub-second resource clash checks.
- **PostgreSQL**: Relational database utilizing TypeORM, read-replicas, and the Outbox Pattern for transactional integrity and audit trails.
- **Apache Kafka**: Event broker ensuring reliable asynchronous messaging and notification publishing.
- **OpenTelemetry & Prometheus/Grafana**: Observability stack for distributed tracing and consumer lag monitoring.

## Rationale
This component architecture uses modular NestJS boundaries, CQRS patterns, and Redis caching to achieve sub-second EMR screen loads and rapid scheduling checks. The Outbox Pattern and Kafka integration ensure high availability (99.99%) and strict HIPAA/GDPR compliance without dual-write risks.