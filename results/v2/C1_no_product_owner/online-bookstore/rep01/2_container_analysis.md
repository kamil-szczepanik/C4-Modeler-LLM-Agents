## Overview
The Online Bookstore is a globally scaled e-commerce platform designed to process physical and electronic book sales, customer reviews, and personalized recommendations. It guarantees high availability and compliance across multiple international regions.

## Key Elements
- Customers and Admin Staff (Users)
- Single Page Application (React, TypeScript)
- AWS API Gateway & Application Load Balancer (ALB)
- Core Containers: Catalog Service (Go), Order & Checkout Service (Node.js), Recommendation Service (Python FastAPI)
- AWS SQS/SNS (Async Event Bus)
- Databases: Amazon Aurora PostgreSQL, Amazon ElastiCache (Redis)
- External Systems: Payment Gateway, Shipping Provider APIs, Identity Provider

## Relationships
- Customer/Admin -> SPA via HTTPS
- SPA -> ALB via HTTPS
- ALB -> Core Services via AWS App Mesh sidecars using gRPC over mTLS
- Order & Checkout Service -> Payment Gateway via HTTPS/REST
- Order & Checkout Service -> Shipping Provider APIs via HTTPS/REST
- Core Services -> AWS SQS/SNS via AWS SDK/HTTPS

## Technology Stack
- **Frontend**: AWS S3 & CloudFront for static asset distribution and <2s page load performance.
- **Orchestration**: AWS ECS with Fargate for serverless container management and 99.95% uptime.
- **Databases**: Amazon Aurora PostgreSQL for relational storage and Amazon ElastiCache (Redis) for low-latency recommendations.
- **Security**: AWS Secrets Manager, AWS KMS (AES-256), and IAM execution roles for compliance and data protection.

## Rationale
This containerized AWS architecture uses serverless compute and Multi-AZ databases to effortlessly scale for 1M MAU while strictly enforcing GDPR, CCPA, and OWASP security controls. App Mesh mTLS and decoupled asynchronous messaging guarantee fault tolerance and secure multi-region operations.