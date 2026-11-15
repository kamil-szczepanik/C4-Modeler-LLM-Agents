## Overview
The Billing Microservice handles insurance claim submissions, payment processing, and financial tracking for the Clinic Management System. It operates on a hybrid Kubernetes infrastructure, ensuring HIPAA and GDPR compliance with high availability.

## Key Elements
- Billing API Controller (Spring Boot REST Controller)
- Claim Processing Engine (Domain Service / Spring Bean)
- Payment Integration Adapter (Outbound Adapter)
- Billing Data Repository (Spring Data JPA)
- Audit Event Publisher (Spring Bean / Event Publisher)
- External Payment Gateway / Insurance Clearinghouse
- PostgreSQL Database & WORM Audit Log Store
- Apache Kafka Event Broker & Istio Service Mesh

## Relationships
- API Gateway -> Billing API Controller: Routes internal requests via gRPC over mTLS
- Billing API Controller -> Claim Processing Engine: In-process method calls with validated JWTs/OAuth2
- Claim Processing Engine -> Payment Integration Adapter: In-process events with resilience breakers
- Payment Integration Adapter -> Payment Gateway / Insurance Clearinghouse: TLS-secured AMQP/Kafka with envelope encryption
- Claim Processing Engine -> Billing Data Repository: JDBC over TLS with AES-256 encryption at rest
- Audit Event Publisher -> WORM Audit Log Store: Direct immutable stream over TLS with mTLS and payload signing
- Audit Event Publisher -> Event Broker: Kafka Producer API over mTLS

## Technology Stack
- Java / Spring Boot: Core framework for microservice components due to enterprise maturity
- Spring Data JPA: Standardized relational data access for PostgreSQL
- PostgreSQL & WORM Storage: Persistent transactional storage and 10-year compliant audit retention
- Apache Kafka / RabbitMQ: Asynchronous event messaging and Dead Letter Queues (DLQs)
- Istio Service Mesh (SPIFFE/SPIRE): Enforces strict mTLS and service-to-service security
- OpenTelemetry: Distributed tracing for P99 latency and performance monitoring

## Rationale
This architecture ensures 99.99% uptime and high throughput by decoupling external clearinghouse interactions via asynchronous queues and circuit breakers. Strict data masking, cryptographic signing, and WORM storage guarantee compliance with HIPAA, GDPR, and long-term financial auditing constraints.