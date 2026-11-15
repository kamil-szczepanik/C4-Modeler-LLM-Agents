## Overview
- Scaled-down Amazon-style e-commerce system built on AWS to support book sales, reviews, and recommendations.
- Designed for high scalability (1M MAU), strict security, and global performance across multiple regions.

## Key Elements
- Single Page Application (React, TypeScript) hosted on Amazon S3 and distributed via Amazon CloudFront.
- API Gateway with Lambda Authorizer acting as the single secure entry point.
- Catalog Service (Node.js/Express), Order & Checkout Service (Spring Boot), Recommendation Service (Python/FastAPI), and Review & Notification Service.
- Message Broker using Amazon SNS and SQS for asynchronous event-driven workflows.
- Managed Data Tier: Amazon Aurora PostgreSQL (database-per-service), Amazon OpenSearch Service, and Amazon Redis.

## Relationships
- Customer/SPA to API Gateway: HTTPS / REST
- API Gateway to Microservices: HTTPS / REST via internal Application Load Balancers
- Microservices to Datastores: Native TCP/TLS drivers (PostgreSQL wire protocol, Redis RESP, OpenSearch REST API)
- Microservices to Message Broker: JSON event publishing/consumption via Amazon SNS/SQS
- External Integration: HTTPS with third-party payment (Stripe/PayPal), tax (Avalara/TaxJar), and shipping (FedEx/UPS) APIs

## Technology Stack
- AWS Cloud: Hosting and infrastructure backbone for multi-region availability (us-east-1, eu-west-1, ap-southeast-1).
- React/TypeScript & S3/CloudFront: Ensures global sub-2-second page loads.
- Polyglot Containers (Node.js, Spring Boot, FastAPI): Matches specific workload requirements for catalog, orders, and AI recommendations.
- Amazon Aurora, OpenSearch, & Redis: Provides isolated data boundaries for GDPR compliance and sub-second search/reads.

## Rationale
- This decoupled container architecture guarantees independent horizontal scalability to handle 1M MAU while meeting 99.95% uptime targets.
- Strict database isolation and AWS Cognito/IAM integration ensure robust GDPR, CCPA, and OWASP Top-10 security compliance.