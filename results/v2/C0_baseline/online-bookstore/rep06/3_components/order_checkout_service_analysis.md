## Overview
The Order & Checkout Service is a cloud-native component of the Online Bookstore that handles ACID-compliant order processing, payment integration, and checkout orchestration. It ensures secure, resilient financial transactions across multiple global regions.

## Key Elements
- **Checkout Orchestrator Component**: Spring Boot / Spring State Machine managing distributed transaction sagas and idempotent API calls.
- **Order Management API Component**: Spring MVC/REST exposing secure endpoints for Customer Support Agent refunds and cancellations.
- **Order Persistence Component**: Spring Data JPA managing relational data against AWS RDS PostgreSQL.
- **Event Publisher Component**: Spring Cloud Stream / AWS SDK dispatching asynchronous events to AWS EventBridge.
- **External Systems**: Payment Gateway, Third-Party Shipping APIs, Tax & Compliance Service, and AWS Secrets Manager.

## Relationships
- Checkout Orchestrator -> Payment Gateway, Shipping APIs, Tax Service [HTTPS / REST API]
- Checkout Orchestrator -> Order Persistence Component [JPA/JDBC over TLS]
- Order Management API -> Order Persistence Component [JPA/JDBC over TLS]
- Checkout Orchestrator & Order Management API -> Event Publisher Component [In-process Spring Events]
- Event Publisher Component -> AWS EventBridge [HTTPS / AWS SDK]

## Technology Stack
- **Java / Spring Boot**: Chosen for enterprise maturity, robust transaction management, and ecosystem support.
- **AWS RDS PostgreSQL**: Provides strict ACID compliance and relational integrity for financial data.
- **AWS ECS Fargate**: Enables scalable, serverless container execution across multiple AWS regions.
- **AWS EventBridge / SQS**: Decouples domain event publishing (`OrderPlaced`, `AbandonedCheckout`) with dead-letter queue support.
- **AWS Secrets Manager & KMS**: Ensures zero hardcoded secrets and robust envelope encryption for PII at rest.

## Rationale
This architecture guarantees 99.95% uptime and 1 M MAU scalability by decoupling core checkout sagas from downstream messaging via asynchronous event publishing. It strictly enforces PCI-DSS, GDPR, and OWASP security controls through zero credit card persistence, IAM least-privilege roles, and idempotency keys.