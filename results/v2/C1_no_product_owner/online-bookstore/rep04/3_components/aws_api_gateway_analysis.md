## Overview
The Online Bookstore system is a scalable e-commerce platform for physical and electronic books, supporting global traffic, secure checkout, and personalized recommendations. The architecture leverages AWS managed services and containerized microservices to guarantee high availability and compliance.

## Key Elements
- Client SPA (React, TypeScript, Amazon CloudFront, AWS S3)
- AWS API Gateway with WAF (REST API Endpoint, AWS Lambda Authorizer, Request Validator, Rate Limiting Module)
- Core E-Commerce Service (Node.js, TypeScript, AWS ECS Fargate)
- Recommendation & Search Service (Python, FastAPI, AWS ECS, Amazon OpenSearch)
- Data Tier (Amazon Aurora PostgreSQL Global Database, Amazon ElastiCache Redis, Amazon SQS/SNS)

## Relationships
- Client SPA -> AWS API Gateway: Sends API requests [HTTPS/REST, TLS 1.3]
- AWS API Gateway -> AWS Lambda Authorizer: Validates JWT tokens [In-memory invocation]
- AWS API Gateway -> Request Validator: Schema-validates JSON payloads [Local execution]
- AWS API Gateway -> Core E-Commerce Service: Forwards validated traffic [gRPC over internal VPC, SigV4/mTLS]
- AWS API Gateway -> Recommendation & Search Service: Routes search queries [gRPC over internal VPC, SigV4/mTLS]

## Technology Stack
- API Management: Amazon API Gateway with AWS WAF for edge security and rate limiting
- Compute: AWS ECS Fargate for containerized microservices scalability
- Database: Amazon Aurora PostgreSQL Global Database for multi-region consistency
- Caching: Amazon ElastiCache Redis for shopping cart and session state
- Security: AWS Lambda Authorizer, AWS Secrets Manager, and AWS KMS for data protection

## Rationale
This architecture ensures 99.95% availability and sub-2-second latency across multiple global regions by utilizing edge caching and serverless API routing. Strict security controls and distributed databases satisfy GDPR/CCPA compliance and OWASP Top-10 requirements at scale.