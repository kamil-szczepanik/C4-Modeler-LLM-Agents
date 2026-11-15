## Overview
- Scaled-down Amazon-style e-commerce site supporting physical and electronic book sales, reviews, and recommendations.
- Built for 1M MAU with 99.95% uptime, sub-2s 3G page loads, and global compliance (GDPR/CCPA, multi-currency).

## Key Elements
- Users: Customers and Admins
- External Systems: Global Edge Layer (CloudFront, Route 53, WAF), Stripe/PayPal, FedEx/UPS, SendGrid/AWS SES, Fixer/Open Exchange Rates
- Containers: React SPA, API Gateway, Catalog Service, Order & Checkout Service, Recommendation Service, Privacy/Compliance Service, Notification Service, Review Service, Analytics Ingestion Pipeline
- Order & Checkout Service Components: Order Management, Payment Orchestration, Fulfillment Integration, Outbox Event Publisher
- Data & Infrastructure: Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon ElastiCache Redis, Amazon SQS/SNS, AWS App Mesh, Amazon ECS Fargate

## Relationships
- Global Edge Layer -> React SPA: Delivers static frontend assets [HTTPS]
- React SPA -> API Gateway: Routes client requests [HTTPS / GraphQL]
- API Gateway -> Order & Checkout Service: Routes checkout requests [gRPC over HTTP/2 via AWS App Mesh with mTLS]
- Order Management -> Payment Orchestration: Internal method calls [Java]
- Payment Orchestration -> Stripe/PayPal: Processes payments [HTTPS with TLS 1.3]
- Fulfillment Integration -> FedEx/UPS: Generates shipping labels [HTTPS]
- Order Management -> Amazon Aurora PostgreSQL: Persists transactional state and audit trails [PostgreSQL Wire Protocol via HikariCP]
- Outbox Event Publisher -> Amazon SQS: Publishes asynchronous fulfillment messages [AWS SDK]
- SQS -> Fulfillment Integration: Asynchronously triggers fulfillment processing [AWS SQS Protocol]
- Payment Orchestration -> Amazon ElastiCache Redis: Stores idempotency keys [Redis Wire Protocol with TLS]

## Technology Stack
- Compute: Amazon ECS Fargate for containerized microservices scalability
- Backend Framework: Spring Boot / Java for core business services
- Communication: gRPC over HTTP/2 via AWS App Mesh for secure internal service-to-service calls
- Database: Amazon Aurora PostgreSQL for ACID-compliant transactional data and outbox pattern
- Caching & State: Amazon ElastiCache Redis for distributed idempotency key management
- Messaging: Amazon SQS with DLQs for decoupled, resilient asynchronous fulfillment workflows
- Security: AWS KMS for encryption-at-rest (PII/Aurora/SQS), AWS Secrets Manager for credentials, and AWS WAF

## Rationale
- Decouples synchronous checkout from third-party shipping APIs using Amazon SQS and transactional outboxes to guarantee 99.95% uptime.
- Enforces strict security, idempotency, and data protection controls to satisfy GDPR/CCPA mandates, PCI-DSS scope reduction, and 3G resilience requirements.