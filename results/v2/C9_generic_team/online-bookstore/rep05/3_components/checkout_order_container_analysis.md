## Overview
The Checkout & Order Container is an AWS-hosted microservice responsible for secure financial transactions, order processing, and third-party logistics integrations for the online bookstore. It ensures high availability, multi-currency support, and strict transactional integrity for global e-commerce operations.

## Key Elements
- Checkout & Order Container (AWS ECS/EKS)
- Dedicated Data Store (PostgreSQL with ACID compliance)
- External Payment Gateway
- Tax Calculation Service
- Third-Party Shipping Provider
- Currency Exchange Rate Service
- Background Worker / Job Processing Container (AWS SQS/SNS with Dead Letter Queue)
- Web Application / API Gateway (Envoy Proxy)

## Relationships
- Web Application / API Gateway -> Checkout & Order Container: Routes checkout and order requests [gRPC/REST over TLS]
- Checkout & Order Container -> Payment Gateway: Authorizes and processes financial transactions [HTTPS]
- Checkout & Order Container -> Tax Calculation Service: Computes regional taxes [HTTPS]
- Checkout & Order Container -> Third-Party Shipping Provider: Initiates fulfillment and shipping [HTTPS]
- Checkout & Order Container -> Currency Exchange Rate Service: Fetches conversion rates [HTTPS]
- Checkout & Order Container -> Background Worker / Job Processing Container: Publishes asynchronous tasks and events [AWS SQS/SNS]

## Technology Stack
- AWS ECS/EKS: Container orchestration platform for scalable, multi-region deployment
- PostgreSQL: ACID-compliant relational database ensuring strict consistency for financial transactions and order states
- OpenTelemetry: Distributed tracing standard for monitoring synchronous and asynchronous execution paths
- AWS SQS/SNS: Asynchronous messaging backbone for decoupled background job processing and event distribution
- Pact: Automated contract testing framework to prevent breaking schema changes in CI/CD pipelines

## Rationale
This architecture uses transactional outboxes, idempotency keys, and the Saga pattern to guarantee financial accuracy and reliable error recovery across distributed third-party APIs. The combination of ACID storage, circuit breakers, and graceful degradation directly fulfills the 99.95% uptime and scalability requirements.