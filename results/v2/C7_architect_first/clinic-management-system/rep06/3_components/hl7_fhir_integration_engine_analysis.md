## Overview
The Clinic Management System is a hybrid cloud platform designed to securely manage patient admissions, EMRs, scheduling, and billing for clinics. It leverages an HL7 FHIR Integration Engine to ensure interoperability with external lab and imaging systems while maintaining HIPAA and GDPR compliance.

## Key Elements
- **FHIR API Gateway / Router**: Apache Camel (REST DSL) managing TLS termination, OAuth2/JWT validation, and mTLS.
- **Transformation & Mapping Engine**: Apache Camel (DataFormats) translating internal domain models to FHIR R4 JSON.
- **Validation & Compliance Service**: Stateless HAPI FHIR Validator ensuring profile conformance and stripping PII.
- **Outbound Dispatcher**: Apache Camel (HTTP4/Netty) with RabbitMQ DLQ and resilience4j circuit breakers.
- **External Systems**: External Labs & Imaging Systems, Insurance Clearinghouse, WORM Audit Store.

## Relationships
- *FHIR API Gateway* -> *Validation Service*: In-process Java API with OpenTelemetry correlation ID headers.
- *Validation Service* -> *Transformation Engine*: In-process Java API.
- *Transformation Engine* -> *Core Business Services*: Reads/writes clinical data via gRPC / Internal REST.
- *Transformation Engine* -> *Outbound Dispatcher* [AMQP / RabbitMQ]: Forwards lab/imaging payloads with AES-256 encryption at rest.
- *Outbound Dispatcher* -> *External Labs & Imaging Systems* [HTTPS/REST via mTLS]: Pushes diagnostics with DLQ fallback.

## Technology Stack
- **Apache Camel**: Powers routing, transformations, and dispatching for high-throughput messaging.
- **RabbitMQ**: Manages asynchronous queueing, retries, and Dead-Letter Queues (DLQ).
- **HAPI FHIR Validator**: Provides stateless validation against cached international profiles.
- **CockroachDB & Redis**: Distributed SQL storage and in-memory caching.
- **OpenTelemetry & Prometheus**: Enables distributed tracing, correlation ID tracking, and metrics monitoring.

## Rationale
This decoupled, stateless component architecture allows horizontal auto-scaling across hybrid Kubernetes clusters to guarantee 99.99% availability. Strict mTLS, OAuth2/JWT, and AES-256 encryption mechanisms satisfy rigorous HIPAA and GDPR security mandates.