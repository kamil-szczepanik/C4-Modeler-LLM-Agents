## Overview
[The system is an online bookstore providing catalog browsing, secure checkout, reviews, and recommendations for physical and electronic books. Its core purpose is to deliver a scalable, secure, and globally performant e-commerce experience handling 1M MAU.]

## Key Elements
- Customer (Shopper)
- Book Reviewer
- Store Administrator
- Single-Page Application (SPA) (React, hosted on Amazon S3 / CloudFront)
- Admin Back-Office App (React)
- API Gateway (Amazon API Gateway)
- Core Services (Node.js/NestJS, Amazon ECS (Fargate))
- Recommendation Engine (Python/FastAPI, Amazon ECS (Fargate))
- Notification Worker (Node.js/Python, Amazon ECS (Fargate))
- Analytics Ingestion Container (Amazon ECS (Fargate))
- Aurora PostgreSQL (Amazon Aurora PostgreSQL (Multi-AZ))
- Amazon DynamoDB
- Amazon S3 (Frontend Bucket, E-Book Asset Bucket, Backup & Analytics Bucket)
- Amazon EventBridge
- Amazon SQS
- External Systems: Payment Gateway, Third-Party Shipping Provider, Tax & Compliance Service, Email/Notification Service

## Relationships
- Customer interacts with SPA via HTTPS (TLS 1.3)
- SPA interacts with API Gateway via HTTPS / REST / JSON
- API Gateway routes requests to Core Services and Recommendation Engine via internal VPC networking
- Core Services interacts with Aurora PostgreSQL via PostgreSQL wire protocol over TLS
- Core Services interacts with Amazon DynamoDB via AWS SDK (HTTPS)
- Core Services interacts with E-Book Asset Bucket via AWS SDK (HTTPS) using pre-signed URLs
- Core Services communicates asynchronously via Amazon EventBridge and Amazon SQS
- Analytics Ingestion Container writes operational logs to Backup & Analytics Bucket via AWS internal APIs

## Technology Stack
- Cloud Provider: AWS (Regions: us-east-1, eu-west-1, ap-southeast-1) for multi-region resilience
- Frontend: React hosted on Amazon S3 and distributed via Amazon CloudFront for sub-2s global page loads
- Backend Services: Node.js/NestJS (Core Services) and Python/FastAPI (Recommendation Engine) running on Amazon ECS (Fargate)
- Databases: Amazon Aurora PostgreSQL (Multi-AZ) for relational transactional data and Amazon DynamoDB for reviews and unstructured data
- Storage & Security: Amazon S3 with AWS KMS customer-managed keys (SSE-KMS), AWS SDK v3, and Terraform/AWS CDK for Infrastructure as Code

## Rationale
[This architecture combines AWS serverless and containerized services to ensure elastic scalability for 1M MAU while meeting strict GDPR, CCPA, and OWASP compliance requirements. Multi-region deployments and managed storage tiers optimize both global performance and operational cost-efficiency.]