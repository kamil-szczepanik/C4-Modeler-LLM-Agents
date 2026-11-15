## Overview
The Scheduling Service Container is a core backend component of the Clinic Management System designed to manage appointment scheduling and resource clash detection for healthcare providers. It ensures high-availability, HIPAA/GDPR compliance, and seamless integration with patient portals and notification gateways.

## Key Elements
- Scheduling Service Container (Node.js / TypeScript)
- Scheduling API Controller (TypeScript / Express or Fastify)
- Resource Clash Engine (TypeScript)
- Appointment Manager (TypeScript)
- Notification Dispatcher (TypeScript)
- Clinical Database (PostgreSQL)
- Audit & Observability Sidecar (FluentBit / Prometheus)
- External Notification Gateway (Twilio/SendGrid)

## Relationships
- API Gateway / BFF Container -> Scheduling Service Container: Routes internal requests [gRPC over mTLS]
- Scheduling API Controller -> Resource Clash Engine: Executes validation logic [In-memory / Function call]
- Resource Clash Engine -> Clinical Database: Enforces atomic locks [SQL with SERIALIZABLE isolation over TLS 1.3]
- Appointment Manager -> Notification Dispatcher: Queues reminders [AMQP/RabbitMQ]
- Notification Dispatcher -> Notification Gateway: Dispatches alerts [HTTPS with TLS 1.3]
- Scheduling Service Container -> Audit & Observability Sidecar: Emits logs and metrics [Stdout / Prometheus metrics]

## Technology Stack
- Node.js / TypeScript: Chosen for rapid development of appointment business logic within the scheduling container.
- PostgreSQL: Utilized with SERIALIZABLE isolation and advisory locks to prevent double-booking race conditions.
- AMQP/RabbitMQ: Implements asynchronous messaging to decouple appointment transactions from notification delivery.
- gRPC over mTLS: Secures internal communication between the API gateway and the scheduling container.
- FluentBit / Prometheus: Provides tamper-evident logging, metrics, and distributed tracing.

## Rationale
This architecture ensures strict concurrency control and data integrity for high-stakes medical scheduling while maintaining 99.99% uptime and regulatory compliance. Asynchronous decoupling of notifications protects core booking performance against external network latencies.