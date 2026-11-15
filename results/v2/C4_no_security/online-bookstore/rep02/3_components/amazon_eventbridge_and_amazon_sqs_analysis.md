## Overview
The Online Bookstore is a scaled-down, multi-region e-commerce platform designed to support 1 million monthly active users with high availability. It provides secure book browsing, purchasing, reviews, and recommendations while maintaining GDPR and CCPA compliance.

## Key Elements
- **Users**: Book Shopper, Book Author/Publisher, Store Administrator
- **External Systems**: Stripe/PayPal, FedEx/UPS, AWS SES, AWS Cognito/Auth0, AWS CloudFront/Route 53, AWS CloudWatch/Datadog
- **Containers**: React SPA (AWS S3), API Gateway, Catalog & Search Service, Order & Checkout Service, Personalization Service, Customer Review Service, Notification Service
- **Data & Messaging Storage**: Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon OpenSearch, Redis (ElastiCache), Amazon EventBridge, Amazon SQS
- **EventBridge Components**: Central Event Bus, Event Payload Sanitizer / Tokenizer, Order Processing Queue, Notification Queue, SQS Dead-Letter Queues (DLQs)

## Relationships
- `React SPA` -> `API Gateway`: Routes HTTPS REST/GraphQL requests [HTTPS / TLS 1.3]
- `Order & Checkout Service` -> `Central Event Bus`: Publishes order events [AWS SDK]
- `Catalog & Search Service` -> `Central Event Bus`: Publishes `BookAdded` events [AWS SDK / HTTPS]
- `Order Processing Queue` -> `Order & Checkout Service`: Delivers retryable fulfillment tasks [AWS SDK / Long Polling]
- `Central Event Bus` -> `AWS KMS`: Encrypts/decrypts event payloads at rest [AWS SDK]
- `Order & Checkout Service` -> `Stripe/PayPal`: Processes secure payments [HTTPS / REST]
- `Order & Checkout Service` -> `FedEx/UPS`: Integrates with third-party shipping APIs [HTTPS / REST]

## Technology Stack
- **Cloud Infrastructure**: AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) chosen for global reach and multi-region scalability.
- **Messaging & Eventing**: Amazon EventBridge and Amazon SQS for asynchronous microservice decoupling and fault tolerance.
- **Backend Services**: Spring Boot (Java) and Python (FastAPI/Celery) for core business logic and high-performance processing.
- **Databases**: Amazon Aurora PostgreSQL for relational data, Amazon DynamoDB for state management, Amazon OpenSearch for catalogue search, and Redis (ElastiCache) for caching.
- **Security & Compliance**: AWS KMS and EventBridge Schema Registry to enforce GDPR/CCPA data tokenization and encryption.

## Rationale
This event-driven microservices architecture guarantees 99.95% uptime and sub-2-second page loads by decoupling critical workflows through SQS queues and EventBridge. Leveraging managed AWS services with strict security controls ensures compliance, scalability under heavy traffic, and fault-tolerant multi-region operations.