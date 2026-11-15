## Overview
[An Amazon-style e-commerce online bookstore built on AWS, designed to handle 1M MAU while ensuring GDPR and CCPA compliance.]
## Key Elements
[• Customers and Admins (Users)
• Single-Page Application (SPA) & Back-Office Admin Portal (React, Amazon S3, Amazon CloudFront)
• API Gateway (Amazon API Gateway)
• Core Microservices (Catalog & Search, Checkout & Order, Recommendation, Admin & Compliance via Spring Boot & Python/FastAPI on Amazon ECS Fargate)
• Data Persistence (Amazon Aurora PostgreSQL, Amazon DynamoDB)
• External Systems (Payment Gateway, Shipping Provider APIs, Tax & Compliance Service, Recommendation Engine)]
## Relationships
[• Users access SPAs via HTTPS over Amazon CloudFront
• SPAs communicate with API Gateway using REST/HTTPS and JWT authentication
• API Gateway routes traffic to ECS Fargate containers via VPC Links with mTLS
• Core services sync with external APIs (Payment, Shipping, Tax, Recommendations) using REST/TLS
• Services read/write to Amazon Aurora PostgreSQL and Amazon DynamoDB]
## Technology Stack
[• Frontend: React on Amazon S3 and CloudFront for sub-2s global page loads
• Backend: Spring Boot and Python/FastAPI on Amazon ECS Fargate for scalability and modularity
• Databases: Amazon Aurora PostgreSQL for relational transactional data; Amazon DynamoDB for low-latency cart states
• Security & Networking: AWS KMS, AWS Secrets Manager, Amazon CloudWatch, and IAM for strict zero-trust isolation and compliance]
## Rationale
[This multi-tier container architecture on AWS isolates critical checkout and catalog workloads to guarantee high availability and sub-2-second performance. Dedicated administrative and compliance services ensure strict adherence to GDPR and CCPA regulations without impacting high-throughput customer journeys.]