## Overview
The Billing & Claims Service is a Spring Boot microservice within the Clinic Management System that automates insurance claim submissions, payment processing, and financial ledger management. It ensures high availability, strict financial auditing, and compliance with healthcare data regulations for medium-sized clinics.

## Key Elements
- Medical Biller / Billing Specialist (User persona)
- Patient / Consumer (User persona)
- Billing & Claims Service (Spring Boot Container)
- Claim Management Component (Spring MVC/Data with Drools Rules Engine)
- Payment Processing Component (Spring Integration with Tokenization Vault)
- Billing Engine / Ledger Component (PostgreSQL with AES-256 and TDE)
- Audit & Retention Publisher
- API Gateway / Reverse Proxy (Envoy/NGINX)
- RabbitMQ Message Broker
- Payment Gateway / Insurance Clearinghouse
- SIEM & Immutable Cold Storage

## Relationships
- API Gateway -> Billing & Claims Service: Routes billing traffic [gRPC over mTLS]
- Claim Management Component -> RabbitMQ: Publishes scrubbed insurance claims [AMQP with message-level envelope encryption]
- Payment Processing Component -> Payment Gateway / Insurance Clearinghouse: Submits transactions [Asynchronous messaging via RabbitMQ]
- Billing Engine / Ledger Component -> PostgreSQL: Persists ledger data and itemized statements [JDBC with column-level AES-256]
- Audit & Retention Publisher -> SIEM & Immutable Cold Storage: Streams cryptographically signed audit logs [TLS 1.3]

## Technology Stack
- Java / Spring Boot / Spring MVC: Core runtime and framework for predictable enterprise performance
- PostgreSQL: Relational database with TDE and column-level AES-256 for ACID compliance and secure ledger storage
- RabbitMQ: Asynchronous message broker for reliable claim submission and decoupled clearinghouse communication
- Drools / Spring Expression Language: Embedded rules engine for high-speed automated claim scrubbing
- OpenTelemetry & Prometheus: Distributed tracing and monitoring for financial transaction SLOs

## Rationale
This architecture uses asynchronous messaging via RabbitMQ and resilient circuit breakers to guarantee business continuity during transient external clearinghouse outages. Component decomposition and PostgreSQL partitioning satisfy strict 10-year data retention and 99.99% availability requirements without performance degradation.