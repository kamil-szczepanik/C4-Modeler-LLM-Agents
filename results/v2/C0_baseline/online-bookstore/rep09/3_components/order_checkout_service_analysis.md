## Overview
The Online Bookstore system is a scalable e-commerce platform for purchasing physical and electronic books with reviews and recommendations. The architecture leverages AWS multi-region infrastructure to ensure secure, high-availability transactions and GDPR compliance.

## Key Elements
- **Users**: Book Buyer / Registered Reviewer, Store Administrator
- **External Systems**: Payment Gateway Provider, Shipping Provider APIs, Identity Provider / Notification Service, Recommendation Engine, Tax & Localization API
- **Containers**: Single Page Application (React / TypeScript), API Gateway (AWS API Gateway), Catalogue Service (Node.js, Amazon OpenSearch), Order & Checkout Service (Java Spring Boot, Amazon Aurora PostgreSQL), Recommendation & Review Service (Python FastAPI, Amazon SQS/SNS)
- **Order & Checkout Internal Components**: Checkout Orchestrator Component, Payment Integration Component, Fulfillment Client Component, Order Repository Component, Notification Publisher Component

## Relationships
- API Gateway -> Order & Checkout Service: Routes order and transaction requests [TLS 1.3 and gRPC]
- Order & Checkout Service -> Amazon Aurora PostgreSQL: Executes transactional queries [JDBC with AWS KMS encryption]
- Order & Checkout Service -> Payment Gateway Provider: Processes payments [Outbound HTTPS with mTLS and Resilience4j circuit breakers]
- Order & Checkout Service -> Shipping Provider APIs: Dispatches shipping orders [Outbound HTTPS with mTLS]
- Order & Checkout Service -> Identity Provider / Notification Service: Triggers order confirmation emails [Amazon SNS/SQS with encrypted payloads]
- Order & Checkout Service -> Amazon EventBridge: Emits business telemetry events [Asynchronous JSON events]

## Technology Stack
- **Compute & Deployment**: AWS ECS (Fargate) with blue/green deployments via AWS CodeDeploy for zero-downtime releases.
- **Backend Framework**: Java Spring Boot utilizing Spring State Machine for Saga pattern execution.
- **Database**: Amazon Aurora PostgreSQL with Aurora Global Databases and cross-region read replicas.
- **Messaging & Events**: Amazon SQS/SNS with Dead-Letter Queues (DLQs) and Amazon EventBridge.
- **Security & Secrets**: AWS Secrets Manager, AWS KMS for PII column-level encryption, OAuth2/JWT token validation.
- **Observability**: OpenTelemetry auto-instrumentation, Amazon CloudWatch, and AWS X-Ray.

## Rationale
This architecture uses containerized microservices on AWS ECS Fargate to scale effortlessly and handle 1M MAU. Multi-region Aurora PostgreSQL deployment and decoupled event-driven messaging via SNS/EventBridge guarantee high availability (99.95% uptime) while maintaining stringent GDPR and CCPA security compliance.