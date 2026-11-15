## Overview
The Library Management System provides cataloging, circulation, and self-service portals for libraries while strictly enforcing EU data residency. The Worker Container executes asynchronous background tasks to maintain performance and system responsiveness.

## Key Elements
- Task Dispatch Consumer (Celery Worker, Python)
- Notification Processor (Python)
- Index Synchronizer (Python)
- State Cache Manager (Redis, Python client)
- Fine & Circulation Batch Processor (Python)
- External Systems: RabbitMQ, Search Container (Elasticsearch), Notification Service, Payment Gateway, Database (PostgreSQL), Telemetry Container (Prometheus, Grafana, Fluentbit)

## Relationships
- Task Dispatch Consumer receives messages from RabbitMQ via AMQPS (TLS 1.3)
- Index Synchronizer pushes updates to Search Container via HTTP/REST
- Notification Processor and Fine & Circulation Batch Processor call external services via HTTPS (TLS 1.3)
- All components interact with State Cache Manager (Redis) via TCP/RESP (TLS)
- Fine & Circulation Batch Processor queries Database (PostgreSQL) via JDBC/TCP

## Technology Stack
- Python / Celery: Core language and task queue framework for scalable background processing
- Redis: Ephemeral state management, rate-limiting, and Redlock distributed locking with AES-256 encryption at rest
- RabbitMQ: Message broker with AMQPS transport security and Dead Letter Queues (DLQ)
- KEDA (Kubernetes Event-driven Autoscaling): Queue-depth-based autoscaling for Celery workers
- Fluentbit / Prometheus: Telemetry and audit log streaming with PII masking

## Rationale
This architecture offloads heavy cyclical computations and external integrations from core APIs to meet the sub-800ms search constraint. Robust security controls, EU-bounded data storage, and strict idempotency ensure regulatory compliance and financial reliability.