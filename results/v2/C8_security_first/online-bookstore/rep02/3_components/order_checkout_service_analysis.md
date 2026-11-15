## Overview
The Order & Checkout Service manages secure shopping cart states, financial transactions, and fulfillment processing for the Online Bookstore. It ensures high availability, multi-currency support, strict GDPR/CCPA compliance, and idempotency across global AWS regions.

## Key Elements
- Shoppers / Customers
- React Single Page Application (SPA)
- AWS API Gateway & Edge Lambda
- Order & Checkout Service (Java 21, Spring Boot)
- Cart Component (Redis-backed)
- Checkout Orchestrator & Idempotency Manager
- Payment Integration Component & Fulfillment Component
- Order Repository & Amazon Aurora PostgreSQL
- External Payment Gateway & Third-Party Shipping APIs

## Relationships
- AWS API Gateway & Edge Lambda -> Order & Checkout Service: Routes order and checkout requests [gRPC over mTLS with JWT]
- Order & Checkout Service -> Payment Gateway: Processes financial transactions and payment captures [HTTPS with TLS 1.3]
- Order & Checkout Service -> Third-Party Shipping APIs: Transmits fulfillment data [HTTPS with TLS 1.3]
- Order & Checkout Service -> Amazon SQS: Queues asynchronous fulfillment data [AWS SDK over HTTPS]
- Order & Checkout Service -> Amazon Aurora PostgreSQL: Persists orders and state [JDBC via AWS RDS Proxy]
- Order & Checkout Service -> Amazon Redis: Manages cart state and idempotency keys [Redis Protocol]

## Technology Stack
- Java 21 & Spring Boot: Core framework for business logic and component orchestration
- Amazon Aurora PostgreSQL & Redis: Primary data store and distributed cache for cart/idempotency state
- AWS ECS (Fargate) & Application Load Balancer: Multi-region container hosting in `us-east-1`, `eu-west-1`, and `ap-southeast-1`
- AWS SQS & Dead Letter Queues: Asynchronous message queuing for resilient third-party shipping integration
- AWS KMS & Secrets Manager: Data-at-rest encryption (AES-256), PII masking, and secure credential management

## Rationale
This architecture uses containerized microservices deployed across multi-region AWS infrastructure to achieve the required 99.95% uptime and low-latency global performance. Incorporating Redis-backed idempotency, database connection pooling, and asynchronous outbox queues guarantees financial integrity and fault tolerance against third-party outages.