## Overview
An Amazon-scale online bookstore providing catalog browsing, shopping carts, secure checkout, reviews, and personalized recommendations. The system is architected for global scale, supporting 1 million monthly active users (MAU) with high availability and GDPR/CCPA compliance.

## Key Elements
- **Users**: Customer, Admin / Content Manager
- **External Systems**: Payment Gateway, Shipping Provider API, Notification Service, Tax Calculation Service, Third-Party Recommendation Engine, Identity Provider
- **Frontend Container**: Single Page Application (React, Amazon CloudFront, Amazon S3)
- **API & Routing**: Amazon API Gateway (AWS API Gateway, JWT)
- **Backend Services**: Core E-Commerce API (Node.js, Express, Amazon ECS (Fargate)), Recommendation & Review Service (Python, FastAPI, Amazon ECS (Fargate))
- **Database Components**: Amazon Aurora (PostgreSQL) Global Database, Amazon RDS Proxy, Primary Cluster Instance (Writer), Cross-Region Read Replica Instances, Aurora Storage Volume, PostgreSQL Extension Manager

## Relationships
- Single Page Application -> Amazon API Gateway: HTTPS / REST [TLS 1.3]
- Amazon API Gateway -> Core E-Commerce API: HTTPS / REST [TLS 1.3]
- Amazon API Gateway -> Recommendation & Review Service: HTTPS / REST [TLS 1.3]
- Core E-Commerce API -> RDS Proxy (Primary): PostgreSQL wire protocol [TLS 1.3]
- Recommendation & Review Service -> RDS Proxy (Regional Replicas): PostgreSQL wire protocol [TLS 1.3]
- RDS Proxy -> Primary Cluster Instance (Writer) / Cross-Region Read Replicas: PostgreSQL wire protocol [TLS 1.3]

## Technology Stack
- **Frontend**: React hosted on Amazon S3 and delivered via Amazon CloudFront for low-latency global static asset delivery.
- **Compute**: Amazon ECS with AWS Fargate for serverless container orchestration of Node.js and Python microservices.
- **Database & Storage**: Amazon Aurora PostgreSQL Global Database with cross-region replication for low-latency regional reads and data residency.
- **Connection Pooling & Security**: Amazon RDS Proxy for connection management and IAM authentication enforcement.
- **Infrastructure & Monitoring**: Terraform for Infrastructure as Code, AWS CloudWatch, and AWS DevOps Guru for observability.

## Rationale
This multi-region AWS architecture ensures a sub-2-second page load time on 3G networks globally and meets the 99.95% uptime requirement. Utilizing RDS Proxy, read replicas, and isolated compute tasks enables seamless horizontal scalability for 1 million MAU while enforcing strict GDPR/CCPA compliance standards.