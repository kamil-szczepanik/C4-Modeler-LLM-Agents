## Overview
The Billing Service is a core container within the Clinic Management System designed to handle financial operations, insurance claim submissions, and dispute workflows. It ensures robust transactional integrity and compliance for medium-sized hospitals and clinics.

## Key Elements
- **Billing Officers**: Primary users managing invoices, payments, and insurance claims.
- **Patients**: End-users accessing transparent billing summaries and self-service payments via the Patient Portal.
- **Billing Service**: Java / Spring Boot container for financial processing.
- **Invoice Controller**: Spring MVC component handling REST/gRPC endpoints, invoice generation, and dispute workflows.
- **Claim Processor**: Spring Batch / Integration component managing claim generation and batch submission.
- **Payment Gateway Client**: Spring Cloud OpenFeign component with Resilience4j circuit breakers for external communication.
- **Dispute Manager**: Spring Service handling partial refunds and dispute tracking.
- **Audit Publisher**: Spring Cloud Stream component emitting immutable audit events.
- **Billing Data Repository**: Spring Data JPA / Hibernate component interacting with PostgreSQL.
- **External Systems**: Insurance/Payer Gateways, Message Broker (Apache Kafka), Audit & Compliance Service, WORM Object Storage.

## Relationships
- API Gateway / Reverse Proxy -> Invoice Controller: Routes API requests [gRPC / REST]
- Claim Processor -> Message Broker: Publishes `ClaimSubmittedEvent` [Apache Kafka]
- Payment Gateway Client -> Insurance/Payer Gateways: Submissions and processing [HTTPS / REST / EDI X12]
- Audit Publisher -> Message Broker: Publishes `FinancialAuditLogEvent` [Apache Kafka]
- Dispute Manager -> Billing Data Repository: Persists dispute states [JPA / JDBC]

## Technology Stack
- **Java / Spring Boot**: Chosen for robust ACID transactional integrity in financial operations.
- **Spring MVC & Spring Batch**: Used for REST/gRPC endpoint exposure and asynchronous claim batch processing.
- **Spring Cloud OpenFeign & Resilience4j**: Manages external communication with circuit breakers and fallback queues to prevent cascading failures.
- **Spring Data JPA / Hibernate & PostgreSQL**: Enforces transactional boundaries with AES-256 encryption at rest and automated date-based table partitioning.
- **Apache Kafka**: Provides asynchronous messaging, event publishing, and Dead Letter Queues (DLQ).
- **OpenTelemetry**: Mandated for distributed tracing across boundaries.

## Rationale
This architecture ensures 99.99% high availability and resilience against external payer outages through circuit breakers and asynchronous processing. It satisfies strict HIPAA, GDPR, and 10-year data retention constraints via AES-256 encryption, database partitioning, and WORM archiving.