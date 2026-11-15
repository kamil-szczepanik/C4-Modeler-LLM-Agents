## Overview
An online bookstore system handling catalogue browsing, secure checkout, reviews, and recommendations for 1M MAU. It uses AWS cloud services with decoupled asynchronous messaging for scalability and high availability.

## Key Elements
- Customers, Reviewers, and Store Administrators (Users)
- Single-Page Application (SPA) & Admin Back-Office App (React on Amazon S3 / CloudFront)
- API Gateway (Amazon API Gateway)
- Core Services & Recommendation Engine (Node.js/NestJS and Python/FastAPI on Amazon ECS Fargate)
- Notification Worker & Analytics Ingestion Container (Amazon ECS Fargate)
- Data Storage (Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon S3)
- Messaging & Integration (Amazon EventBridge, Amazon SQS)
- External Systems (Payment Gateway, Third-Party Shipping Provider, Tax & Compliance Service, Email/Notification Service)

## Relationships
- Customer -> SPA: Browses catalogue, manages cart, places orders [HTTPS]
- SPA -> API Gateway: Routes client requests [HTTPS/JSON]
- API Gateway -> Core Services: Forwards API requests [REST/gRPC]
- Core Services -> Amazon Aurora PostgreSQL & Amazon DynamoDB: Persists transactional and user data [TCP/TLS]
- Core Services -> Amazon EventBridge (`bookstore-domain-bus`): Publishes asynchronous domain events (`OrderPlaced`, `InventoryUpdated`) [AWS SDK, HTTPS/JSON, TLS 1.2+, SigV4]
- Amazon EventBridge -> Amazon SQS (Dead-Letter Queues): Dispatches filtered events and handles failed invocations [HTTPS]
- Amazon SQS -> Notification Worker & Third-Party Shipping Provider: Triggers fulfillment and notification tasks [HTTPS]

## Technology Stack
- Frontend: React hosted on Amazon S3 and CloudFront for fast global content delivery
- Backend Services: Node.js/NestJS and Python/FastAPI running on Amazon ECS (Fargate) for scalable container orchestration
- Datastores: Amazon Aurora PostgreSQL (Multi-AZ) for ACID-compliant transactional data and Amazon DynamoDB for scalable key-value data
- Messaging: Amazon EventBridge with custom buses, Schema Registry validation, and Amazon SQS DLQs for asynchronous decoupling
- Security & Compliance: AWS KMS (Customer Managed Keys with 90-day rotation), AWS IAM least-privilege policies, and TLS 1.2+ for GDPR/CCPA compliance

## Rationale
This architecture uses event-driven microservices on AWS Fargate and EventBridge to guarantee 99.95% uptime and sub-2-second page loads under high concurrency. Decoupling core workflows with managed message queues ensures robust scalability for 1M MAU while strictly enforcing regulatory compliance and multi-region resilience.