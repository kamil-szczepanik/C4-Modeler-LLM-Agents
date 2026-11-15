## Overview
The Async Worker Containers manage background workloads, long-running clinical sagas, and batch integrations for the Clinic Management System. It ensures HIPAA/GDPR compliance, secure external interoperability, and high availability across hybrid cloud environments.

## Key Elements
- Task Dispatcher (Python / Celery)
- Workflow Orchestrator (Temporal)
- Integration Dispatcher (Python / httpx)
- Encryption / Sanitization Component (Python `cryptography`)
- Batch Export Formatter (Python / Jinja2 / Marshmallow)
- Audit Logger Component (Python structlog)
- Dead-Letter Queue (DLQ) Handler (Celery DLQ extensions)
- Worker Health & Metrics Exporter (Prometheus Python Client)

## Relationships
- Task Dispatcher consumes messages from Message Broker via AMQP/Kafka.
- Workflow Orchestrator persists state to Data Layer (PostgreSQL) via encrypted SQL/TLS 1.3.
- Integration Dispatcher invokes External Systems securely via HTTPS/mTLS.
- Batch Export Formatter sends payloads to Integration Dispatcher via gRPC/HTTP.
- Audit Logger flushes encrypted records to Data Layer (PostgreSQL) via TLS 1.3.
- Worker Health & Metrics Exporter exposes endpoints scraped by Kubernetes via HTTP/GET.

## Technology Stack
- Python: Primary runtime for all worker components and task processing.
- Temporal: Manages durable, multi-step clinical sagas with built-in audit trails.
- PostgreSQL & Redis: Provides persistent state storage and transient caching via RESP/TLS.
- Prometheus: Collects runtime metrics and container telemetry.

## Rationale
This architecture uses Temporal and Celery for fault-tolerant background processing, guaranteeing 99.99% availability for critical healthcare workloads. Dedicated encryption, sanitization, and audit components ensure strict compliance with HIPAA and GDPR data regulations.