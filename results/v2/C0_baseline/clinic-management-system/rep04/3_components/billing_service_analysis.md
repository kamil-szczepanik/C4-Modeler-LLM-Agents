## Overview
The Billing Service is a container within the Clinic Management System responsible for financial transactions, patient invoices, insurance claims, and dispute workflows. It ensures high availability, PCI-DSS scope reduction, and HIPAA/GDPR compliance across a hybrid cloud infrastructure.

## Key Elements
- **Billing API Controller**: Spring MVC component exposing REST/gRPC endpoints for invoice retrieval and copay settlements.
- **Invoice & Ledger Component**: Java/Spring Boot component managing core billing logic, patient invoices, and immutable ledger entries.
- **Claim Processing Engine**: Java/Spring Boot component handling insurance claim validation and clearinghouse submissions.
- **Dispute & Adjustment Workflow Component**: Java/Spring Boot component managing claim rejections, appeals, and state-machine dispute workflows.
- **Apache Kafka**: Event streaming platform used for outbox pattern, async event publishing, and Dead Letter Queues (DLQ).
- **PostgreSQL Clusters**: Encrypted primary data store with append-only audit tables.
- **Redis Enterprise**: Caching and deduplication tracking layer.
- **WORM Object Storage**: Storage for cryptographically signed, immutable financial audit logs.

## Relationships
- **Kong/Envoy API Gateway -> Billing API Controller**: Routes incoming external traffic via gRPC/REST over mTLS (Istio).
- **Patient Portal BFF -> Billing API Controller**: Requests patient-facing invoices and copay settlements via HTTPS.
- **Invoice & Ledger Component -> PostgreSQL Clusters**: Stores encrypted financial records via JPA/JDBC.
- **Claim Processing Engine -> External Payment Gateway & Insurance Clearinghouse**: Submits claims and verifies insurance via HTTPS (REST/SOAP).
- **Claim Processing Engine & Dispute Handler -> Apache Kafka**: Publishes and consumes domain events, claim rejections, and outbox messages.
- **Dispute & Adjustment Handler -> WORM Object Storage**: Writes cryptographically signed audit logs via secure object storage protocols.

## Technology Stack
- **Java / Spring Boot**: Core language and framework for internal billing components due to enterprise maturity and strong security ecosystem.
- **Spring MVC**: Powers the Billing API Controller for robust REST/gRPC endpoint exposure.
- **Apache Kafka**: Event stream for asynchronous transaction handling, outbox patterns, and DLQ resilience.
- **PostgreSQL**: Relational database with Transparent Data Encryption (TDE) for structured ledger and invoice persistence.
- **Redis Enterprise**: High-performance caching layer used for idempotency keys and replay protection.
- **Resilience4j**: Circuit breaker implementation for external clearinghouse communication.
- **OpenTelemetry**: Standardized distributed tracing framework across all billing components.

## Rationale
This architecture uses fine-grained component decomposition within the Billing Service to isolate complex financial workflows and maintain strict separation of concerns. The event-driven outbox pattern, Redis idempotency checks, and WORM storage integration collectively guarantee 99.99% availability, strict 10-year financial audit compliance, and robust PCI-DSS scope reduction.