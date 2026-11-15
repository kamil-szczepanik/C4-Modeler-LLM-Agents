## Overview
The Finance & Billing container manages financial transactions, insurance claims, and invoicing for the Clinic Management System. It ensures secure, high-availability processing for medium-sized hospitals and clinics.

## Key Elements
- InvoiceGenerator: Spring component rendering itemized patient statements
- ClaimProcessor: Spring WebFlux component formatting and submitting ANSI X12/HL7 FHIR claims
- PaymentEngine: Spring component integrating with external Payment Gateways using Resilience4j
- LedgerService: Spring Data JPA service managing append-only, partitioned financial ledgers
- PostgreSQL cluster: Database utilizing table partitioning and immutable INSERT/SELECT roles
- Apache Kafka: Event bus handling asynchronous invoicing and claim events via Spring Cloud Stream

## Relationships
- API Gateway -> Finance & Billing: Proxies requests via gRPC over mTLS
- Finance & Billing -> PostgreSQL cluster: Persists financial data via Secure TCP/TLS
- Finance & Billing -> Payment Gateway: Processes transactions and insurance claims via HTTPS REST with mTLS and certificate pinning
- LedgerService -> Apache Kafka: Publishes payment and invoicing events using transactional outbox patterns

## Technology Stack
- Spring Boot & Spring WebFlux: Frameworks for synchronous and reactive asynchronous processing
- PostgreSQL: Relational database with date-range partitioning for 10-year audit retention
- Apache Kafka & Spring Cloud Stream: Event-driven backbone for asynchronous communication
- Resilience4j: Circuit breaking and bulkhead patterns for external gateway isolation
- OpenTelemetry & Prometheus: Observability and distributed tracing for transaction monitoring

## Rationale
This architecture uses reactive pipelines and bulkhead isolation to maintain high availability and prevent thread starvation during peak batch billing cycles. Strict append-only database partitioning and field-level encryption satisfy HIPAA, GDPR, and 10-year financial data retention mandates.