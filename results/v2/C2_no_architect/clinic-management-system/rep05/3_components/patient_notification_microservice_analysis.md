## Overview
The Patient Notification Microservice is a secure, highly available containerized service that dispatches automated, multi-channel notifications and handles two-way patient messaging for the Clinic Management System. It ensures timely care coordination while strictly adhering to HIPAA and GDPR compliance mandates.

## Key Elements
- **Patient Notification Microservice:** Node.js container handling outbound dispatch logic, multi-channel templating, and webhook ingestion.
- **API Gateway:** Istio Service Mesh with Envoy proxy managing ingress/egress traffic, mTLS, and rate limiting.
- **Message Broker & Queuing:** RabbitMQ / Kafka with Dead-Letter Queues (DLQs) and exponential backoff retry logic.
- **Third-Party Gateways:** External providers for SMS and Email delivery (Twilio, SendGrid).
- **Core Database:** PostgreSQL with PgBouncer connection pooling for updating appointment statuses.
- **Observability Stack:** Prometheus and Datadog for metrics, OpenTelemetry for tracing, and PagerDuty for alerting.

## Relationships
- API Gateway -> Patient Notification Microservice: Triggers notification workflows via [gRPC / HTTPS with mTLS].
- Patient Notification Microservice -> RabbitMQ / Kafka: Publishes and consumes asynchronous dispatch events via [AMQP / TCP].
- Patient Notification Microservice -> Third-Party Gateways (Twilio, SendGrid): Sends SMS/Email messages via [HTTPS REST APIs].
- Third-Party Gateways -> API Gateway -> Patient Notification Microservice: Routes inbound SMS webhooks with HMAC signatures via [HTTPS].
- Patient Notification Microservice -> API Gateway -> Core Database: Updates appointment confirmation statuses via [HTTPS / gRPC].

## Technology Stack
- **Runtime:** Node.js (non-blocking I/O ideal for asynchronous messaging and webhook handling).
- **Security & Networking:** Istio Service Mesh, Envoy proxy, mTLS, JWT validation, and HMAC cryptographic signature verification.
- **Messaging & Resiliency:** RabbitMQ/Kafka, DLQs, and automated Istio circuit breaking for provider failover.
- **Encryption:** AES-256 field-level encryption for queued message content and TLS for data in transit.
- **Observability:** OpenTelemetry, Prometheus, Datadog (with PII log scrubbing), and PagerDuty.

## Rationale
This architecture guarantees 99.99% availability and zero-loss reliability through asynchronous message queues, circuit breakers, and automated provider failover. It rigorously enforces HIPAA and GDPR compliance via payload minimization (`appointment_id` references), field-level encryption, mTLS, and strict PII log scrubbing.