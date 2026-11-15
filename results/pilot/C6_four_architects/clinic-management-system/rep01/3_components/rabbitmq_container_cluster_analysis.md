## Overview
The Clinic Management System is a hybrid cloud clinical IT platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals. It ensures high availability, 10-year data retention, and HIPAA/GDPR compliance.

## Key Elements
*   RabbitMQ Container cluster (RabbitMQ 3.12+, Quorum Queues, Federation, Shovel plugins)
*   Scheduling Service & Billing Service (Node.js, Docker, Kubernetes)
*   Audit & Compliance Sidecar Container
*   Envoy Service Mesh Container
*   Observability Collector Container (OpenTelemetry, Prometheus)
*   HashiCorp Vault

## Relationships
*   Scheduling Service & Billing Service -> RabbitMQ Container cluster: Publishes/consumes transient clinical events [AMQP 0-9-1, MQTT over TLS 1.3]
*   RabbitMQ Dead Letter Exchanges -> Audit & Compliance Sidecar Container: Forwards unacknowledged or expired payloads [AMQP]
*   RabbitMQ Cluster Operator -> Vault: Automates TLS certificate and credential rotation [HTTPS]
*   RabbitMQ Prometheus plugin -> Observability Collector Container: Exposes broker runtime metrics [HTTP/Prometheus scrape]

## Technology Stack
*   RabbitMQ 3.12+ with Raft consensus: Chosen for active-active quorum queues and fault-tolerant message routing.
*   Encrypted local NVMe storage with StatefulSets: Provides optimal disk I/O throughput for quorum queue WAL logs.
*   TLS 1.3 with SASL/SCRAM-SHA-512: Secures transit messaging to meet HIPAA data protection mandates.
*   RabbitMQ Federation and Shovel plugins: Guarantees seamless cross-region transient event replication between on-premise and AWS `eu-central-1`.

## Rationale
This architecture guarantees 99.99% uptime and partition-tolerant messaging across a hybrid footprint using active-active quorum queues and federation. It enforces strict compliance and security through TLS encryption, virtual host isolation, and automated dead-letter routing to audit sidecars.