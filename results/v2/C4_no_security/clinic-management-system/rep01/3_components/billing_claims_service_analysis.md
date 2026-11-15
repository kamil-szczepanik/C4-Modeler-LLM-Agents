## Overview
The Billing & Claims Service is a container within the Clinic Management System that handles patient invoices, insurance claims, and payments. It ensures high availability, strict HIPAA/GDPR compliance, and low-latency financial transactions for clinics.

## Key Elements
- **Single-Page Application / Mobile Client**: Patient and Billing Specialist user interface (React / TypeScript).
- **Billing & Claims Service**: Spring Boot / Java 21 container containing Invoice Management, Claims Engine, Payment Gateway Integration, Outbox Dispatcher, and Notification & Exception Handler components.
- **PostgreSQL Clusters**: Encrypted relational data store (AES-256) utilizing Spring Data JPA.
- **Integration Service**: Apache Camel / Spring Integration handling external routing.
- **External Systems**: Insurance Clearinghouse APIs, Payment Gateways, and SMS/Email Notification Gateway.

## Relationships
- Single-Page Application -> Billing & Claims Service: Routes billing inquiries and payments [gRPC over Istio mTLS]
- Claims Engine -> Outbox Dispatcher: Persists and dispatches transactional messages [Internal Java method call]
- Outbox Dispatcher -> Integration Service: Forwards asynchronous claim payloads [gRPC / Internal Queue]
- Integration Service -> Insurance Clearinghouse APIs: Submits and verifies claims [HTTPS]
- Billing & Claims Repository -> PostgreSQL Clusters: Reads and writes billing data [Encrypted connections with AES-256]

## Technology Stack
- **Spring Boot / Java 21**: Provides a robust foundation for building enterprise-grade backend services.
- **Spring Data JPA**: Simplifies relational database operations with PostgreSQL.
- **Resilience4j**: Implements circuit breakers to prevent cascade-failure risks during clearinghouse outages.
- **OpenTelemetry & Prometheus**: Enables distributed tracing and real-time metric tracking for performance SLAs.
- **Kubernetes Secrets & Vault**: Manages secure, dynamic injection of payment gateway and clearinghouse credentials.

## Rationale
This architecture ensures 99.99% availability by decoupling core billing operations from unreliable external networks via the Asynchronous Outbox Pattern. It satisfies strict HIPAA and GDPR mandates through AES-256 encryption, zero-hardcoded secrets, and an immutable audit streaming pipeline.