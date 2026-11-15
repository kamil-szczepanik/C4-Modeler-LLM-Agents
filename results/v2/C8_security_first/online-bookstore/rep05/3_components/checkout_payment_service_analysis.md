## Overview
The Checkout & Payment Service processes secure, multi-currency transactions and order fulfillment for the Online Bookstore. It ensures PCI-DSS compliance, high availability (99.95%), and low-latency performance using resilient cloud-native components.

## Key Elements
- **Users**: Customers, Store Administrators
- **External Systems**: Stripe / PayPal, FedEx / UPS, AWS Cognito / Auth0, AWS SES / SendGrid
- **Containers**: Single Page Application, Amazon CloudFront / API Gateway / ALB, Checkout & Payment Service (ECS Fargate), Recommendation Service, Catalog & Search Service, Amazon Aurora PostgreSQL Global Database, Amazon SQS / SNS
- **Components (Checkout & Payment Service)**: Cart Manager, Checkout Orchestrator, Payment Gateway Adapter, Fulfillment Integration Component

## Relationships
- *API Gateway* -> *Checkout Orchestrator* [HTTPS, gRPC / mTLS]
- *Checkout Orchestrator* -> *Cart Manager* [Redis protocol / In-memory]
- *Checkout Orchestrator* -> *Payment Gateway Adapter* & *Fulfillment Integration Component* [Internal Function Call]
- *Checkout Orchestrator* -> *Amazon Aurora PostgreSQL Global Database* [SQL over TLS]
- *Payment Gateway Adapter* -> *Stripe / PayPal* [HTTPS]
- *Fulfillment Integration Component* -> *FedEx / UPS* [HTTPS]
- *Fulfillment Integration Component* -> *Amazon SQS / SNS* [AWS SDK / AMQP]

## Technology Stack
- **Compute**: Go, AWS ECS Fargate for lightweight, scalable container execution.
- **Data & Caching**: Amazon Aurora PostgreSQL Global Database, Redis for distributed locking and cart persistence.
- **Security & Secrets**: AWS KMS, AWS Secrets Manager, OAuth2/OIDC via AWS Cognito/Auth0.
- **Messaging & Observability**: Amazon SQS / SNS, AWS X-Ray/OpenTelemetry for distributed tracing.

## Rationale
This architecture uses Go and ECS Fargate for high performance and rapid scaling to handle 1M MAU. Component isolation, tokenization, and multi-region deployment guarantee strict GDPR/PCI-DSS compliance and 99.95% availability.