## Overview
Modular monolithic architecture for the Core E-Commerce Container built with Node.js and TypeScript on Amazon ECS with AWS Fargate. It manages catalogue browsing, secure shopping carts, order fulfillment, and notifications while adhering to high-availability and compliance standards.

## Key Elements
- **Catalogue Component**: NestJS module managing product browsing and search via TypeORM.
- **Cart & Checkout Component**: NestJS module handling ephemeral cart states and tokenized payment processing.
- **Order Fulfillment Component**: Manages order state transitions and third-party logistics integration.
- **Customer Notification Component**: Handles transactional communications via AWS SES.
- **Data Stores**: Amazon Aurora PostgreSQL, Amazon DynamoDB, and Amazon ElastiCache Redis.

## Relationships
- API Gateway -> Core E-Commerce Container via gRPC / HTTPS
- Core E-Commerce Container -> Amazon Aurora PostgreSQL via PostgreSQL wire protocol
- Core E-Commerce Container -> Amazon DynamoDB via DynamoDB API
- Core E-Commerce Container -> Amazon ElastiCache Redis for cart state management
- Core E-Commerce Container -> Stripe/PayPal via Outbound HTTPS/REST
- Core E-Commerce Container -> FedEx/UPS via Outbound HTTPS/REST
- Core E-Commerce Container -> AWS SES via Outbound HTTPS/API
- Core E-Commerce Container -> Amazon SQS/SNS via asynchronous event publishing

## Technology Stack
- **Node.js / TypeScript**: Core runtime language providing rapid feature delivery and unified backend tooling.
- **NestJS**: Modular framework enforcing strict directory-level boundaries and dependency injection.
- **Amazon ECS with AWS Fargate**: Serverless container orchestration for scalable, isolated execution.
- **Amazon ElastiCache Redis**: Low-latency, ephemeral storage for cart session management and seamless user login merges.
- **AWS Secrets Manager**: Secure runtime injection and rotation of database credentials and API keys.

## Rationale
Modular NestJS design within a single Fargate runtime minimizes initial operational complexity while maintaining strict internal boundaries for future microservice extraction. Integrated resilience patterns, tokenized payments, and OpenTelemetry instrumentation satisfy strict performance, multi-currency, and compliance requirements.