## Overview
The Notification Worker is an asynchronous Go-based container within the Library Management System that reliably dispatches localized alerts and notifications to patrons and staff. It enforces strict EU-only data residency and PII minimization while handling high-throughput messaging workloads.

## Key Elements
- Notification Worker (Async Worker) [container] (Go)
- Queue Consumer Component [component] (Go / RabbitMQ Client)
- Preference & Routing Component [component] (Go)
- Template Engine Component [component] (Go template library)
- Dispatch Handler Component [component] (Go HTTP/SMTP Client)
- External Notification Service [externalSystem]
- Primary Database (PostgreSQL, EU-hosted) [container]
- EU Monitoring & APM Provider [externalSystem]

## Relationships
- Circulation & Core Engine -> Notification Worker: Queues notification tasks [Async Message Queues (RabbitMQ/Redis)]
- Queue Consumer Component -> Preference & Routing Component: Passes raw job for preference validation [In-memory function call]
- Preference & Routing Component -> Primary Database: Queries patron preferences [Postgres Wire Protocol over mTLS]
- Preference & Routing Component -> Template Engine Component: Passes filtered/routed payload [In-memory function call]
- Template Engine Component -> Dispatch Handler Component: Passes rendered message [In-memory function call]
- Dispatch Handler Component -> External Notification Service: Dispatches alerts and notifications [SMTP/HTTPS API, TLS 1.3]
- Notification Worker -> EU Monitoring & APM Provider: Exports telemetry metrics [OTLP/HTTPS]

## Technology Stack
- Go: Chosen for high concurrency and low memory footprint in async worker tasks
- RabbitMQ / Redis: Utilized for reliable message queueing and dead-letter queue (DLQ) support
- PostgreSQL: Provides persistent storage for patron preferences with mTLS encryption
- TLS 1.3 / AES-256: Ensures secure data transport and encryption at rest for PII compliance

## Rationale
This architecture ensures high-throughput message processing and delivery reliability via asynchronous queues, circuit breakers, and backoff retries. It strictly enforces EU data residency and PII protection through localized caching, encryption, and telemetry scrubbing.