## Overview
This architecture defines the Order & Checkout Service container for the Online Bookstore, a Spring Boot application handling secure multi-currency transactions and order processing. It ensures strict PCI-DSS boundaries, GDPR/CCPA compliance, and 99.95% availability on AWS.

## Key Elements
- **Checkout Orchestrator Component**: Manages multi-step checkout workflows and distributed transaction sagas using Spring `@Service`.
- **Payment Integration Component**: Handles tokenized payment interactions with the external Payment Gateway.
- **Fulfillment Client Component**: Integrates with third-party Shipping Provider APIs for label generation and tracking.
- **Order Repository Component**: Interfaces with data persistence using Spring Data JPA.
- **Event Publisher Component**: Dispatches asynchronous domain events via Spring Cloud Stream and AWS SDK.

## Relationships
- **AWS API Gateway -> Checkout Orchestrator Component**: Routes order requests via gRPC over mTLS and ECS Service Connect, validating inbound JWTs.
- **Checkout Orchestrator Component -> Payment Integration Component**: Invokes payment processing synchronously via direct Java method calls.
- **Checkout Orchestrator Component -> Fulfillment Client Component**: Invokes fulfillment operations synchronously via direct Java method calls.
- **Order Repository Component -> Amazon Aurora PostgreSQL**: Persists order and transaction data using TCP/TLS.
- **Event Publisher Component -> AWS EventBridge / SQS**: Publishes asynchronous domain events via HTTPS.

## Technology Stack
- **Spring Boot**: Core framework for building the microservice container and internal components.
- **Amazon ECS Fargate**: Serverless container execution platform for running the service.
- **Amazon Aurora PostgreSQL**: Relational database for ACID-compliant order data persistence.
- **Resilience4j**: Implements circuit breaking and timeouts for third-party API calls.
- **HikariCP**: Manages database connection pooling to prevent starvation.
- **AWS KMS & Secrets Manager**: Handles encryption keys and runtime secret injection.

## Rationale
Decomposing the service into focused Spring components ensures high internal cohesion while isolating third-party payment and shipping risks. This modularity, combined with robust resilience patterns and tokenization, directly satisfies scalability, security, and PCI-DSS compliance constraints.