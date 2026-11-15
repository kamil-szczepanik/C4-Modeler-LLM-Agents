## Overview
The Online Bookstore system is a scalable, cloud-native e-commerce platform designed to support global book sales, search, secure checkout, and recommendations. It delivers high performance and strict security compliance for 1 million monthly active users across multiple regions.

## Key Elements
- Customer & Administrator (Users)
- Single-Page App (SPA) container
- API Gateway (AWS API Gateway)
- Backend Services: Catalog, Order & Checkout, Recommendation, Email (Amazon ECS/Fargate)
- Databases & Caching: Amazon RDS (PostgreSQL), Amazon DynamoDB, Amazon OpenSearch, Amazon ElastiCache (Redis)
- External Systems: Payment Gateway, Shipping Provider APIs, Email Service, Identity Provider, Tax Calculation Service

## Relationships
- Customer/Administrator -> Single-Page App (SPA): Accesses UI and manages sessions [HTTPS / TLS 1.3]
- Single-Page App (SPA) -> API Gateway: Routes frontend requests and API calls [HTTPS / JSON]
- API Gateway -> ECS/Fargate Microservices: Dispatches internal service requests [gRPC / REST]
- Microservices -> Amazon RDS / DynamoDB / OpenSearch / ElastiCache: Persists and retrieves transactional, catalog, and session data [TCP / TLS]

## Technology Stack
- React & Redux Toolkit: Powers the frontend SPA and global state management for fast rendering
- AWS S3 & CloudFront: Provides global static asset hosting and CDN delivery
- Node.js & NestJS: Implements backend microservices for maintainability and scalability
- Amazon ECS with Fargate: Runs containerized backend workloads without server management
- Amazon PostgreSQL, OpenSearch, DynamoDB & Redis: Handles relational data, full-text search, NoSQL items, and caching

## Rationale
This microservices-based architecture on AWS ensures 99.95% uptime and horizontal scalability for 1 million users. Decoupled services and global CDN caching achieve sub-2-second page loads on 3G connections.