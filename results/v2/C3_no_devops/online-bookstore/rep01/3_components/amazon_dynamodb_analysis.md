## Overview
The system is an Amazon-style online bookstore designed to handle 1 million monthly active users globally with sub-2-second page loads. It utilizes a multi-region AWS cloud architecture to support catalog browsing, secure checkouts, reviews, and personalized recommendations.

## Key Elements
* **Users**: Customers, Book Authors/Publishers, Store Administrators
* **Edge & Security**: Amazon CloudFront, AWS WAF, AWS API Gateway
* **Frontend Container**: React SPA (React, TypeScript, AWS S3)
* **Backend Containers**: Catalog & Search Container (Spring Boot, Amazon OpenSearch), Order & Checkout Container (Node.js, TypeScript), Recommendation & Review Container (Python FastAPI), Customer Engagement Worker (Node.js)
* **Data & Storage Containers**: Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon ElastiCache Redis
* **DynamoDB Components**: `ShoppingCarts` Table, `UserSessions` Table, DynamoDB Global Tables
* **External Services**: Payment Gateway, Third-Party Shipping APIs, Tax Calculation Service, Email Service, AWS SQS/SNS

## Relationships
* **React SPA -> AWS CloudFront**: Serves static frontend assets and forwards API requests over HTTPS/TLS 1.3
* **AWS API Gateway -> Backend Containers**: Routes client requests using mTLS and HTTPS protocols
* **Order & Checkout Container -> Amazon DynamoDB**: Manages carts and sessions via AWS SDK using HTTPS/DynamoDB API and IAM roles
* **Order & Checkout Container -> Payment Gateway**: Processes secure payments via HTTPS/REST APIs
* **Order & Checkout Container -> Third-Party Shipping APIs**: Integrates fulfillment via HTTPS/REST APIs

## Technology Stack
* **AWS DynamoDB**: NoSQL database for carts/sessions chosen for single-digit millisecond latency and serverless scaling.
* **DynamoDB Global Tables**: Multi-region replication across `us-east-1`, `eu-west-1`, and `ap-southeast-1` to guarantee low latency.
* **AWS KMS**: Multi-region customer-managed keys for transparent encryption at rest.
* **IAM & Fine-Grained Access Control**: Secures container access via least privilege and `dynamodb:LeadingKeys`.
* **DynamoDB TTL & Auto Scaling**: Enforces GDPR data minimization and optimizes provisioned capacity at 70% utilization.

## Rationale
This architecture uses multi-region DynamoDB Global Tables and caching to achieve global sub-2-second page loads and 99.95% availability. AWS KMS encryption, IAM isolation, and DynamoDB TTL ensure strict GDPR and CCPA compliance.