## Overview
The Order & Checkout Service manages secure, multi-currency transactions, shopping carts, and order fulfillment for the Online Bookstore. It ensures high-availability ACID compliance and integrates with external payment and shipping gateways.

## Key Elements
- **Checkout Controller**: Exposes REST/GraphQL endpoints via mTLS.
- **Order Management Manager**: Handles domain logic, state transitions, and cart mapping.
- **Payment Client & Shipping Client**: Integrates with external gateways using Resilience4j circuit breakers.
- **Order Repository**: Manages data persistence via Spring Data JPA.
- **Domain Event Mapper**: Transforms JPA entities into versioned event schemas.
- **Event Publisher**: Publishes messages to the Messaging Bus.
- **Amazon Aurora (PostgreSQL)**: Stores transactional order data using Outbox Pattern tables.
- **Amazon ECS (Fargate)**: Hosts the containerized microservice.

## Relationships
- **API Gateway -> Checkout Controller**: Routes secure client requests [REST/GraphQL via mTLS over HTTPS]
- **Order Management Manager -> Payment Client**: Executes payment processing [REST/JSON over HTTPS]
- **Order Management Manager -> Shipping Client**: Integrates for order fulfillment [REST/SOAP over HTTPS]
- **Order Repository -> Amazon Aurora (PostgreSQL)**: Persists transactional data [Dedicated database driver with AWS KMS encryption]
- **Event Publisher -> Amazon Messaging Bus**: Publishes asynchronous order events [SQS/SNS protocols]

## Technology Stack
- **Java (Spring Boot)**: Provides robust enterprise framework for domain logic and dependency injection.
- **Amazon Aurora (PostgreSQL)**: Ensures ACID compliance and multi-region read scaling via Global Databases.
- **Amazon ECS (Fargate)**: Enables serverless container orchestration and auto-scaling.
- **Resilience4j**: Prevents cascading failures during external gateway outages.
- **AWS Secrets Manager**: Secures runtime credential injection and automated rotation.

## Rationale
This architecture ensures 99.95% uptime and low latency for 1M MAU through multi-region ECS and Aurora Global Databases. The Outbox Pattern guarantees reliable messaging without compromising transactional integrity.