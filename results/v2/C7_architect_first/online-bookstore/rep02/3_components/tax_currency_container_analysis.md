## Overview
[An online bookstore system enabling global customers to browse, purchase, and review physical and electronic books with localized pricing and tax calculations. Core purpose is delivering a scalable, compliant, multi-currency e-commerce platform.]

## Key Elements
- **Users**: Guest Buyer, Registered Buyer, Store Administrator, Third-Party Vendor/Publisher
- **Frontend Container**: React.js SPA hosted on AWS S3, delivered via Amazon CloudFront
- **API Gateway**: AWS API Gateway with AWS Cognito JWT validation
- **Core E-Commerce Container**: Node.js / TypeScript running on Amazon ECS with AWS Fargate
- **Recommendation & Review Container**: Python, FastAPI running on Amazon ECS with AWS Fargate
- **Tax & Currency Container**: Node.js running on Amazon ECS with AWS Fargate
- **Storage**: Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon ElastiCache Redis
- **Integration**: Amazon SQS / SNS Event Bus, AWS SES, Stripe/PayPal, FedEx/UPS, Avalara/TaxJar

## Relationships
- **SPA -> API Gateway**: HTTPS / REST
- **API Gateway -> Core E-Commerce Container**: gRPC / HTTPS via Internal VPC ALBs
- **Core E-Commerce Container -> Tax & Currency Container**: mTLS / IAM via Internal VPC ALBs
- **Tax & Currency Container -> External Tax API (Avalara/TaxJar)**: HTTPS / REST with TLS 1.3
- **Currency Conversion Component -> Amazon ElastiCache Redis**: TCP with TLS and AWS KMS encryption

## Technology Stack
- **Cloud Provider**: AWS (Regions: us-east-1, eu-west-1, ap-southeast-1) for global multi-region availability
- **Compute**: Amazon ECS with AWS Fargate for serverless container scalability
- **Databases**: Amazon Aurora PostgreSQL (relational data) and Amazon DynamoDB (scalable key-value data)
- **Caching**: Amazon ElastiCache Redis for sub-10ms exchange rate retrieval
- **Security & Secrets**: AWS Cognito, AWS Secrets Manager, and AWS X-Ray for observability

## Rationale
[This architecture uses containerized microservices on AWS Fargate behind an API Gateway to achieve the required 1 million MAU scalability and 99.95% availability. Dedicated data stores, multi-region deployments, and resilient caching ensure sub-2-second page loads and strict GDPR/CCPA compliance.]