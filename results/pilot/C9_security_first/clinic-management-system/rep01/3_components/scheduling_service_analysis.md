## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for clinics. The Scheduling Service component handles real-time appointment scheduling, clash detection, and calendar workflows.

## Key Elements
- `AppointmentController`: Handles incoming gRPC routing and OAuth2/OIDC JWT scope validation
- `CalendarManager`: Executes core scheduling business logic and distributed locking
- `ResourceAllocationEngine`: Manages clinician, room, and equipment availability
- `SlotCacheAdapter`: Interfaces with Redis to cache practitioner availability matrices
- `PersistenceAdapter`: Interfaces with Distributed PostgreSQL Database via Spring Data JPA
- `KafkaEventPublisher`: Publishes domain events to Apache Kafka Event Broker
- `NotificationDispatcher`: Processes async domain events for automated reminders and rescheduling

## Relationships
- NGINX/Kong API Gateway -> `AppointmentController`: Routes scheduling requests [gRPC with mTLS]
- `CalendarManager` -> `ResourceAllocationEngine`: Evaluates booking constraints [In-process method calls]
- `CalendarManager` -> `SlotCacheAdapter`: Reads/writes availability [Redis protocol]
- `PersistenceAdapter` -> Distributed PostgreSQL Database: Persists encrypted records [JDBC with AES-256 and distributed locks]
- `KafkaEventPublisher` -> Apache Kafka Event Broker: Streams domain events [SASL/SCRAM authenticated event streaming]

## Technology Stack
- Java / Spring Boot: Core runtime for Scheduling Service components and Spring Beans
- gRPC: Inter-service communication protocol with mTLS for secure transport
- Redis: In-memory caching layer for read-heavy availability matrices
- Distributed PostgreSQL: Primary transactional data store with optimistic and distributed locking
- Apache Kafka: Event broker for decoupling asynchronous notifications and reminders
- OpenTelemetry & Prometheus: Distributed tracing and metrics collection for hybrid observability

## Rationale
This architecture ensures 99.99% availability via active-active Kubernetes hybrid deployment across on-prem and `eu-central-1`. It satisfies HIPAA/GDPR constraints using AES-256 encryption, RBAC, and immutable audit logs.