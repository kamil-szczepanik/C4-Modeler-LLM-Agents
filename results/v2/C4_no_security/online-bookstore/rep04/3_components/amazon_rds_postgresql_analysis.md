## Overview
[An Amazon-style e-commerce online bookstore for physical and electronic books with reviews and recommendations. Core purpose is secure browsing, cart management, and checkout serving 1M MAU globally.]

## Key Elements
- Shopper and Customer Support Agent
- AWS Route 53, AWS CloudFront & Amazon S3
- React SPA, AWS API Gateway
- Catalog, Order & Checkout, User & Compliance, and Notification Services (Spring Boot/Node.js on Amazon ECS/Fargate)
- Recommendation Worker
- Amazon RDS PostgreSQL (Primary, Read Replicas, and RDS Proxy)
- Amazon DynamoDB, Amazon ElastiCache (Redis)
- AWS SQS/SNS with DLQs, Payment Gateway, Shipping Provider APIs, Identity Provider

## Relationships
- Shopper -> AWS Route 53: DNS resolution [HTTPS]
- SPA -> AWS CloudFront & Amazon S3: Static asset delivery [HTTPS]
- SPA -> AWS API Gateway: API requests [HTTPS/REST]
- API Gateway -> ECS/Fargate Containers: Internal routing [HTTP/gRPC]
- Services -> Amazon RDS Proxy: Connection pooling [TCP/PostgreSQL Wire Protocol]
- RDS Proxy -> RDS PostgreSQL Primary/Read Replicas: Database queries [PostgreSQL Protocol]

## Technology Stack
- AWS (us-east-1, eu-west-1, ap-southeast-1): Global cloud infrastructure for low latency
- Amazon RDS PostgreSQL & RDS Proxy: Relational data storage with connection pooling and regional replicas
- Amazon ECS/Fargate: Container orchestration for scalable microservices
- React & TypeScript: Frontend SPA performance

## Rationale
[Multi-region AWS architecture with read replicas and caching ensures sub-second page loads and 99.95% availability for 1M MAU. PostgreSQL with RDS Proxy and rigorous backup policies guarantees transactional integrity for secure checkouts and GDPR compliance.]