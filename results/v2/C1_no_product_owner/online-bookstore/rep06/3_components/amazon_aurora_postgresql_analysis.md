## Overview
- Online Bookstore e-commerce platform processing physical and electronic book sales, recommendations, and reviews.
- Built on a multi-region AWS cloud architecture ensuring high availability, compliance, and low-latency global performance.

## Key Elements
- Customers (Users)
- AWS CloudFront and AWS WAF, AWS Route 53
- Single Page Application (React / TypeScript, AWS S3)
- API Gateway / ALB (AWS ALB / Amazon API Gateway)
- Order & Checkout (Amazon ECS Fargate)
- Amazon Aurora PostgreSQL (AWS RDS Proxy, Primary Writer, Global Read Replicas, Aurora Distributed Storage Volume)
- Amazon DynamoDB, Amazon OpenSearch, Amazon SQS / SNS
- External Payment Gateway and Shipping Provider APIs

## Relationships
- Customer -> AWS CloudFront + WAF: HTTPS
- Single Page Application -> API Gateway / ALB: HTTPS / JSON
- Order & Checkout -> AWS RDS Proxy: TLS-encrypted PostgreSQL wire protocol (Port 5432)
- AWS RDS Proxy -> Primary Instance: TCP
- Primary Instance -> Read Replicas: Storage-level replication log stream

## Technology Stack
- Frontend: React / TypeScript hosted on AWS S3 and distributed via AWS CloudFront
- Compute: Amazon ECS Fargate for containerized microservices execution
- Database: Amazon Aurora PostgreSQL with AWS RDS Proxy for connection pooling and transaction management
- Security: AWS KMS for encryption at-rest, IAM Database Authentication, AWS Secrets Manager, TLS 1.3 for data-in-transit
- Storage: Amazon Aurora Distributed Storage, Amazon DynamoDB, Amazon S3

## Rationale
- Multi-region Aurora Global Database deployment ensures sub-2-second page loads and 99.95% availability across global regions.
- Strict security controls, private subnet isolation, and IAM authentication satisfy GDPR, CCPA, and OWASP Top-10 compliance mandates.