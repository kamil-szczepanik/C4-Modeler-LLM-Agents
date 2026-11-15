## Overview
The Scheduling Service manages patient appointment scheduling and resource clash checks within the Clinic Management System. It ensures high availability and concurrency control for medium-sized hospitals and clinics.

## Key Elements
* **Appointment API Handler**: Go-based component receiving gRPC requests from the API Gateway.
* **Conflict Detection Engine**: Go-based business logic component for resource clash checks.
* **Calendar Storage Repository**: Go database interface managing persistence.
* **Notification Dispatcher**: Go component handling asynchronous event consumption.
* **Redis Cache**: External cache managing distributed scheduling locks.
* **PostgreSQL Database**: Persistent storage with AES-256 encryption.
* **Apache Kafka**: Event broker for domain events.
* **SMS / Notification Gateway**: External service for patient reminders.

## Relationships
* **API Gateway -> Appointment API Handler**: Routes requests via gRPC over mTLS.
* **Appointment API Handler -> Conflict Detection Engine**: Invokes business rules via direct function calls.
* **Conflict Detection Engine -> Redis Cache**: Acquires distributed locks via Redis Protocol over TLS.
* **Conflict Detection Engine -> PostgreSQL Database**: Persists confirmed appointments via PostgreSQL wire protocol using TLS and AES-256.
* **Conflict Detection Engine -> Apache Kafka**: Publishes `AppointmentScheduled` events via Kafka Protocol over TLS.
* **Notification Dispatcher -> SMS / Notification Gateway**: Sends appointment reminders via HTTPS/REST.

## Technology Stack
* **Go**: Used for all scheduling components for high performance and concurrency support.
* **gRPC over mTLS**: Ensures secure, high-performance service-to-service communication.
* **Redis**: Provides fast distributed locking to prevent booking race conditions.
* **Apache Kafka**: Enables asynchronous, decoupled event-driven messaging.
* **PostgreSQL**: Guarantees ACID compliance and secure persistent storage.

## Rationale
This component architecture isolates high-concurrency scheduling logic using a dedicated Conflict Detection Engine backed by Redis locks to prevent race conditions. Asynchronous event publishing via Kafka ensures reliable, decoupled notifications while meeting high availability and security constraints.