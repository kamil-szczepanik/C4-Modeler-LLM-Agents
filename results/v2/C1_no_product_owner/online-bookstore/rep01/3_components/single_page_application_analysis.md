## Overview
An Amazon-style online bookstore providing catalog browsing, secure checkout, reviews, and personalized recommendations. The architecture ensures global scalability, high availability, and strict regulatory compliance.

## Key Elements
- Customers & Admin Staff
- Single Page Application (React, TypeScript, AWS S3, CloudFront)
- AWS API Gateway & Application Load Balancer
- Catalog Service, Order & Checkout Service, Recommendation Service (AWS ECS Fargate)
- Amazon Aurora PostgreSQL & Amazon ElastiCache (Redis)
- External Payment Gateway, Shipping Provider APIs, Identity Provider

## Relationships
- Customer & Admin Staff -> Single Page Application: Accesses platform via HTTPS
- Single Page Application -> AWS API Gateway & ALB: Sends API requests via HTTPS/REST
- Microservices -> Amazon Aurora PostgreSQL & ElastiCache: Data persistence and caching via TCP

## Technology Stack
- React & TypeScript: Core frontend framework for type-safe UI development
- AWS S3 & CloudFront: Global content delivery and static asset hosting for performance
- AWS ECS Fargate: Serverless container execution for backend microservices
- Amazon Aurora PostgreSQL: Relational data store for transactional integrity

## Rationale
The serverless container and global CDN architecture easily scales to 1M MAU while guaranteeing sub-2-second page loads. Decoupled microservices and robust cloud infrastructure ensure 99.95% availability and rigorous security compliance.