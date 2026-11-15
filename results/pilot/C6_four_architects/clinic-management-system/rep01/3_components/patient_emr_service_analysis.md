## Overview
The Patient & EMR Service is a core microservice within the Clinic Management System responsible for managing patient admissions and electronic medical records. It ensures secure, high-availability, and interoperable clinical data workflows for medium-sized hospitals and clinics.

## Key Elements
* Patient & EMR Service Container (Node.js runtime, Docker, Kubernetes)
* Internal Components: EMR Management Engine, Patient Demographics Controller, Validation & Sanitization Middleware, Audit Logging Component, Crypto Interceptor Component, Caching & Distributed Locking Component, HL7 FHIR Transformation Component, Search Index Sync Component, FHIR Resource Validation Component, Tenant Context Manager Component, DLQ Handler Component, Offline Sync & Conflict Resolution Component, Access Policy Enforcer Component, Bulk Export & Retention Component, CDS Hook Engine, Consent Management Component, Diagnostic Telemetry Interceptor Component
* External Systems: PostgreSQL Container cluster, Redis Container tier, Apache Kafka StatefulSet, RabbitMQ Container cluster, Elasticsearch Containers, MinIO Object Storage Gateway Container, HL7 FHIR Adapter Container, Tenant Context & Authorization Proxy Container, Data Encryption & Key Management Container, Audit & Compliance Sidecar Container, Observability Collector Container

## Relationships
* API Gateway Container -> Patient & EMR Service: Dispatches routing and authenticates requests via OAuth2/OIDC, gRPC
* Patient & EMR Service -> PostgreSQL Container cluster: Executes transactional queries and search via SQL over TLS
* Patient & EMR Service -> Redis Container tier: Executes caching and distributed locking via ioredis / gRPC
* Patient & EMR Service -> Elasticsearch Containers: Executes read model queries via gRPC
* Patient & EMR Service -> Apache Kafka StatefulSet: Publishes and consumes domain events via KafkaJS (Protocol Buffers)
* Patient & EMR Service -> RabbitMQ Container cluster: Publishes transient events and CDS pipelines via AMQP
* Patient & EMR Service -> HL7 FHIR Adapter Container: Exchanges clinical payloads via internal gRPC channels
* Patient & EMR Service -> MinIO Object Storage Gateway Container: Streams historical archives via chunked multipart uploads over HTTPS
* Patient & EMR Service -> Audit & Compliance Sidecar Container: Dispatches immutable audit logs via Unix domain sockets
* Patient & EMR Service -> Observability Collector Container: Exports metrics and traces via OpenTelemetry SDK

## Technology Stack
* Node.js / TypeScript: Core runtime environment for microservice execution
* Fastify: High-throughput request routing and demographic controllers
* TypeORM: Object-relational mapping for PostgreSQL interactions
* ioredis: Client library for Redis caching and distributed locks
* KafkaJS & Protocol Buffers: Asynchronous binary event serialization and streaming
* ajv: Fast schema enforcement for clinical payloads
* OpenTelemetry SDK: Diagnostic telemetry and distributed tracing instrumentation

## Rationale
This architecture ensures strict HIPAA and GDPR compliance through field-level AES-256 encryption, immutable audit logging, and explicit consent management. Active-active high availability (99.99%) and sub-second P95 performance are achieved via distributed caching, optimized PostgreSQL querying, and asynchronous CDC-driven Elasticsearch read models.