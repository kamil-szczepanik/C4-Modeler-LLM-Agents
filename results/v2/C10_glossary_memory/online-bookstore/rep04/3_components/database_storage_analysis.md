## Overview
The Online Bookstore system is a globally distributed e-commerce platform built for 1M MAU to deliver catalog browsing, secure checkout, reviews, and personalized recommendations. It ensures high availability, strict security compliance, and low-latency performance across multiple international regions.

## Key Elements
- Customers, Authors/Publishers, Store Administrators
- Web App Frontend (React, Next.js, TypeScript)
- API Gateway (Amazon API Gateway)
- Catalog & Search Service (Java, Spring Boot, Amazon OpenSearch)
- Checkout & Order Service (Go, gRPC/REST)
- Recommendation Service (Python, FastAPI)
- Admin Management Service (Java, Spring Boot)
- Database Storage (Amazon Aurora PostgreSQL Global Database)
- Caching Layer (Amazon ElastiCache (Redis))
- External Systems: Payment Gateway, Third-Party Shipping APIs, Notification Service, Customer Support CRM, Identity Provider, AWS CloudFront CDN/WAF, Route 53, AWS Secrets Manager, AWS KMS

## Relationships
- Customers -> Web App Frontend: HTTPS / TLS 1.3 / OAuth 2.0 / OIDC
- Web App Frontend -> API Gateway: HTTPS / REST / gRPC
- API Gateway -> Catalog & Search Service, Checkout & Order Service, Recommendation Service, Admin Management Service: HTTPS / gRPC
- Checkout & Order Service -> Payment Gateway, Third-Party Shipping APIs: HTTPS / REST APIs
- Recommendation Service -> Caching Layer: Redis Protocol
- Catalog & Search Service, Checkout & Order Service, Admin Management Service -> Database Storage: PostgreSQL Protocol over TLS

## Technology Stack
- Frontend: React, Next.js, TypeScript for responsive client-side rendering
- Backend Microservices: Java (Spring Boot), Go (gRPC/REST), Python (FastAPI) for domain-driven scalability
- Database: Amazon Aurora PostgreSQL Global Database with Amazon RDS Proxy for multi-region replication and connection management
- Caching & Search: Amazon ElastiCache (Redis) and Amazon OpenSearch for sub-100ms retrieval
- Security & Infrastructure: AWS IAM, AWS KMS (AES-256), AWS Secrets Manager, AWS CloudFront CDN/WAF, Amazon API Gateway deployed across AWS regions (`us-east-1`, `eu-west-1`, `ap-southeast-1`)

## Rationale
This architecture uses multi-region serverless and managed AWS services to guarantee 99.95% uptime and sub-2-second page loads globally. Schema segregation, IAM authentication, and encryption at rest directly fulfill strict GDPR, CCPA, and OWASP security constraints.