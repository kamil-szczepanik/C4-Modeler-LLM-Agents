## Overview
- Event-driven decoupling mechanism for the Library Management System.
- Enables asynchronous processing, reliable notifications, and audit trails while enforcing strict EU data residency and GDPR compliance.

## Key Elements
- **Broker Engine:** Apache Kafka deployed on Kubernetes via Strimzi Operator
- **Schema Registry:** Enforces contract validation using Avro or JSON Schema
- **Topic Partition Manager:** Kafka native partition assignment and replication (min. ISR = 2)
- **Dead Letter Queue (DLQ) Handler:** Captures poisoned messages with encrypted, restricted access
- **Event Stream Compaction Engine:** Manages state-based topics and audit trails

## Relationships
- **Catalog Service / Circulation Service -> Schema Registry:** Validate event schemas over HTTP/TLS
- **Producers -> Broker Engine:** Publish events via Kafka protocol over TLS 1.3 with mTLS, SASL/SCRAM-512, and idempotent producers (`enable.idempotence=true`)
- **Broker Engine -> Notification Service:** Push-based consumer delivery using Kafka consumer groups
- **Broker Engine -> OpenTelemetry Backend:** Export metrics via Prometheus exporters and tracing headers (W3C Trace Context)

## Technology Stack
- **Apache Kafka:** Chosen for log retention, high throughput, and native stream-processing
- **Strimzi Operator:** Automates Kubernetes deployment, scaling, and rolling upgrades
- **Avro / JSON Schema:** Ensures strict contract validation at the broker boundary
- **EU-hosted Cloud KMS:** Manages application-layer encryption keys for PII payloads with automated rotation
- **OpenTelemetry & Prometheus:** Enables distributed tracing and metric collection

## Rationale
- The architecture guarantees zero data loss, strict EU-only data residency, and application-layer PII encryption to meet GDPR requirements.
- It decouples core circulation workflows from notifications and catalog updates, ensuring high performance and reliable asynchronous processing.