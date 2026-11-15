## Overview
An online bookstore system enabling catalogue browsing, secure checkout, reviews, and recommendations. The architecture utilizes distributed microservices deployed across multiple AWS regions to ensure high availability and scalability.

## Key Elements
* Shoppers, Vendors, & Admins (Users)
* AWS API Gateway & WAF (Ingress & Security)
* Review & Rating Microservice (ECS Fargate Container)
* Amazon DynamoDB Global Tables & Amazon DAX (Data Persistence & Caching)
* Checkout & Cart Microservice (Downstream Dependency)
* Amazon SQS / SNS (Asynchronous Messaging)

## Relationships
* Shoppers -> AWS API Gateway & WAF: HTTPS
* API Gateway & WAF -> Review & Rating Microservice: gRPC over HTTP/2 (mTLS)
* Review & Rating Microservice -> Checkout & Cart Microservice: gRPC (mTLS)
* Review & Rating Microservice -> Amazon DynamoDB / DAX: AWS SDK (HTTPS)
* Review & Rating Microservice -> Amazon SQS: AWS SDK (HTTPS)

## Technology Stack
* AWS ECS Fargate: Container orchestration for microservices
* Amazon DynamoDB Global Tables: Multi-region NoSQL persistence
* Amazon DAX: In-memory caching for read scalability
* gRPC over HTTP/2: High-performance inter-service communication
* AWS KMS: Encryption-at-rest with customer-managed keys
* AWS X-Ray: Distributed tracing and observability

## Rationale
Multi-region DynamoDB Global Tables and DAX caching ensure sub-second performance and 99.95% availability for 1M MAU. ECS Fargate auto-scaling and gRPC communication meet strict performance and scalability constraints.