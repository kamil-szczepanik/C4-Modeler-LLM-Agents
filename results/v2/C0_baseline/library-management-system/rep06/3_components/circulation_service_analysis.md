## Overview
[The Circulation Service is a core Spring Boot container within the Library Management System responsible for managing borrowing workflows, renewals, and fine processing. It ensures secure, resilient, and EU-compliant circulation operations for public and academic libraries.]

## Key Elements
* Circulation API Controller (Spring `@RestController`)
* Loan Management Component (Spring `@Service`)
* Fine & Fee Component (Spring `@Service`)
* Data Access Repository (Spring Data JPA)
* Event Publisher/Consumer (Spring Cloud Stream / Kafka)
* Notification Event Adapter (Spring `@Component`)
* External Payment Gateway and Managed PostgreSQL Database

## Relationships
* API Gateway -> Circulation API Controller: Routes patron self-service and staff requests [gRPC and internal REST over mTLS]
* Circulation API Controller -> Loan & Fine Components: Executes business logic with JWT-based RBAC enforcement
* Data Access Repository -> Managed Databases: Queries and persists transactional data [private VPC with AES-256 encryption]
* Fine & Fee Component -> Payment Gateway: Processes fine payments and tokenized references [REST APIs over TLS 1.3 with Resilience4j circuit breakers]
* Event Publisher/Consumer -> Event Broker: Publishes domain events [Kafka protocol with `acks=all` and W3C Trace Context headers]

## Technology Stack
* Java / Spring Boot: Core container framework for modular internal service design
* Spring Data JPA & PostgreSQL: Relational persistence ensuring transactional consistency and EU-only data residency
* Resilience4j: Circuit breaking and retries for external payment gateway integration
* Apache Kafka & Spring Cloud Stream: Asynchronous messaging with idempotent producers for event-driven decoupled architecture
* OpenTelemetry: Distributed tracing across API requests and asynchronous event flows

## Rationale
[This architecture cleanly separates synchronous loan transactions from asynchronous notifications while enforcing strict GDPR data minimization and security controls. Incorporating circuit breakers, resilient messaging, and RBAC guarantees high availability and regulatory compliance for financial and patron data.]