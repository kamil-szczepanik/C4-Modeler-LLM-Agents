## Overview
An Amazon-style e-commerce online bookstore built on AWS to support 1 million monthly active users while ensuring GDPR compliance, multi-currency processing, and high availability. It uses a decoupled containerized microservices architecture to deliver fast catalogue browsing and secure checkout.

## Key Elements
- **Client**: React Single Page Application hosted in Amazon S3 and served via Amazon CloudFront.
- **Edge**: Amazon API Gateway for routing, rate limiting, and JWT validation.
- **Core Microservices**: Catalog & Search Service (Spring Boot), Order & Checkout Service (Node.js), Payment & Currency Service (.NET Core), Recommendation & Review Service (Python), Data Privacy & User Service (Python), Admin & Content Management Service (.NET Core), and Async Worker Service (Python).
- **Data Stores & Caching**: Amazon RDS (PostgreSQL), Amazon DynamoDB, Amazon ElastiCache (Redis), and Amazon OpenSearch.
- **Messaging & Integration**: Amazon EventBridge, Amazon SQS, AWS Personalize, AWS Fraud Detector, Stripe/PayPal, Avalara, and UPS/FedEx APIs.

## Relationships
- **Client to Edge**: HTTPS requests via CloudFront to Amazon API Gateway.
- **Internal Microservices**: gRPC and HTTPS over TLS within an AWS VPC, secured by mutual TLS via ECS Service Connect.
- **Data Layer**: JDBC/SQL over TCP to Amazon RDS, NoSQL APIs to DynamoDB, and Redis protocols to ElastiCache.
- **Asynchronous Events**: Event-driven messaging via Amazon EventBridge and SQS for order processing workflows.
- **External Integrations**: HTTPS egress from backend workers to Stripe, PayPal, Avalara, UPS, FedEx, and AWS Personalize.

## Technology Stack
- **Frontend**: React (SPA) on Amazon S3 and CloudFront for global content delivery.
- **Compute**: AWS ECS with AWS Fargate for serverless container orchestration.
- **Backend Languages/Frameworks**: Spring Boot, Node.js/Express, Python (FastAPI), and .NET Core chosen for workload-specific performance.
- **Databases**: Amazon RDS (PostgreSQL) for relational data and Amazon DynamoDB for shopping carts.
- **Search & Caching**: Amazon OpenSearch for catalogue indexing and ElastiCache (Redis) for low-latency search and currency caching.

## Rationale
The containerized microservices architecture on AWS ECS/Fargate scales independently to handle 1M MAU and maintain 99.95% uptime. Decoupling core workflows with event-driven messaging and caching guarantees sub-2-second page loads and robust security compliance.