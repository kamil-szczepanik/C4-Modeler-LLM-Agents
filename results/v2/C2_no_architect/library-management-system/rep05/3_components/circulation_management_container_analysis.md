## Overview
The Circulation Management Container is a core backend service within the Library Management System that executes check-outs, returns, renewals, and loan policy enforcement. It ensures high-performance, secure, and EU-compliant library operations for patrons and staff.

## Key Elements
* **Circulation Management Container**: Kubernetes-hosted microservice handling circulation logic.
* **API Gateway**: Entry point issuing OAuth2/OIDC JWTs and routing external traffic.
* **Catalogue Database & Read-Replica**: Multi-zone replicated data store for items and loans.
* **Message Broker**: Kafka / RabbitMQ for asynchronous event publishing.
* **Cloud KMS / Vault**: Secret management and encryption key provider.

## Relationships
* **API Gateway -> Circulation Management Container**: Routes validated requests via Istio mTLS.
* **Circulation Management Container -> Catalogue Database**: Executes queries and updates using TLS 1.3 with connection pooling and circuit-breaking.
* **Circulation Management Container -> Message Broker**: Publishes asynchronous domain events over TLS 1.3.

## Technology Stack
* **Kubernetes & Istio**: Container orchestration and service mesh ensuring mTLS, circuit-breaking, and EU node pinning.
* **OpenTelemetry & Prometheus**: Distributed tracing and metrics for monitoring transaction latencies (<500ms SLA).
* **AES-256 & Kubernetes Secrets**: Data-at-rest encryption and dynamic credential injection via Vault.
* **Idempotent REST APIs**: Ensures safe request retries without local state persistence.

## Rationale
This architecture guarantees strict compliance with EU data residency laws by pinning workloads and encrypting PII at rest. It prioritizes operational resilience through multi-zone database replication, API idempotency, and Istio circuit-breaking to protect physical library workflows.