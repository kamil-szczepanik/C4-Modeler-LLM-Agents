## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce site for purchasing physical and electronic books with recommendations and reviews. It utilizes a resilient, multi-region AWS cloud architecture to support high scalability, security, and low latency.

## Key Elements
- Customers and Store Administrators (Users)
- Single Page App (SPA) (React, TypeScript, Amazon CloudFront, S3)
- API Gateway (Amazon API Gateway)
- Catalog Service (Go), Order & Checkout Service (Node.js), Recommendation Service (Python, FastAPI)
- Cache (ElastiCache Redis) containing Recommendation Cache Component and Session Store Component
- Databases: Amazon DynamoDB and Amazon Aurora PostgreSQL
- Message Broker (Amazon SQS, Amazon SNS, Amazon EventBridge)
- External Systems: Payment Gateway, Shipping Provider APIs, Email/Notification Service, Tax Calculation Service, Identity Provider (IdP)

## Relationships
- Single Page App -> API Gateway via HTTPS/REST/GraphQL
- API Gateway -> Catalog Service, Order & Checkout Service, Recommendation Service via gRPC/REST
- Recommendation Service -> Cache (ElastiCache Redis) via Redis Protocol
- Message Broker -> Cache (ElastiCache Redis) for cache invalidation via AMQP/SNS topics
- Order & Checkout Service -> Amazon Aurora PostgreSQL and Amazon DynamoDB via TLS/TCP

## Technology Stack
- Frontend: React, TypeScript hosted on Amazon CloudFront and S3 for global CDN distribution
- Compute: Amazon ECS with AWS Fargate for serverless container orchestration
- Caching: Redis Cluster (OSS Redis Engine) deployed on Amazon ElastiCache with Multi-AZ automatic failover
- Databases: Amazon DynamoDB and Amazon Aurora PostgreSQL for transactional and NoSQL persistence
- Integration: Amazon SQS, SNS, and EventBridge for asynchronous messaging

## Rationale
This architecture uses Amazon ECS with AWS Fargate and Redis Cluster to scale horizontally, effortlessly handling 1M MAU while ensuring sub-2-second page loads. High availability (99.95% uptime) is achieved through Multi-AZ failover and managed AWS cloud services across global regions.