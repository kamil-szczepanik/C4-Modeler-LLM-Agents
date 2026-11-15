## Overview
The Patient & Scheduling Service manages patient admissions and appointment scheduling for the Clinic Management System. It ensures high availability, zero double-booking incidents, and strict HIPAA/GDPR compliance across hybrid infrastructure.

## Key Elements
- **Patient Registry Controller**: Go (Gin/Protobuf) component for patient registration.
- **Scheduling Engine**: Go component executing appointment logic and resource clash checks.
- **Policy Enforcer**: Go component evaluating cancellation rules and receptionist override permissions.
- **Waitlist Manager**: Go component managing waitlist promotion logic.
- **Event Publisher**: Go (AMQP client) component dispatching domain and waitlist events.
- **Data Access Repository**: Go (pgx/sqlc) component interfacing with PostgreSQL.
- **RabbitMQ**: Message broker using AMQPS.
- **PostgreSQL**: Primary database with AES-256 encryption at rest.

## Relationships
- API Gateway & Patient Portal BFF -> Patient Registry Controller & Scheduling Engine: Routes requests via gRPC over mTLS with JWT/OAuth2 RBAC.
- Scheduling Engine -> Policy Enforcer: Evaluates rules via in-memory function calls.
- Policy Enforcer -> Waitlist Manager: Triggers promotions via in-memory function calls.
- Waitlist Manager -> Event Publisher: Dispatches promotion events via in-memory calls.
- Event Publisher -> RabbitMQ: Publishes messages via AMQPS (TLS-encrypted AMQP) with field-level PII encryption.
- Scheduling Engine -> Data Access Repository: Executes queries with serializable isolation via SQL / TLS.

## Technology Stack
- **Go**: Core language for microservices, chosen for high concurrency and performance.
- **PostgreSQL**: Relational database providing serializable isolation levels to prevent double-booking.
- **RabbitMQ**: Asynchronous broker using AMQPS for secure event-driven workflows.
- **gRPC over mTLS**: Secure protocol for internal service-to-service communication.

## Rationale
Decomposing the Go service into specialized sub-components isolates complex business and policy logic while maintaining strict database transactional boundaries. This design guarantees zero double-bookings, robust concurrency performance, and rigorous HIPAA/GDPR compliance.