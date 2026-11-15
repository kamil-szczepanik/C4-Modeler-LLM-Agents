## Overview
An AWS-hosted online bookstore application designed to support 1 million monthly active users globally. It provides multi-currency catalog browsing, secure checkout, reviews, and personalized recommendations with strict uptime and compliance standards.

## Key Elements
- Shopper and Administrator (Users)
- Frontend App (React SPA, Amazon CloudFront, Amazon S3)
- Amazon API Gateway
- Catalog Service, Order & Checkout Service, Recommendation Service (Node.js/Java/Python, AWS ECS Fargate)
- Amazon Aurora PostgreSQL (Multi-region database container)
- Amazon OpenSearch
- Third-Party Payment Gateway, Shipping Provider, Currency Exchange, Recommendation Engine
- Amazon RDS Proxy, AWS Secrets Manager, AWS KMS

## Relationships
- Shopper -> Frontend App: HTTPS
- Frontend App -> Amazon API Gateway: HTTPS
- Amazon API Gateway -> Catalog Service / Order & Checkout Service / Recommendation Service: REST/gRPC
- Catalog Service -> Amazon Aurora PostgreSQL (Read Replicas): PostgreSQL wire protocol via TLS 1.3
- Order & Checkout Service -> Amazon Aurora PostgreSQL (Primary Writer): PostgreSQL wire protocol via TLS 1.3
- Services -> Amazon RDS Proxy: PostgreSQL wire protocol via TLS 1.3
- RDS Proxy -> Amazon Aurora PostgreSQL: Internal database protocol

## Technology Stack
- Cloud Infrastructure: AWS (us-east-1, eu-west-1, ap-southeast-1) managed via Terraform/AWS CDK
- Compute: AWS ECS Fargate for containerized microservices
- Database: Amazon Aurora PostgreSQL Global Database with Amazon RDS Proxy for connection pooling
- Search & Recommendations: Amazon OpenSearch
- Security & Compliance: AWS KMS, AWS Secrets Manager, IAM database authentication, TLS 1.3

## Rationale
Amazon Aurora PostgreSQL with RDS Proxy provides high availability, ACID compliance, and connection scalability required for 1 million MAU. Multi-region replication and strict encryption controls ensure global low-latency performance while maintaining GDPR and CCPA compliance.