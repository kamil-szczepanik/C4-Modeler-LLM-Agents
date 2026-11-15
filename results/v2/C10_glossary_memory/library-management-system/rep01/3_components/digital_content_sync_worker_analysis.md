## Overview
[The Digital Content Sync Worker is an asynchronous processing container within the Library Management System that synchronizes digital assets from external providers. It ensures high-performance metadata ingestion while maintaining strict EU-only data residency constraints.]

## Key Elements
- Sync Task Consumer
- Provider Integration Client
- Catalog Persistence Adapter
- Telemetry & Audit Publisher
- Sync Circuit Breaker & Retry Manager

## Relationships
- Circulation & Core Engine -> Sync Task Consumer: Queues sync tasks [Async Message Queues (RabbitMQ/Redis, AMQPS)]
- Provider Integration Client -> Third-Party Digital Content Providers (OverDrive/Libby): Syncs digital assets [OAuth2, HTTPS/REST]
- Catalog Persistence Adapter -> Primary Database: Writes metadata [Postgres Wire Protocol over mTLS]
- Telemetry & Audit Publisher -> EU Monitoring & APM Provider: Sends metrics and traces [OTLP/HTTPS]

## Technology Stack
- Node.js with TypeScript: Chosen for asynchronous I/O efficiency during high-concurrency external REST API pagination.
- KEDA (Kubernetes Event-driven Autoscaling): Used for queue-depth-based horizontal scaling of worker pods.
- PostgreSQL with Bounded Connection Pool: Persists catalog data securely with strict encryption at rest (AES-256).

## Rationale
[This architecture uses decoupled asynchronous workers and circuit breakers to prevent database exhaustion and third-party API throttling. It guarantees scalable, resilient ingestion of digital content while satisfying strict EU regulatory and performance requirements.]