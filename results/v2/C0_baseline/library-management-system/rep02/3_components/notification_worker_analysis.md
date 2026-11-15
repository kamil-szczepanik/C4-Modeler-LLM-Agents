## Overview
- Asynchronous Notification Worker container for the Library Management System.
- Processes, templates, and securely dispatches multi-channel alerts while maintaining EU data residency.

## Key Elements
- Notification Worker (Go container)
- Consumer / Event Listener component
- Template Engine component
- Dispatch Router component
- Provider Adapters component
- Message Broker (Kafka/RabbitMQ)
- EU Notification Service (External)

## Relationships
- Consumer / Event Listener -> Message Broker: Consumes events [AMQP/Kafka via mTLS]
- Consumer / Event Listener -> Template Engine: Passes payloads [Go structs]
- Template Engine -> Dispatch Router: Forwards messages [Go structs]
- Dispatch Router -> Provider Adapters: Delegates dispatch with fallback [Go interfaces]
- Provider Adapters -> EU Notification Service: Sends external alerts [HTTPS/REST with TLS 1.3]

## Technology Stack
- Go: High-performance, concurrent language for the notification worker
- Kafka/RabbitMQ: Message broker for zero message loss and queuing
- TLS 1.3 & mTLS: Secure transport and authentication protocol
- Kubernetes & KEDA: Container orchestration and queue-depth horizontal autoscaling
- HashiCorp Vault: Dynamic secret management and API key rotation

## Rationale
- Decouples notification dispatch from core circulation workflows to maintain sub-800ms search performance.
- Enforces strict EU data residency and PII sanitization via isolated components, mTLS, and encrypted queues.