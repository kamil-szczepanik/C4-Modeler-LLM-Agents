## Overview
The Checkout Container processes secure online orders, payments, and fulfillment integrations for the Amazon-style e-commerce bookstore. It ensures high availability, strict transactional consistency, and fault-tolerant communication with third-party vendors.

## Key Elements
- **Cart/Order State Manager**: Manages cart processing and core domain models
- **Payment Gateway Adapter**: Integrates with external payment providers via an Anti-Corruption Layer (ACL)
- **Fulfillment Integrator**: Interfaces with third-party shipping APIs for order delivery
- **Saga Orchestrator**: Manages distributed transactions and compensation workflows
- **Outbox Publisher & DLQ**: Handles reliable event publishing using AWS SQS/SNS and dead-letter queues

## Relationships
- **API Gateway & BFF -> Checkout Container**: Routes incoming checkout and cart requests via [HTTPS/REST]
- **Checkout Container -> Payment Gateways**: Processes secure payments using [HTTPS/REST] with Idempotency Keys
- **Checkout Container -> Third-Party Shipping APIs**: Coordinates order fulfillment via [HTTPS/REST]
- **Checkout Container -> Amazon Aurora/RDS**: Persists transactional state and outbox events via [TCP/PostgreSQL Protocol]
- **Checkout Container -> AWS SQS/SNS**: Publishes asynchronous order and fulfillment events via [AWS SDK/HTTPS]

## Technology Stack
- **Docker & Amazon ECS/EKS**: Provides containerized deployment and scalable execution across AWS regions
- **Amazon Aurora/RDS**: Relational database chosen for ACID compliance during order processing
- **AWS SQS, SNS & DLQ**: Asynchronous messaging infrastructure guaranteeing reliable outbox event delivery
- **AWS Secrets Manager**: Injects sensitive API keys and credentials at runtime securely

## Rationale
This architecture uses the Saga Pattern and Idempotency to prevent duplicate charges and maintain data integrity across distributed third-party APIs. Circuit breakers, bulkheads, and graceful shutdowns ensure 99.95% uptime and fault tolerance under high concurrency.