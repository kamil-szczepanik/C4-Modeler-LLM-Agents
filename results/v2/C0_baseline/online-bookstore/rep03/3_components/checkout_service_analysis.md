## Overview
- Secure e-commerce checkout service for an online bookstore processing multi-currency transactions.
- Handles PCI-DSS compliant payments, tax calculations, and fulfillment coordination across three global AWS regions.

## Key Elements
- **Cart & Pricing Engine Component**: Spring Service managing localized tax calculations and pricing.
- **Payment Orchestrator Component**: Spring Integration managing Stripe/PayPal, Apple Pay, and SEPA.
- **Fulfillment Coordinator Component**: Spring Cloud OpenFeign handling FedEx/DHL shipping integrations.
- **Order Event Publisher Component**: Spring Cloud Stream emitting domain events to Amazon EventBridge.
- **Amazon Aurora (PostgreSQL)**: Transactional data store with regional read replicas.
- **AWS Secrets Manager**: Secure injection of API keys and webhook secrets.

## Relationships
- **Amazon API Gateway -> Checkout Service**: Routes checkout requests [mTLS via AWS App Mesh and internal VPC endpoints]
- **Payment Orchestrator -> Stripe/PayPal**: Processes tokenized payments and webhooks [Synchronous HTTPS with HMAC verification]
- **Fulfillment Coordinator -> FedEx/DHL**: Coordinates physical book fulfillment [REST / HTTPS]
- **Order Event Publisher -> Amazon EventBridge / SQS**: Publishes domain events (`OrderCreated`, `OrderCompleted`, `CartAbandoned`) [AMQP / Event Stream]
- **Cart & Pricing Engine -> Amazon Aurora (PostgreSQL)**: Reads and writes transactional data [TLS-encrypted connection over JDBC]

## Technology Stack
- **Java & Spring Boot**: Core language and framework for robust transactional integrity.
- **AWS ECS (Fargate)**: Container execution platform scaling across us-east-1, eu-west-1, and ap-southeast-1.
- **Resilience4j**: Circuit breaking and timeout management for unstable external APIs.
- **AWS Secrets Manager**: Dynamic secret and webhook key retrieval to enforce least-privilege security.

## Rationale
- Component decomposition isolates third-party payment and shipping failures, preserving core checkout availability.
- Asynchronous event-driven patterns with EventBridge guarantee high scalability while maintaining strict PCI-DSS scope reduction.