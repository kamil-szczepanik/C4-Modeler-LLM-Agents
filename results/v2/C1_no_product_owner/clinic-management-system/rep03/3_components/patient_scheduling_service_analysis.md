## Overview
The Patient & Scheduling Service manages patient registrations and appointment scheduling within a hybrid cloud clinical IT architecture. It ensures high availability, strict security compliance, and robust interoperability for medium-sized healthcare facilities.

## Key Elements
- **Patient Registry Component**: Fastify/TypeScript plugin managing demographic capture and Zod input validation.
- **Scheduling Engine Component**: Fastify/TypeScript plugin handling temporal/spatial resource clash checks with in-memory indexing.
- **Secrets & Encryption Component**: Fastify plugin integrating HashiCorp Vault for field-level PHI encryption and automated key rotation.
- **Event Dispatcher Component**: Dedicated wrapper isolating RabbitMQ AMQP messaging from domain logic.
- **Audit & Compliance Interceptor**: Fastify middleware writing cryptographically hashed, immutable audit logs to a WORM sink.

## Relationships
- **API Gateway -> Patient & Scheduling Service**: Routes internal API requests via gRPC over mTLS using SPIFFE/SPIRE.
- **Patient Registry & Scheduling Engine -> CockroachDB**: Reads and writes state via PostgreSQL wire protocol over TLS 1.3.
- **Event Dispatcher -> RabbitMQ**: Publishes envelope-encrypted appointment events using AMQP 0-9-1.
- **Secrets & Encryption -> HashiCorp Vault**: Fetches encryption keys and secrets over HTTPS/TLS 1.3.

## Technology Stack
- **Node.js / TypeScript (Fastify)**: Chosen for high-performance, asynchronous REST/gRPC service execution.
- **Prisma ORM**: Provides type-safe database access for the PostgreSQL-compatible CockroachDB backend.
- **CockroachDB**: Ensures distributed, highly available (99.99%) SQL data persistence across hybrid clusters.
- **RabbitMQ**: Asynchronous message broker for decoupled event-driven workflows.
- **HashiCorp Vault**: Secures PHI via field-level encryption and manages credential lifecycle.
- **OpenTelemetry & ArgoCD**: Enables distributed tracing across boundaries and hybrid GitOps deployments.

## Rationale
This architecture combines resilient distributed data storage with strict container isolation to meet HIPAA/GDPR constraints and 99.99% uptime requirements. Component-level separation of encryption, auditing, and scheduling ensures sub-second performance while maintaining uncompromising data security.