## Overview
An AWS-based online bookstore system handling 1 million monthly active users with multi-region deployment. It provides scalable book browsing, secure checkout, and real-time recommendations.

## Key Elements
- **Users**: Customers, Book Authors/Publishers, Customer Support Agents, Shipping Partners, Site Administrators
- **Client Tier**: Single-Page Application using React, hosted on Amazon S3, distributed via Amazon CloudFront
- **API & Routing Tier**: AWS API Gateway, Envoy Service Mesh using SPIFFE/SPIRE
- **Core Services**: Catalog Service, Order & Checkout Service, Recommendation Service, Customer Service, Admin & Support Service (all running on AWS ECS on Fargate in Node.js, Spring Boot, Python FastAPI, and Go)
- **Data & Messaging Tier**: Amazon Aurora PostgreSQL with AWS KMS, Amazon ElastiCache (Redis), Amazon S3, Amazon EventBridge with custom bus `store-domain-events`, Amazon SQS, Amazon EventBridge Schema Registry

## Relationships
- **Client Tier to API Gateway**: HTTPS / TLS 1.3
- **API Gateway to Envoy Service Mesh**: gRPC / mTLS
- **Services to Database**: TCP / PostgreSQL protocol
- **Order & Checkout Service to Amazon EventBridge**: Publishes domain events via AWS SDK / HTTPS, TLS 1.3
- **Amazon EventBridge to Amazon SQS**: Delivers matched events via AWS API / HTTPS
- **Amazon EventBridge to Amazon S3 (`store-event-archive`)**: Archives domain events via AWS API / HTTPS, TLS 1.3

## Technology Stack
- **Compute**: AWS ECS on Fargate for containerized microservices scaling without server management
- **Messaging & Integration**: Amazon EventBridge for event-driven decoupled architecture and Amazon SQS for reliable message queuing
- **Databases**: Amazon Aurora PostgreSQL for relational storage with AWS KMS encryption and Amazon ElastiCache (Redis) for caching
- **Storage**: Amazon S3 with S3 Object Lock and S3 Lifecycle policies for static assets and compliance audit logging

## Rationale
AWS ECS on Fargate and Amazon EventBridge ensure elasticity and decoupling to handle 1M MAU and 99.95% availability. Customer-managed AWS KMS encryption and schema validation satisfy GDPR, CCPA, and security requirements.