## Overview
[The Worker Service container handles background tasks, asynchronous operations, and external integrations for the Library Management System, ensuring EU data residency compliance and reliable performance.]

## Key Elements
- Task Dispatcher (Python, Celery)
- Payment Processor Component (Python)
- Notification Dispatcher (Python)
- Data Sync Component (Python)
- Scheduled Task Scheduler Component (Python, Celery Beat)
- Transient Job State Store (Redis)
- RabbitMQ Message Broker
- EU-Compliant Payment Gateway
- Third-Party Notification Service
- Circulation & Search Service (Elasticsearch)

## Relationships
- API Gateway -> Task Dispatcher: Triggers asynchronous background tasks [gRPC over Istio service mesh with mTLS]
- Scheduled Task Scheduler Component -> Task Dispatcher: Triggers periodic background jobs [Internal function call]
- Task Dispatcher -> RabbitMQ Message Broker: Consumes and routes background jobs [AMQP with TLS 1.3, SCRAM-SHA-512]
- Task Dispatcher -> Transient Job State Store: Checks and sets idempotency deduplication keys [Redis Protocol over TLS]
- Payment Processor Component -> EU-Compliant Payment Gateway: Processes financial transactions securely [HTTPS]
- Notification Dispatcher -> Third-Party Notification Service: Sends notifications and alerts [HTTPS]
- Data Sync Component -> Circulation & Search Service: Handles indexing updates [REST/gRPC]

## Technology Stack
- Python / Celery: Core framework for asynchronous task execution and worker management
- RabbitMQ: Message broker with Dead Letter Queues (DLQ) for reliable task routing
- Redis: Transient job state store for idempotency deduplication keys with replication and AOF persistence
- Celery Beat: Drives scheduled batch workflows and periodic task scheduling
- OpenTelemetry: Injected into gRPC payloads for distributed tracing across the Istio mesh
- KEDA: Enables Horizontal Pod Autoscaling based on RabbitMQ queue depth metrics

## Rationale
[This architecture decouples heavy asynchronous workloads from the core APIs while enforcing strict queue isolation and idempotency to guarantee reliable payment processing and notifications. It meets stringent EU data residency and performance requirements through secure state management and scalable resource allocation.]