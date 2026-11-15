## Overview
[The Notification Dispatcher is a Go-based worker service that asynchronously dispatches notifications to external services for the Library Management System while ensuring EU-only data residency and strict GDPR compliance.]

## Key Elements
- [Event Consumer Worker (Go, segmentio/kafka-go)]
- [Notification Router & Template Engine (Go, in-process logic)]
- [DLQ Handler / Retry Interceptor (Go middleware)]
- [Dispatch Client (Go, net/http with gofeature/gobreaker)]
- [Telemetry Exporter (Go, OpenTelemetry Go SDK)]
- [Configuration & Secrets Manager Client]
- [Integration/Messaging Container (Managed Apache Kafka, EU-hosted)]
- [External Notification Service]
- [Observability Platform & SIEM]

## Relationships
- [Integration/Messaging Container -> Event Consumer Worker: Consumes events via Kafka Protocol with SASL/SCRAM-512 & mTLS]
- [Event Consumer Worker -> Notification Router & Template Engine: Passes events via in-process Go function calls]
- [Notification Router & Template Engine -> Dispatch Client: Routes payload via in-process calls]
- [Dispatch Client -> External Notification Service: Dispatches alerts via REST/JSON over TLS 1.3 with certificate pinning]
- [DLQ Handler / Retry Interceptor -> Integration/Messaging Container: Routes poisoned messages to Kafka DLQ Topic with PII sanitization]
- [Telemetry Exporter -> Observability Platform & SIEM: Streams metrics via OpenTelemetry (OTel) / Prometheus over TLS]

## Technology Stack
- [Go / Worker service: Selected for high-performance concurrent processing and low memory footprint]
- [Kafka Protocol (segmentio/kafka-go): Used for reliable, event-driven messaging and consumer lag tracking]
- [gofeature/gobreaker: Implements circuit breaking to protect against external third-party outages]
- [OpenTelemetry (OTel) / Prometheus: Provides end-to-end telemetry, delivery success rate, and latency tracking]
- [Kubernetes / KEDA: Manages container deployment, liveness/readiness probes, and autoscaling based on consumer lag]

## Rationale
[This architecture ensures high availability, fault tolerance, and 60-second end-to-end delivery SLAs through asynchronous event processing and KEDA-driven autoscaling. It strictly enforces EU data residency and GDPR compliance via automated PII sanitization, in-memory masking, and strict Kubernetes egress network policies.]