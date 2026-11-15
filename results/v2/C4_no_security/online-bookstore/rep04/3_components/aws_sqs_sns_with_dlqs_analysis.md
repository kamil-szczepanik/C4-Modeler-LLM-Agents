## Overview
The Online Bookstore is a globally distributed e-commerce platform built on AWS, designed to support 1 million monthly active users with 99.95% uptime. It provides resilient physical and electronic book purchasing, secure checkout, multi-currency processing, and asynchronous customer notifications and recommendations.

## Key Elements
- **Users:** Shopper, Customer Support Agent
- **External Systems:** Payment Gateway, Shipping Provider APIs, Identity Provider, Third-Party Recommendation Engine, AWS Route 53
- **Frontend Containers:** AWS CloudFront & Amazon S3, Single Page Application (SPA) using React & TypeScript
- **Backend Containers:** AWS API Gateway, Catalog Service, Order & Checkout Service, User & Compliance Service, Notification Service, Recommendation Worker (all Spring Boot/Node.js on Amazon ECS/Fargate)
- **Data & Messaging Containers:** Amazon RDS PostgreSQL, Amazon DynamoDB, Amazon ElastiCache (Redis), AWS SQS/SNS with DLQs (Amazon SNS, Amazon SQS, AWS KMS, Amazon CloudWatch)

## Relationships
- Shopper -> AWS CloudFront & Amazon S3: Accesses static web assets [HTTPS]
- SPA -> AWS API Gateway: Invokes backend REST APIs [HTTPS]
- Order & Checkout Service -> Amazon SNS: Publishes order events [HTTPS/SigV4]
- Amazon SNS -> Amazon SQS: Broadcasts messages to notification and recommendation queues [HTTPS]
- Notification Service / Recommendation Worker -> Amazon SQS: Consumes events via long-polling [HTTPS]

## Technology Stack
- **Cloud Provider:** AWS (Regions: us-east-1, eu-west-1, ap-southeast-1) for multi-region scalability and 99.95% availability.
- **Compute:** Amazon ECS with AWS Fargate for serverless container management of microservices.
- **Messaging:** Amazon SNS and Amazon SQS with DLQs and KMS encryption for reliable asynchronous decoupling.
- **Databases:** Amazon RDS PostgreSQL and Amazon DynamoDB for transactional and high-throughput data storage.
- **Infrastructure as Code:** Terraform for consistent, modular multi-region deployments.

## Rationale
This architecture leverages serverless containers and managed AWS services to effortlessly scale and maintain sub-2-second page loads globally. Asynchronous messaging via SQS/SNS with DLQs and strict IAM controls ensure fault-tolerance, GDPR/CCPA compliance, and secure, highly available operations.