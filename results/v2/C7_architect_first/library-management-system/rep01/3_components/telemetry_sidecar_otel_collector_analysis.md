## Overview
[Telemetry Sidecar / OTEL Collector container decomposes into a secure OpenTelemetry pipeline to ingest, sanitize, and forward application telemetry while enforcing EU data residency.]

## Key Elements
* Receivers Component (OpenTelemetry Receiver Modules)
* Processors Component (OTEL Processor Pipeline & PII Scrubbing)
* Memory Limiter & Sampler Component
* Exporters Component (OTEL Exporter Modules)
* Persistent Queueing Extension (Encrypted at Rest)
* Prometheus Self-Monitoring Endpoint

## Relationships
* Core Domain Service, Search Service, and Async Worker push telemetry to Receivers Component via OTLP/gRPC.
* Receivers Component authenticates internal microservices using Kubernetes service account tokens.
* Exporters Component forwards processed telemetry to Centralized Observability Platform via TLS 1.3 / mTLS and OTLP/gRPC.

## Technology Stack
* OpenTelemetry Collector Contrib (Go-based) for native performance and broad plugin support.
* Kubernetes Sidecar Pattern for strict pod-level isolation and namespace boundaries.
* Regex-based PII Masking Processor for GDPR compliance.
* Persistent File Storage Extension with encryption at rest for backpressure and queueing.

## Rationale
[This component-level design secures telemetry transport and enforces strict EU data residency by scrubbing PII at the edge. Additionally, it preserves 100% of the metrics needed to track the 99th-percentile search response SLA under 800 ms.]