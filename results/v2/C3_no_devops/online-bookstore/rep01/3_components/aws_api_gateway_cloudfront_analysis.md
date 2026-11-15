## Overview
A scaled-down Amazon-style e-commerce site providing book browsing, secure checkout, reviews, and recommendations for 1M MAU. It features a distributed multi-region cloud architecture adhering to strict GDPR/CCPA and security constraints.

## Key Elements
- **Users**: Customers, Book Authors/Publishers, Store Administrators
- **Edge Layer**: AWS CloudFront, AWS WAF, Amazon Route 53, CloudFront Origin Shield
- **Ingress Layer**: Amazon API Gateway (Regional Endpoints, Usage Plans, API Keys)
- **Compute Containers**: React SPA, Catalog & Search, Order & Checkout, Recommendation & Review, Customer Engagement
- **Data Stores**: Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon ElastiCache Redis
- **External Systems**: Payment Gateway, Third-Party Shipping APIs, Tax Calculation Service, Email Service

## Relationships
- React SPA -> AWS API Gateway & CloudFront: Sends API requests and loads static assets [HTTPS / TLS 1.3]
- CloudFront -> Route 53 / API Gateway Regional Endpoints: Routes dynamic traffic globally [HTTPS]
- API Gateway -> Backend Containers: Routes via VPC Links and mTLS [REST / JSON over HTTP]

## Technology Stack
- **Cloud Provider**: AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for global multi-region scalability.
- **Frontend**: React, TypeScript, hosted on AWS S3 with CloudFront CDN.
- **Backend**: Spring Boot, Node.js (TypeScript), and Python FastAPI for microservices.
- **Data Tier**: Amazon Aurora PostgreSQL, Amazon DynamoDB, and Amazon ElastiCache Redis.
- **Security & Ingress**: AWS WAF, AWS Firewall Manager, mTLS, and AWS Secrets Manager.

## Rationale
The distributed AWS multi-region architecture ensures 99.95% availability and sub-2-second page loads globally for 1M MAU. Edge security controls and VPC isolation enforce GDPR/CCPA compliance and mitigate OWASP Top-10 threats.