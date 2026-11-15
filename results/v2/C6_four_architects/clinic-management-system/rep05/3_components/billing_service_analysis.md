## Overview
[The system is a Clinic Management System designed for medium-sized hospitals and clinics to handle patient admissions, electronic medical records, scheduling, and billing.]
[The architecture uses a hybrid cloud model to ensure high availability, strict HIPAA/GDPR compliance, and long-term data retention.]

## Key Elements
* Invoice Controller (Express.js / TypeScript)
* Claims Processor (TypeScript Business Logic Engine)
* Circuit Breaker Middleware (Opossum / TypeScript)
* Insurance Gateway Client (Axios / HTTPS over TLS 1.3)
* Billing Data Repository (TypeORM / TCP via PgBouncer)
* Billing Audit Logger (TypeScript Event-Driven / TCP)
* Payment Reconciliation Worker (Node.js Worker Threads / Kafka Consumer)
* API Gateway (Nginx / Kong)
* Message Broker (Apache Kafka)
* Primary Database (PostgreSQL)

## Relationships
* API Gateway -> Billing Service: Routes billing traffic [Istio Service Mesh (mTLS / HTTP/2)]
* Claims Processor -> Circuit Breaker Middleware: Invokes external submission [TypeScript]
* Circuit Breaker Middleware -> Insurance Gateway Client: Submits claims [HTTPS / TLS 1.3]
* Claims Processor -> Message Broker: Publishes domain events [SASL/SCRAM over TLS]
* Message Broker -> Payment Reconciliation Worker: Consumes payment events [SASL/SCRAM over TLS]
* Billing Components -> Billing Data Repository: Queries and persists data [TCP]

## Technology Stack
* Node.js / TypeScript: Core runtime for the Billing Service ensuring modern asynchronous performance.
* Express.js: Web framework for handling HTTP routing in the Invoice Controller.
* TypeORM: Object-Relational Mapper for structured data access via PgBouncer.
* Apache Kafka: Event broker for reliable asynchronous messaging.
* PostgreSQL: Relational storage meeting ACID and retention requirements.

## Rationale
[This architecture uses containerized microservices and active-active deployments to guarantee 99.99% uptime and high performance.]
[Dedicated audit logging, encryption, and circuit breakers ensure strict HIPAA/GDPR compliance and resilience against external gateway failures.]