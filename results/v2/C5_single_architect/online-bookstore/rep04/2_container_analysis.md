## Overview
The Online Bookstore is a scaled-down e-commerce platform for purchasing physical and electronic books with recommendations and reviews. It provides a secure, multi-currency retail experience designed to handle 1 million MAU with high availability.

## Key Elements
- Customer (Person)
- Single Page Application (React/TypeScript)
- API Gateway (AWS API Gateway)
- Catalog Service (Go)
- Order & Checkout Service (Node.js)
- Recommendation Service (Python FastAPI)
- Review Service (Java Spring Boot)
- Background Worker (AWS ECS/Lambda)
- Databases: PostgreSQL (RDS), MongoDB, Redis, Vector DB
- Message Broker (AWS SQS/SNS)
- External Systems: Payment Gateway, Shipping Provider API, Identity Provider, Notification Service, Tax Calculation Service

## Relationships
- Customer -> Single Page Application (HTTPS)
- Single Page Application -> API Gateway (HTTPS/WSS)
- API Gateway -> Core Services (gRPC/HTTP)
- Core Services -> Amazon ElastiCache (TCP)
- Order & Checkout Service -> AWS SQS (AWS SDK)
- Order & Checkout Service -> Payment Gateway & Shipping Provider API (HTTPS)

## Technology Stack
- React/TypeScript & AWS S3/CloudFront: Ensures sub-2s page loads via CDN caching.
- AWS API Gateway: Centralizes entry point, JWT validation, and OWASP rate limiting.
- Go, Node.js, Python (FastAPI), Java (Spring Boot): Polyglot backend tailored to specific workload performance needs.
- PostgreSQL, MongoDB, Redis, Vector DB: Optimized data storage for relational orders, unstructured reviews, fast caching, and AI recommendations.
- AWS SQS/SNS & ECS/Lambda: Asynchronous event-driven decoupling for shipping, notifications, and background tasks.

## Rationale
This container architecture distributes workload across specialized microservices and polyglot persistence layers to achieve massive scalability and low-latency performance. AWS managed infrastructure ensures 99.95% availability, strict compliance, and global reach across multiple regions.