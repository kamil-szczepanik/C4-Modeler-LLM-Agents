## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform enabling users to purchase physical and electronic books, view ratings, and receive recommendations. It is architected for global scale, high availability, and strict regulatory compliance across multiple AWS regions.

## Key Elements
- **Users**: Customer, Store Administrator
- **External Systems**: Payment Gateway, Shipping Provider APIs, Email/Notification Service, Tax Calculation Service, Identity Provider (IdP)
- **Containers**: Single Page App (React, TypeScript), API Gateway (Amazon API Gateway), Catalog Service (Go), Order & Checkout Service (Node.js), Recommendation Service (Python, FastAPI), Database (Amazon DynamoDB, Amazon Aurora PostgreSQL), Cache (Amazon ElastiCache Redis), Message Broker (Amazon SQS, SNS, EventBridge)
- **DynamoDB Components**: Catalog Table (`Books`), Global Secondary Indexes (`SearchIndex`), DynamoDB Streams with AWS Lambda

## Relationships
- **Catalog Service -> Database (DynamoDB)**: Reads and writes catalogue data [DynamoDB Protocol]
- **Recommendation Service -> Database (DynamoDB)**: Reads user interactions and metadata [DynamoDB API / HTTPS]
- **Database (DynamoDB) -> AWS Global Tables**: Replicates data asynchronously across `us-east-1`, `eu-west-1`, and `ap-southeast-1`
- **Database (DynamoDB) -> Message Broker (Amazon SNS/EventBridge)**: Publishes change data capture events via DynamoDB Streams [AWS SDK / Internal API]

## Technology Stack
- **Frontend**: React, TypeScript, Amazon CloudFront, S3 (Ensures <2s page load performance on 3G)
- **Backend Services**: Go, Node.js (Express), Python (FastAPI) running on Amazon ECS / AWS Fargate
- **Databases**: Amazon DynamoDB (catalogue and recommendations), Amazon Aurora PostgreSQL (relational data)
- **Caching & Messaging**: Amazon ElastiCache (Redis), Amazon SQS, Amazon SNS, Amazon EventBridge
- **Cloud & Compliance**: AWS (us-east-1, eu-west-1, ap-southeast-1) configured for GDPR & CCPA compliance

## Rationale
This architecture uses serverless containers and managed multi-region databases to achieve 99.95% availability and sub-10ms response times for 1 million MAU. Asynchronous replication and event-driven caching ensure low-latency performance globally while maintaining strict security and compliance standards.