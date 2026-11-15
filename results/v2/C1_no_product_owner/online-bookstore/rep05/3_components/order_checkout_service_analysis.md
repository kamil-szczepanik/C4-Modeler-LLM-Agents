## Overview
[The Online Bookstore system provides a scalable e-commerce platform for purchasing physical and electronic books with integrated reviews and recommendations. The Order & Checkout Service manages secure, multi-step transactions, shopping carts, and external fulfillment workflows.]

## Key Elements
- Cart Management Component (Spring Bean / Redis Client)
- Checkout Orchestrator (Spring State Machine / Saga pattern with Resilience4j)
- Order Processing Component (Spring Data JPA)
- Event Publisher Component (Spring Cloud Stream)
- External Systems: Stripe, Avalara, FedEx/UPS Shipping APIs
- Data Stores: Amazon ElastiCache (Redis), Amazon RDS (PostgreSQL)
- Messaging: Amazon EventBridge, SQS, SNS

## Relationships
- Cart Management Component -> Amazon ElastiCache (Redis): Reads/writes cart sessions [Redis Protocol over TLS]
- Checkout Orchestrator -> Amazon RDS (PostgreSQL): Persists workflow state [JDBC over TLS]
- Checkout Orchestrator -> Stripe, Avalara, Shipping APIs: Executes payments, tax calculations, and fulfillment [HTTPS / REST]
- Order Processing Component -> Amazon RDS (PostgreSQL): Commits final order line items [Spring Data JPA over TLS]
- Event Publisher Component -> Amazon EventBridge / SQS: Emits asynchronous `OrderPlaced` domain events [AWS SDK v2 over HTTPS]

## Technology Stack
- Spring Boot (Java): Chosen for mature ecosystem, Spring State Machine, and Spring Cloud Stream to orchestrate reliable ACID-compliant checkout workflows.
- AWS ECS (Fargate): Provides serverless, elastic container execution.
- Amazon RDS (PostgreSQL): Ensures durable persistence for transactional orders and externalized state machine states.
- Amazon ElastiCache (Redis): Delivers low-latency shopping cart and session management.
- Resilience4j: Implements circuit breakers for unreliable third-party APIs.

## Rationale
[This architecture ensures high availability (99.95% uptime) and scalability to support 1 million MAU while enforcing strict PCI-DSS and GDPR compliance. Offloading tokenization to Stripe and externalizing state guarantees transactional integrity during distributed failures.]