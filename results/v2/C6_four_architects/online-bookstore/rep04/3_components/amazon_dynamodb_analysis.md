## Overview
The Online Bookstore system is a scalable e-commerce platform built on AWS designed to handle 1 million MAU with high availability and GDPR/CCPA compliance. It provides catalog browsing, secure checkout, 5-star reviews, and personalized recommendations across multiple currencies.

## Key Elements
- **Users**: Customers, Store Administrators
- **External Systems**: Payment Gateway, Shipping Provider APIs, Identity Provider, Tax Calculation Service, Notification Service
- **Containers**: React/TypeScript SPA, Amazon API Gateway, Node.js/ECS Catalog Service, Java/Spring Boot/ECS Order & Checkout Service, Python/FastAPI/ECS Recommendation Service, ECS Auth & Privacy Services, Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon OpenSearch, Amazon S3 & CloudFront, Amazon SNS/SQS
- **DynamoDB Components**: Request Router, DAX Cluster, Storage Node Engine, Index Manager, TTL Background Cleaner, Streams Publisher

## Relationships
- Customers -> SPA: Browse and checkout via HTTPS/TLS
- SPA -> Amazon API Gateway: REST/GraphQL API requests via HTTPS/TLS
- Order & Checkout Service -> DAX Cluster / DynamoDB: Read/Write session and cart state via AWS SDK / TCP / HTTPS
- Streams Publisher -> Amazon SNS/SQS: Asynchronous CDC event relay via HTTPS for GDPR compliance

## Technology Stack
- **Frontend**: React, TypeScript, Amazon S3, Amazon CloudFront for fast global asset delivery
- **Compute**: AWS ECS (Fargate) running Node.js, Java Spring Boot, and Python FastAPI containers
- **Databases**: Amazon Aurora PostgreSQL for relational data, Amazon DynamoDB with DAX for high-throughput carts and sessions
- **Search & Messaging**: Amazon OpenSearch for catalog search, Amazon SNS/SQS for asynchronous event-driven messaging

## Rationale
This microservices-based AWS architecture ensures horizontal scalability to support 1 million MAU and sub-2-second page loads. Managed services like DynamoDB DAX and Aurora PostgreSQL guarantee 99.95% availability while built-in CDC streams and TTL cleaners enforce GDPR and CCPA compliance.