## Overview
The Clinic Management System is a hybrid-cloud healthcare platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing while ensuring HIPAA/GDPR compliance and 99.99% availability. It securely integrates internal domain services with external clinical systems via robust asynchronous processing pipelines.

## Key Elements
- **Integration Service Container:** Asynchronous worker processing HL7 FHIR traffic and external system interactions.
- **Event Bus / Message Broker Container:** Apache Kafka or RabbitMQ managing asynchronous message distribution.
- **External Lab & Imaging Systems:** Third-party, HL7 FHIR-compliant medical endpoints.
- **Observability & Configuration Container:** Prometheus, Fluentbit, and Secret Manager managing telemetry and hot-reloadable configs.
- **Kubernetes Ingress / Custom Proxy:** API Gateway handling ingress traffic.

## Relationships
- **Integration Service Container -> HL7 FHIR-Compliant Lab/Imaging Systems:** Exchanges lab and imaging data using [HL7 FHIR REST/JSON over mutual TLS (mTLS)].
- **Integration Service Container <-> Event Bus / Message Broker Container:** Consumes asynchronous events and publishes integration state updates via [AMQP/TCP or Kafka Protocol].

## Technology Stack
- **Kubernetes (on-prem-k8s, eu-central-1):** Hybrid-cloud container orchestration ensuring high availability and strict cgroups resource quotas.
- **Streaming JSON Parsers:** Memory-efficient payload parsing to prevent Out-Of-Memory crashes on large imaging files.
- **Circuit Breaker & Dead-Letter Queue (DLQ):** Error handling pattern with PII/PHI sanitization for resilient external communication.
- **Transactional Outbox Pattern:** Ensures atomic state changes and message dispatches to prevent split-brain issues.

## Rationale
This architecture uses asynchronous patterns, circuit breakers, and transactional outboxes to isolate external system failures and guarantee 99.99% uptime. Additionally, mTLS, streaming parsers, and sanitized DLQs satisfy strict HIPAA/GDPR compliance and performance requirements.