## Overview
The Online Bookstore is a globally distributed, scalable e-commerce platform hosted on AWS to support secure shopping, catalog browsing, and personalized recommendations. It ensures high performance, regulatory compliance (GDPR/CCPA), and robust multi-currency transactions for 1 million monthly active users.

## Key Elements
- **Users**: Customer, Administrator
- **External Systems**: Payment Gateway, Shipping Provider, Email/Notification Service, Identity Provider
- **Frontend Container**: React/TypeScript Single Page Application (SPA)
- **Edge & Gateway Containers**: AWS CloudFront, Amazon Route 53, AWS API Gateway
- **Backend Containers**: Catalog Service (Node.js), Order & Checkout Service (Spring Boot), Recommendation Service (Python/FastAPI)
- **Data & Messaging Containers**: Amazon Aurora PostgreSQL, Amazon DocumentDB, Amazon ElastiCache (Redis), AWS EventBridge / SQS
- **Infrastructure Containers**: Amazon ECS with Fargate, AWS Secrets Manager, AWS KMS

## Relationships
- Customer to CloudFront/SPA via HTTPS/TLS 1.3
- SPA to API Gateway via HTTPS/JSON REST/GraphQL
- API Gateway to Core Services via gRPC over mTLS (AWS ECS Service Connect)
- Catalog Service to Amazon DocumentDB via TCP/TLS
- Order & Checkout Service to Aurora PostgreSQL via TCP/TLS, and to Payment Gateway & Shipping Provider via HTTPS APIs
- Recommendation Service to Amazon ElastiCache (Redis) via TCP/TLS
- Core Services to AWS EventBridge/SQS via HTTPS for asynchronous messaging

## Technology Stack
- **Frontend**: React/TypeScript, AWS S3, AWS CloudFront (for sub-2s global page load performance)
- **Compute**: Amazon ECS with Fargate, AWS ECS Service Connect (for secure, serverless container orchestration)
- **Databases**: Amazon Aurora PostgreSQL (ACID compliance & multi-AZ failover), Amazon DocumentDB (flexible catalog metadata), Amazon ElastiCache for Redis (low-latency recommendations)
- **Messaging & Routing**: AWS EventBridge, Amazon SQS, AWS Route 53 (latency-based global traffic management)
- **Security**: AWS KMS (AES-256 encryption), AWS Secrets Manager, Amazon Inspector (container hardening & vulnerability scanning)

## Rationale
This multi-region AWS architecture combines managed services (Aurora, DocumentDB, Fargate) to guarantee 99.95% availability and handle 1M MAU without operational overhead. Zero-trust mTLS networking, tokenization, and KMS encryption ensure strict GDPR/CCPA compliance and OWASP Top-10 mitigation.