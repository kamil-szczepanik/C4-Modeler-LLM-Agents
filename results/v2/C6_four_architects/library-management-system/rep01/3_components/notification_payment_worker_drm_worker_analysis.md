## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. The system ensures robust asynchronous third-party integration while strictly maintaining EU-only data residency.

## Key Elements
- **Notification & Payment Worker / DRM Worker**: Python/Celery container isolating third-party integrations
- **Kafka Task Router**: Internal component for ingesting asynchronous task payloads
- **Payment Task Consumer**: Internal component processing financial events
- **Notification Dispatcher**: Internal component formatting and delivering alerts
- **DRM License Manager**: Internal component interacting with digital rights endpoints
- **Worker State Cache Manager**: Internal component tracking task idempotency and retry states
- **Worker DLQ & Retry Handler**: Internal component managing failed task exceptions and dead-letter queues
- **Message Broker**: Apache Kafka
- **Caching Layer**: Redis
- **External Services**: EU-Hosted Payment Gateway, Notification Service, Digital Content Repository / DRM Provider

## Relationships
- **Message Broker** -> **Kafka Task Router**: Consumes asynchronous task events via TCP / Kafka Protocol
- **Kafka Task Router** -> **Payment Task Consumer / Notification Dispatcher / DRM License Manager**: Delegates tasks internally via Python Function Calls / Celery routing
- **Payment Task Consumer / Notification Dispatcher / DRM License Manager** -> **Caching Layer**: Stores task idempotency keys and retry states via TCP / Redis Protocol
- **Payment Task Consumer** -> **EU-Hosted Payment Gateway**: Processes secure financial transactions via HTTPS/REST
- **Notification Dispatcher** -> **Notification Service**: Dispatches alerts via HTTPS/REST
- **DRM License Manager** -> **Digital Content Repository / DRM Provider**: Provisions access tokens via HTTPS/REST
- **Payment Task Consumer / Notification Dispatcher / DRM License Manager** -> **Worker DLQ & Retry Handler**: Offloads persistently failed jobs via in-process Python exception handling
- **Worker DLQ & Retry Handler** -> **Message Broker**: Publishes poisoned messages to a dedicated DLQ topic via TCP / Kafka Protocol

## Technology Stack
- **Python with Celery**: Powers the worker container and asynchronous task execution natively
- **Apache Kafka**: Acts as the message broker for event distribution and dead-letter queue management
- **Redis (redis-py)**: Provides caching for task idempotency keys and retry states
- **HTTPS/REST**: Secures all external communications with EU-hosted third-party services

## Rationale
This architecture decouples ingestion, execution, state management, and failure recovery to prevent cascading failures from third-party services. The chosen technology stack guarantees fault-tolerant, idempotent execution while strictly complying with EU data residency constraints.