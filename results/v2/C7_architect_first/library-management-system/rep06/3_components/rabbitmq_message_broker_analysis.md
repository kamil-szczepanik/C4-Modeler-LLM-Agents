## Overview
The RabbitMQ Message Broker provides asynchronous messaging and zero-loss notification processing for the Library Management System. It ensures high availability and reliable communication across core domain services under strict EU data residency constraints.

## Key Elements
- Exchange Router Component
- Quorum Queue Component
- Connection Manager Component
- Management API/UI Component
- Dead Letter Router Component
- Policy Enforcement Component

## Relationships
- Core Domain Service -> Connection Manager Component [AMQP 0-9-1 with TLS 1.3]
- Notification Service -> Connection Manager Component [AMQP 0-9-1 with TLS 1.3]
- Quorum Queue Component -> Dead Letter Router Component [AMQP 0-9-1]
- Management API/UI Component -> Monitoring Stack [HTTP/S over Port 15672]

## Technology Stack
- RabbitMQ: Core message broker technology chosen for robust AMQP support and quorum queues.
- Quorum Queues: Raft-consensus-backed storage ensuring zero-loss messaging.
- TLS 1.3 & mTLS: Encrypts data in transit and secures service authentication.
- Prometheus: Exports operational metrics for centralized observability.

## Rationale
This architecture uses clustered quorum queues and strict security controls to meet zero-loss messaging and EU data residency constraints. Resource guardrails and priority handling ensure high availability and performance during peak library loads.