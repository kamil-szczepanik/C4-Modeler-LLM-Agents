## Overview
The Notification Dispatcher is a container within the Library Management System responsible for securely and reliably processing asynchronous events to deliver critical alerts to patrons and staff. It ensures high-performance event-driven messaging while strictly adhering to EU data residency and security compliance.

## Key Elements
- Notification Dispatcher [container] (Go)
- Event Consumer [component] (Go / AMQP)
- Notification Router [component] (Go)
- Template Engine [component] (Go)
- Delivery Worker Pool [component] (Go)
- External Client Adapter [component] (Go / HTTP Client)
- Audit Logger [component] (Go)
- RabbitMQ [container] (Message Broker)
- Notification Service [externalSystem] (External Notification Service)

## Relationships
- RabbitMQ -> Event Consumer: Consumes notification events [AMQP over TLS 1.3]
- Event Consumer -> Notification Router: Internal function call
- Notification Router -> Template Engine: Internal function call
- Template Engine -> Delivery Worker Pool: Internal channel-based dispatch
- Delivery Worker Pool -> External Client Adapter: Internal function call
- External Client Adapter -> Notification Service: Sends notifications [REST / HTTPS over TLS 1.3 with mTLS/OAuth 2.0]

## Technology Stack
- Go: Chosen for high-concurrency worker pools and minimal memory footprint
- RabbitMQ: Facilitates asynchronous event-driven messaging with Dead-Letter Exchange support
- OpenTelemetry: Provides distributed tracing across event consumption and REST dispatches
- Prometheus: Tracks worker pool saturation and queue depth metrics for HPA
- Kubernetes: Hosts distroless container deployment with HPA in EU-central region

## Rationale
This architecture uses an event-driven Go implementation to meet low-latency and high-throughput requirements while executing within EU data residency constraints. Internal security, templating, and auditing components ensure strict PII data minimization and regulatory compliance.