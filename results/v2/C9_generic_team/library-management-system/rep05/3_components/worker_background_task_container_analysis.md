## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The architecture ensures EU data residency and strict <800 ms search performance.

## Key Elements
- Worker / Background Task Container
- Message Broker Container (RabbitMQ / Kafka)
- Distributed Cache Container (Redis)
- External Legacy ILS / Campus ERP Systems
- Observability Sidecar

## Relationships
- Worker Container -> Message Broker Container: Consumes jobs using AMQP / Kafka protocols
- Worker Container -> Distributed Cache Container: Manages locks and state checkpoints using Redis protocol
- Worker Container -> External Legacy ILS: Syncs data using Scheduled Batch Protocols with circuit breakers

## Technology Stack
- Redis: Used for distributed locking, rate limiting, and storing idempotent state checkpoints
- RabbitMQ / Kafka: Powers priority queue partitioning, exponential backoffs, and Dead-Letter Queues (DLQs)
- Protocol Buffers / JSON Schema: Enforces structured payload versioning and backward-compatible data contracts
- Horizontal Pod Autoscaling (HPA): Dynamically scales workers based on queue depth and CPU metrics

## Rationale
Idempotency, circuit breakers, and resource isolation protect fragile legacy systems while preserving worker resources. Queue partitioning and dynamic scaling prevent heavy background syncs from violating the 800 ms search performance SLA.