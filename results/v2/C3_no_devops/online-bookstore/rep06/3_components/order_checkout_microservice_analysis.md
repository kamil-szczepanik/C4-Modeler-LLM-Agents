## Overview
The Order & Checkout Microservice processes customer financial transactions, multi-currency pricing, and shipping integrations for the Online Bookstore. It ensures secure, distributed transaction orchestration while maintaining GDPR and PCI-DSS compliance.

## Key Elements
- **Shopper & Customer Support Agent**: Internal actors interacting with the checkout and order management flows.
- **Order API Controller**: Handles incoming gRPC requests and JWT-based authorization.
- **Checkout Orchestrator (Saga Coordinator)**: Manages distributed transaction workflows and transient failures.
- **Payment Processor Client**: Integrates with the Payment Gateway using tokenization.
- **Fulfillment Adapter**: Interfaces with the Third-Party Shipping Partner API.
- **Tax & Currency Evaluator**: Handles real-time USD, EUR, and GBP conversion.
- **Retry & DLQ Manager**: Manages asynchronous failure resilience.
- **Event Publisher**: Dispatches domain events to downstream services.
- **Order Repository**: Persists encrypted transaction and order data.

## Relationships
- **API Gateway -> Order API Controller**: Routes incoming checkout requests [gRPC over mTLS via AWS App Mesh]
- **Checkout Orchestrator -> Payment Processor Client**: Processes financial transactions [HTTPS REST API]
- **Checkout Orchestrator -> Fulfillment Adapter**: Sends fulfillment data [HTTPS API]
- **Checkout Orchestrator -> Tax & Currency Evaluator**: Fetches localized pricing [HTTPS REST]
- **Checkout Orchestrator -> Retry & DLQ Manager**: Offloads transient failures [AWS SQS with AWS KMS]
- **Event Publisher -> Notification Microservice**: Dispatches order state changes [AWS EventBridge / SNS]
- **Order Repository -> AWS Aurora PostgreSQL**: Persists order data [TCP with AWS KMS encryption at rest]

## Technology Stack
- **Node.js & TypeScript**: Core runtime and language for business logic execution.
- **AWS ECS Fargate**: Container orchestration platform for serverless compute.
- **AWS Aurora PostgreSQL & TypeORM**: Relational data store enforcing field-level encryption for PII.
- **AWS SQS**: Asynchronous messaging for retry queues and dead-letter handling.
- **AWS EventBridge / SNS**: Event-driven communication backbone for domain notifications.
- **AWS KMS**: Cryptographic service ensuring encryption at rest for databases and queues.

## Rationale
This component architecture uses a Saga pattern with a dedicated orchestrator and DLQ management to ensure high availability and prevent transaction loss during third-party outages. Strict data minimization and tokenization isolate sensitive PII and financial records to guarantee GDPR and PCI-DSS compliance.