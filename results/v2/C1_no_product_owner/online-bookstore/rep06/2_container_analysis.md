## Overview
An Amazon-style online bookstore providing catalogue browsing, secure checkout, reviews, and recommendations at scale. It ensures high availability, multi-region deployment, and compliance with GDPR and CCPA.

## Key Elements
- Single Page Application (React / TypeScript)
- API Gateway / Application Load Balancer (ALB)
- Backend Containers: Catalog & Search, Order & Checkout, Engagement Service
- Data Stores: Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon OpenSearch
- AWS Infrastructure: ECS Fargate, AWS S3, CloudFront, WAF, KMS, Secrets Manager, SQS/SNS

## Relationships
- Client to CloudFront/S3: HTTPS/TLS 1.3
- API Gateway to ECS Fargate: mTLS via AWS App Mesh with OAuth2.0/JWT propagation
- Backend Containers to Data Stores: TLS-encrypted TCP with AWS RDS Proxy
- Inter-service communication: Asynchronous via Amazon SQS/SNS
- External integrations: HTTPS/REST to third-party shipping and payment APIs

## Technology Stack
- Frontend: React / TypeScript hosted on AWS S3 & CloudFront for sub-2s global page loads
- Compute: Amazon ECS (Fargate) for elastic container scalability supporting 1M MAU
- Databases: Aurora PostgreSQL (multi-region transactions), DynamoDB (carts/sessions), OpenSearch (catalogue search)
- Security & DevOps: AWS WAF, KMS, Secrets Manager, App Mesh, Terraform/OpenTofu, ADOT

## Rationale
The containerized micro-service approach balances domain separation with operational manageability to handle 1M MAU. Multi-region AWS deployment with secure managed services guarantees 99.95% uptime and OWASP compliance.