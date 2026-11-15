## Overview
The Notification Worker is an asynchronous Go-based container within the Library Management System responsible for dispatching multi-channel patron alerts. It securely processes event messages while enforcing EU data residency and privacy compliance.

## Key Elements
* **Notification Worker**: Go application container deployed in an EU Kubernetes Cluster.
* **Kafka Consumer Component**: Uses `segmentio/kafka-go` for safe JSON event consumption.
* **Preference & Template Engine Component**: Uses Go `text/template` for channel opt-ins and PII sanitization.
* **Dispatcher & Rate-Limiter Component**: Uses `net/http` and `golang.org/x/time/rate` for outbound API calls.
* **DLQ & Audit Forwarder Component**: Routes failed messages and emits delivery events.
* **External Dependencies**: Apache Kafka, Notification Provider, EU Cloud Provider's HSM, Audit Log Stream.

## Relationships
* **Apache Kafka -> Kafka Consumer Component**: Consumes notification events via TCP (SASL/SCRAM or mTLS).
* **Dispatcher & Rate-Limiter Component -> Notification Provider**: Sends outbound messages via HTTPS (TLS 1.3).
* **DLQ & Audit Forwarder Component -> Audit Log Stream**: Emits structured delivery logs via internal network protocols.
* **Notification Worker -> EU Cloud Provider's HSM**: Fetches rotated secrets via Kubernetes Secrets.

## Technology Stack
* **Language & Runtime**: Go (chosen over Python/Celery for lightweight goroutines, lower memory overhead, and elimination of dynamic deserialization risks).
* **Messaging**: Apache Kafka with KafkaConsumer and Dead-Letter Queue (DLQ).
* **Templating & Security**: Go `text/template` with context-aware sanitization and IP whitelisting.
* **Orchestration & Observability**: Kubernetes HPA with Prometheus KEDA, OpenTelemetry, and Fluentbit/Vector sidecar.

## Rationale
Go provides high-throughput concurrent I/O with minimal memory overhead, reducing EU cloud infrastructure costs while avoiding Python's dynamic deserialization vulnerabilities. Strict TLS 1.3 encryption, HSM secret management, and Kafka integration fulfill EU data residency and PII protection requirements.