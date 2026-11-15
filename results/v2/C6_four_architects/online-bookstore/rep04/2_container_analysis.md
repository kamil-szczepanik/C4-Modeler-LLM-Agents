## Overview
An AWS-hosted e-commerce platform built as a microservices architecture to sell physical and electronic books. It handles high scalability, secure payments, and GDPR compliance.

## Key Elements
* **Single-Page Application (SPA)**: React/TypeScript client interface.
* **API Gateway**: Amazon API Gateway managing entry traffic.
* **Backend Services**: ECS Fargate containers including Catalog Service (Node.js), Order & Checkout Service (Java/Spring Boot), Recommendation Service (Python/FastAPI), Auth Service, Privacy Service, and Background Worker.
* **Data Tier**: Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon OpenSearch, and Amazon S3.
* **Messaging & Observability**: Amazon SNS/SQS, Amazon CloudWatch, and AWS X-Ray.

## Relationships
* **SPA** to **API Gateway**: HTTPS / JSON.
* **API Gateway** to **ECS Fargate Services**: Internal gRPC / HTTP/2 over private VPC subnets.
* **Services** to **Aurora PostgreSQL / DynamoDB**: JDBC / TCP.
* **Services** to **SNS/SQS**: Asynchronous event messaging.

## Technology Stack
* **AWS ECS (Fargate)**: Container orchestration for secure, scalable microservices deployment.
* **Amazon Aurora PostgreSQL & DynamoDB**: Managed relational storage for transactions and NoSQL storage for carts/sessions.
* **Amazon OpenSearch**: Dedicated search engine for catalogue browsing.
* **Amazon S3 & CloudFront**: Static asset delivery and digital book storage with low-latency CDN.

## Rationale
This architecture uses serverless and managed AWS components to meet the 1M MAU scalability, sub-2s 3G performance, and 99.95% availability targets. Isolated VPC subnets and dedicated privacy services ensure strict GDPR and CCPA compliance.