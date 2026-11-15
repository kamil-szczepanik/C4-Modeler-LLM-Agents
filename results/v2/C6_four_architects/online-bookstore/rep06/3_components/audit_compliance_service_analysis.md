## Overview
[The system is an Audit & Compliance Service container for an online bookstore, designed to enforce strict GDPR and CCPA regulations. Its core purpose is to handle data retention, immutable audit logging, and data subject access requests.]

## Key Elements
- Audit Event Consumer
- Compliance Policy Engine
- Audit Log Repository Interface
- Compliance API Controller
- Data Export Generator
- Retention Policy Scheduler
- Compliance Health & Metrics Monitor

## Relationships
- Audit Event Consumer reads from Amazon SQS [AMQP/SQS]
- Compliance Policy Engine triggers Amazon EventBridge for GDPR cascades [Async Events / JSON over EventBridge]
- Audit Log Repository Interface persists to Amazon Aurora PostgreSQL [TLS/TCP]
- Compliance API Controller receives requests from AWS API Gateway [HTTPS/REST]
- Data Export Generator writes to Amazon S3 [HTTPS/S3 API]
- Retention Policy Scheduler triggers Compliance Policy Engine [In-Process]
- Components emit metrics to Compliance Health & Metrics Monitor [In-Process / OpenTelemetry]

## Technology Stack
- Node.js / TypeScript: Core language for service components
- Amazon Aurora PostgreSQL: Secure WORM/RLS append-only data storage
- Amazon S3: Temporary storage for encrypted DSAR export bundles
- Amazon EventBridge & SQS: Decoupled asynchronous event ingestion and distribution
- OpenTelemetry / Prometheus: Metrics and observability instrumentation

## Rationale
[This architecture uses decoupled asynchronous event-driven patterns to ensure fault isolation during large-scale GDPR purge operations. PostgreSQL WORM semantics and strict data segregation guarantee the immutability required for regulatory compliance.]