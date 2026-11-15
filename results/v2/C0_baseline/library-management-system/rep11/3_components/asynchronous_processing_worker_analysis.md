## Overview
The Asynchronous Processing Worker is a background service within the Library Management System that handles decoupled tasks such as batch catalogue indexing, fine calculations, and automated patron notifications. It ensures high performance and meets the 99th-percentile search response requirement under 800 ms while adhering to EU-only data residency constraints.

## Key Elements
- Asynchronous Processing Worker (.NET Core Worker Service)
- Message Consumer Component (MassTransit [.NET])
- Workflow Orchestrator Component (C# domain logic)
- Notification Dispatcher Component (HttpClient with Polly)
- Audit Logging Interceptor Component (Serilog with structured enrichment)
- Message Broker (RabbitMQ / Redis)
- Integration Gateway (Kong / Envoy)
- EU Notification Service
- Central Logging & Monitoring SIEM

## Relationships
- Message Consumer -> Message Broker: Pulls asynchronous jobs [AMQP/TCP with payload encryption and SCRAM-SHA-512/mTLS]
- Message Consumer -> Workflow Orchestrator: Invokes task handlers [In-Memory]
- Workflow Orchestrator -> Notification Dispatcher: Triggers patron alerts [In-Memory]
- Notification Dispatcher -> Integration Gateway: Forwards outbound requests [HTTPS/REST with mTLS and Polly circuit breaker]
- Workflow Orchestrator -> Audit Logging Interceptor: Dispatches domain events [In-Memory Event Bus]
- Audit Logging Interceptor -> Central Logging & Monitoring SIEM: Ships structured audit payloads [OTLP/gRPC over TLS 1.3]

## Technology Stack
- .NET Core Worker Service: Chosen for high-throughput, cross-platform background task processing.
- MassTransit (.NET): Provides robust message consumption, retry policies, and dead-letter queue handling.
- Polly: Implements circuit breakers, bounded exponential backoff, and jitter for resilient external egress.
- Serilog: Enables structured logging and PII-sanitized audit trails.
- Kubernetes: Hosts stateless worker pods with Horizontal Pod Autoscalers driven by custom Prometheus metrics.

## Rationale
This architecture ensures non-blocking self-service workflows and responsiveness during peak loads by offloading heavy batch processing to a resilient background worker. Strict security controls, payload encryption, and audit logging guarantee EU regulatory compliance and transparent traceability.