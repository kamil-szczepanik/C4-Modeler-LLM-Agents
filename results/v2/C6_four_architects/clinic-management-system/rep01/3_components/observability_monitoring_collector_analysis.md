## Overview
The Observability & Monitoring Collector aggregates metrics, traces, and logs for the Clinic Management System across hybrid infrastructure. It ensures strict HIPAA/GDPR compliance via automated PHI/PII redaction and audit enforcement while maintaining 99.99% availability.

## Key Elements
- OTLP Receiver & mTLS Terminator (Go)
- Data Redaction Processor (Custom Go Component)
- Trace Sampler Processor (Go)
- Metrics Aggregator Component (Prometheus/Go)
- Audit & Compliance Enforcer (Go)
- Prometheus Remote-Write Exporter (Go)
- Grafana Loki Exporter (Go)
- OTLP Storage Exporter (Go)
- Key Management Service (HashiCorp Vault / AWS KMS)
- Audit Log Store (PostgreSQL Append-Only tables / AWS S3 Glacier)

## Relationships
- Upstream Containers -> OTLP Receiver & mTLS Terminator: Ingests telemetry data [gRPC/OTLP over TLS]
- OTLP Receiver & mTLS Terminator -> Data Redaction Processor & Trace Sampler Processor: Passes telemetry payloads [Internal Memory Call]
- Data Redaction Processor -> Key Management Service: Fetches masking policies and keys [HTTPS/REST, mTLS]
- Data Redaction Processor -> Audit & Compliance Enforcer: Validates sanitization compliance [Internal Memory Call]
- Audit & Compliance Enforcer -> Audit Log Store: Persists verification logs [PostgreSQL Wire Protocol over TLS]
- Trace Sampler Processor -> OTLP Storage Exporter: Forwards sampled traces [Internal gRPC]
- Metrics Aggregator Component -> Prometheus Remote-Write Exporter: Forwards metrics [HTTP/Snappy]
- Data Redaction Processor -> Grafana Loki Exporter: Streams sanitized logs [gRPC/OTLP]

## Technology Stack
- OpenTelemetry Collector: Core telemetry processing engine for distributed tracing, metrics, and logging.
- Go / C++: High-performance languages for collector components and processors.
- Prometheus & Grafana Loki: Storage and querying backends for metrics and structured logs.
- gRPC / OTLP: Secure transport protocol for inter-container telemetry transmission.
- PostgreSQL / AWS S3 Glacier: Compliant persistent storage for audit logs and retention.

## Rationale
This component-based collector architecture decouples ingestion, redaction, and export to meet strict HIPAA/GDPR data protection standards. Tail-based sampling and in-memory aggregation optimize cross-region bandwidth across the hybrid cloud while sustaining a 99.99% availability SLA.