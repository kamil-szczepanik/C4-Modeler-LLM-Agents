## Overview
An Amazon-style e-commerce online bookstore built on AWS, designed to handle 1 million monthly active users with multi-currency and GDPR/CCPA compliance. The system decouples catalogue browsing from secure checkout to ensure high availability and performance.

## Key Elements
* **Users:** Book Buyer / Registered Reviewer, Store Administrator
* **Containers:** Single Page Application (SPA), API Gateway, Catalogue Service, Order & Checkout Service, Recommendation & Review Service
* **Data Stores & Messaging:** Amazon Aurora PostgreSQL, Amazon OpenSearch, Amazon SQS/SNS
* **External Systems:** Payment Gateway Provider, Shipping Provider APIs, Identity Provider / Notification Service, Recommendation Engine, Tax & Localization API
* **Infrastructure:** AWS ECS (Fargate), AWS CloudFront & S3, AWS API Gateway, AWS VPC

## Relationships
* **SPA to API Gateway:** HTTPS/JSON via AWS CloudFront/S3
* **API Gateway to Internal Services:** mTLS and gRPC
* **Catalogue Service to OpenSearch:** Internal query protocol for fast keyword lookups
* **Order & Checkout Service to Aurora PostgreSQL:** Transactional database queries
* **Order & Checkout Service to External APIs:** Outbound HTTPS to Payment Gateway and Shipping Provider APIs
* **Recommendation & Review Service to SQS/SNS:** Asynchronous event publishing

## Technology Stack
* **Frontend:** React / TypeScript hosted on AWS S3 & CloudFront for edge caching and global performance (<2s load time)
* **API Routing:** AWS API Gateway for JWT validation, rate limiting, and routing
* **Catalogue Service:** Node.js (Express) backed by Amazon OpenSearch for scalable product search
* **Order & Checkout Service:** Java (Spring Boot) with Amazon Aurora PostgreSQL for secure, transactional payments
* **Recommendation Service:** Python (FastAPI) integrated via Amazon SQS/SNS for asynchronous event handling
* **Infrastructure & Security:** AWS ECS (Fargate), AWS VPC with mTLS, AWS KMS, and AWS Secrets Manager for zero-trust security and GDPR compliance

## Rationale
The decoupled microservices architecture isolates transactional checkout from resource-heavy search and recommendations, meeting strict scalability (1M MAU) and availability (99.95%) targets. Multi-region AWS deployment combined with edge-cached localization ensures low-latency performance globally while satisfying regulatory constraints.