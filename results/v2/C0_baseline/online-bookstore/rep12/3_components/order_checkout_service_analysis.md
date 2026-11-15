## Overview
An Order & Checkout Service processes secure, multi-currency retail transactions and order fulfillment. It ensures strict PCI-DSS compliance, zero cardholder data storage, and high availability across global regions.

## Key Elements
- **Users & Personas:** Customer, Customer Support Agent
- **External Systems:** External Payment Gateway, External Shipping Provider
- **Containers:** Order & Checkout Service (Spring Boot, isolated private VPC)
- **Internal Components:** Checkout Orchestrator, Payment Integration Adapter, Fulfillment Adapter, Order Management API, Order Repository, Idempotency & Token Manager
- **Infrastructure:** AWS SQS, AWS ElastiCache Global Datastores, Amazon RDS PostgreSQL, AWS Secrets Manager, AWS CloudWatch

## Relationships
- API Gateway -> Order & Checkout Service: Routes checkout requests [mTLS]
- Checkout Orchestrator -> Idempotency & Token Manager: Validates idempotency [Local Method Call]
- Checkout Orchestrator -> Payment Integration Adapter: Processes payments synchronously [Spring Cloud OpenFeign / HTTPS]
- Fulfillment Adapter -> AWS SQS: Queues fulfillment handoffs asynchronously [AWS SDK / HTTPS]
- Order Management API -> Order Repository: Persists state and logs [Spring Data JPA / PostgreSQL]
- Order & Checkout Service -> External Payment Gateway: Executes secure transactions [HTTPS / TLS 1.3]

## Technology Stack
- **Java / Spring Boot:** Core framework for building resilient, modular microservices.
- **Spring Cloud OpenFeign & WebClient:** Handles synchronous payment integration and async REST calls.
- **Amazon RDS PostgreSQL:** Multi-AZ persisted storage for transactional state and audit logs.
- **AWS ElastiCache Redis:** Global datastore backing distributed idempotency checks.
- **AWS SQS:** Asynchronous message queue for decoupling fulfillment operations.
- **AWS Secrets Manager:** Secure dynamic injection and rotation of credentials and API keys.

## Rationale
The architecture isolates sensitive payment workflows within a private VPC, enforcing tokenization to eliminate PCI-DSS scope. Asynchronous queues and global caching guarantee scalability and 99.95% uptime across multi-region deployments.