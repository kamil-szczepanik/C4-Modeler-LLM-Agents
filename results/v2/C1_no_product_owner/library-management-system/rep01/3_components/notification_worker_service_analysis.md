## Overview
The Notification Worker Service is a background container within the Library Management System responsible for processing and dispatching asynchronous alerts to library patrons and staff. It ensures strict EU data residency compliance while maintaining robust fault tolerance and security.

## Key Elements
- Kafka Consumer Component (Go, segmentio/kafka-go)
- Template Engine Component (Go, text/template)
- Dispatch Adapter Component (Go, net/http)
- Retry & DLQ Manager Component (Go)
- Apache Kafka / AWS MSK
- External Notification Service
- AWS Secrets Manager

## Relationships
- Kafka Consumer Component -> Apache Kafka (AWS MSK): Consumes alert events via Avro/JSON over TLS (mTLS + SCRAM-SHA-512)
- Kafka Consumer Component -> Template Engine Component: Passes raw events in-memory
- Template Engine Component -> Dispatch Adapter Component: Passes rendered payloads in-memory
- Dispatch Adapter Component -> External Notification Service: Dispatches outbound HTTPS notifications via egress proxy
- Retry & DLQ Manager Component -> Apache Kafka (AWS MSK): Publishes PII-scrubbed poison-pill events to DLQ topic over TLS

## Technology Stack
- Go: Chosen for high concurrency and performance in background processing
- Apache Kafka (AWS MSK): Used for reliable asynchronous event streaming
- OpenTelemetry: Selected for distributed tracing and Prometheus metrics export
- Kubernetes (HPA, NetworkPolicy): Utilized for horizontal scaling and strict network segmentation

## Rationale
This architecture uses decoupled components to isolate retry logic, PII sanitization, and message rendering, ensuring high testability and error handling. Strict egress filtering, container hardening, and mTLS guarantee adherence to EU data residency and enterprise security requirements.