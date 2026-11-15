## Overview
An Amazon-style online bookstore designed to handle 1 million monthly active users while ensuring strict GDPR and CCPA compliance. The system supports multi-currency browsing, real-time checkout, automated recommendations, and sub-2-second global page loads.

## Key Elements
* Customers and Store Administrators / Content Managers (Users)
* Storefront (React SPA on Amazon S3 / CloudFront)
* API Gateway (AWS API Gateway with RBAC and JWT validation)
* Catalog & Search Service (Node.js, Amazon OpenSearch)
* Order & Checkout Service (Spring Boot in isolated private VPC)
* Recommendation Service (Python, FastAPI, Amazon DynamoDB)
* Customer Privacy Service (Node.js, Amazon DynamoDB)
* Pricing & Currency Service (Go, Redis cache)
* External Payment Gateway, Shipping Provider, Identity Provider, and Notification Service

## Relationships
* Customers interact with Storefront via HTTPS/TLS 1.3
* Storefront communicates with API Gateway via HTTPS/REST
* API Gateway routes requests to ECS Fargate containers via mTLS
* Order & Checkout Service integrates with External Payment Gateway and Shipping Provider via HTTPS/REST
* Services persist data to Amazon OpenSearch, DynamoDB, and Redis with KMS encryption at rest

## Technology Stack
* **Cloud Infrastructure:** AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`), Amazon ECS on AWS Fargate, Application Load Balancer, AWS Global Accelerator
* **Frontend:** React, Amazon S3, Amazon CloudFront CDN
* **Backend Services:** Node.js/Express, Java/Spring Boot, Python/FastAPI, Go
* **Databases & Caching:** Amazon OpenSearch, Amazon DynamoDB, Redis
* **Security & Observability:** AWS Secrets Manager, AWS KMS, AWS X-Ray, Amazon CloudWatch, SPIFFE/SPIRE for service mesh mTLS

## Rationale
This microservices-based architecture deployed on AWS Fargate across multi-AZ regions guarantees 99.95% uptime and high scalability for 1M MAU. Isolated VPC subnets, regional data partitioning, and tokenized payments ensure robust OWASP Top-10 mitigation and GDPR/CCPA compliance.