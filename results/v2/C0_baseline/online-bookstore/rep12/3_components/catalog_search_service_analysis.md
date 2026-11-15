## Overview
The Online Bookstore system is a scaled-down e-commerce platform designed for buying physical and electronic books with recommendations, reviews, and multi-currency support. It delivers high performance, secure transactions, and global scalability for 1 million monthly active users.

## Key Elements
- Customers and Store Administrators
- Storefront (React SPA on Amazon S3 and Amazon CloudFront CDN)
- API Gateway (AWS API Gateway with RBAC and JWT validation)
- Catalog & Search Service (Node.js, Amazon OpenSearch, Amazon DocumentDB)
- Order & Checkout Service (Spring Boot in isolated private VPC)
- Recommendation Service (Python, FastAPI, Amazon DynamoDB)
- Customer Privacy Service (Node.js, Amazon DynamoDB)
- Pricing & Currency Service (Go, Redis cache)
- External Systems: External Payment Gateway, External Shipping Provider, External Identity Provider, External Notification Service

## Relationships
- Storefront -> API Gateway: HTTPS [TLS 1.3]
- API Gateway -> Catalog & Search Service: HTTP/2 over mTLS [mTLS]
- Search API Controller -> Search Engine Client: In-process calls (gRPC/Async)
- Search Engine Client -> Amazon OpenSearch: HTTPS [TLS 1.3]
- Search API Controller -> Pricing Aggregator Client: In-process calls
- Pricing Aggregator Client -> Pricing & Currency Service: HTTP/2 [mTLS] within internal VPC
- System -> External Payment Gateway: HTTPS [TLS 1.3], REST API
- System -> External Shipping Provider: HTTPS [TLS 1.3], REST API

## Technology Stack
- Cloud Provider: AWS across us-east-1, eu-west-1, ap-southeast-1 regions
- Frontend: React SPA hosted on Amazon S3 with Amazon CloudFront CDN
- Backend Services: Node.js (Catalog/Search, Privacy), Spring Boot (Checkout), Python FastAPI (Recommendations), Go (Pricing)
- Datastores: Amazon OpenSearch, Amazon DocumentDB, Amazon DynamoDB, Redis
- Security & Infrastructure: AWS API Gateway, AWS KMS, AWS Secrets Manager, mTLS, TLS 1.3, Terraform/AWS CDK

## Rationale
This architecture decouples domain services to ensure independent scaling, fault isolation, and low-latency performance under heavy traffic. AWS managed services combined with strict regional replication and zero-trust security controls guarantee high availability, GDPR/CCPA compliance, and robust OWASP Top-10 mitigation.