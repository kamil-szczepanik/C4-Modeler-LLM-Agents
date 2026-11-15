## Overview
[The Patient & Scheduling Service manages patient registrations, demographic capture, and appointment scheduling with conflict checks for the Clinic Management System. It ensures high availability, strict HIPAA/GDPR compliance, and sub-second performance across a hybrid cloud infrastructure.]

## Key Elements
* **Patient Registry Controller**: Go, chi/gRPC component handling REST/gRPC endpoints and JWT-based RBAC for patient demographics.
* **Scheduling Engine**: Go component executing resource clash checks using an in-memory interval tree and atomic DB locks.
* **Audit Interceptor**: Go middleware providing cryptographic audit logging signed via HashiCorp Vault.
* **Notification Dispatcher**: Go worker pool managing asynchronous patient reminders and appointment alerts.
* **PostgreSQL with Patroni**: Relational database providing ACID-compliant storage with encrypted connections.
* **NATS / RabbitMQ**: Message broker handling domain events (`PatientRegistered`, `AppointmentBooked`) with DLQ configuration.

## Relationships
* **API Gateway (Envoy)** -> **Patient Registry Controller**: Routes external client requests [gRPC over Istio mTLS].
* **Scheduling Engine** -> **PostgreSQL with Patroni**: Executes booking transactions and clash checks [Encrypted SQL].
* **Patient Registry Controller** -> **NATS / RabbitMQ**: Publishes domain events [TLS 1.3].
* **Scheduling Engine** -> **Notification Dispatcher**: Triggers async notifications [Internal channels / TLS 1.3].
* **Notification Dispatcher** -> **External Notification Gateway**: Sends patient alerts with PII masking [HTTPS / TLS 1.3 with certificate pinning].

## Technology Stack
* **Go**: Chosen for high concurrency and performance to achieve P95 latency targets under 1 second.
* **PostgreSQL with Patroni**: Selected for high availability (99.99%) and robust ACID transaction guarantees.
* **HashiCorp Vault**: Implemented for dynamic secret injection and cryptographic audit log signing to satisfy compliance mandates.
* **Istio Service Mesh**: Deployed for zero-downtime canary deployments, circuit breaking, and mTLS security.
* **NATS / RabbitMQ**: Used for reliable asynchronous event messaging with backpressure management.

## Rationale
[Decomposing the service into specialized Go components ensures sub-second scheduling performance and 99.99% availability. Integrating Istio mTLS, HashiCorp Vault, and strict cryptographic audit controls fulfills stringent HIPAA and GDPR security mandates in a hybrid cloud environment.]