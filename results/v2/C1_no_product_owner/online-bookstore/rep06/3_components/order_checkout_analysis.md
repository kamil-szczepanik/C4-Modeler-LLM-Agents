## Overview
The Online Bookstore's Order & Checkout container manages shopping carts, checkout sagas, and order processing. It uses a decomposed Spring Boot microservices architecture on AWS ECS Fargate to ensure high availability and scalability.

## Key Elements
- **Cart Manager**: Manages ephemeral shopping cart and session state
- **Checkout Orchestrator**: Coordinates payment and fulfillment workflows
- **Order Processor**: Handles persistent order state and domain events
- **Amazon DynamoDB**: Stores cart and session data
- **Amazon Aurora PostgreSQL**: Stores transactional order data via AWS RDS Proxy
- **Payment Gateway & Shipping Provider APIs**: External financial and logistics systems

## Relationships
- **API Gateway / ALB -> Checkout Orchestrator / Cart Manager**: Ingress requests via HTTPS / AWS Cloud Map
- **Checkout Orchestrator -> Cart Manager**: Cart item retrieval via gRPC (Protobuf over HTTP/2) with mTLS
- **Checkout Orchestrator -> Payment Gateway & Shipping Providers**: Processes payments and fulfillment via HTTPS/REST
- **Order Processor -> Amazon Aurora PostgreSQL**: Persists order data via TLS-encrypted JDBC / AWS RDS Proxy
- **Cart Manager -> Amazon DynamoDB**: Reads/writes cart state via AWS SDK (TLS)
- **Order Processor -> Message Bus**: Publishes asynchronous events via AWS SQS/SNS

## Technology Stack
- **Compute**: Amazon ECS Fargate for containerized Spring Boot components
- **Databases**: Amazon Aurora PostgreSQL (ACID orders) and Amazon DynamoDB (carts/sessions)
- **Database Proxy**: AWS RDS Proxy for connection pooling and draining
- **Internal Communication**: gRPC over HTTP/2 with mTLS for low-latency cart retrieval
- **Security & Secrets**: AWS Secrets Manager, AWS IAM, and client-side tokenization for PCI-DSS compliance

## Rationale
This architecture isolates high-velocity cart operations from ACID-compliant financial transactions to protect uptime goals. Decoupling orchestration from persistence guarantees low-latency checkouts and robust third-party failure resilience.