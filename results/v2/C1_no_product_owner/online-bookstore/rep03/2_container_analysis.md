## Overview
An Amazon-style e-commerce online bookstore for catalog browsing, checkout, recommendations, and reviews. Built for global scale, regulatory compliance, and high availability.

## Key Elements
* **SPA**: React/TypeScript frontend on Amazon CloudFront and S3
* **API Gateway**: Amazon API Gateway REST/GraphQL entry point
* **Catalog & Search Container**: Spring Boot and Amazon OpenSearch service
* **Order & Checkout Container**: Node.js/Express service
* **Recommendations Container**: Python/FastAPI service
* **Notification Service Container**: Go-based worker service
* **Data Stores**: Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon SQS/EventBridge

## Relationships
* **SPA to API Gateway**: HTTPS/WSS
* **API Gateway to Backend Containers**: gRPC/REST over VPC internal load balancers
* **Order Container to EventBridge**: HTTPS publishing of order events
* **Notification Service to EventBridge/SQS**: Asynchronous event consumption
* **Catalog Container to Aurora PostgreSQL**: JDBC/TLS querying of read replicas

## Technology Stack
* **AWS Cloud & Compute**: Amazon ECS with AWS Fargate for scalable container orchestration
* **Frontend**: React and TypeScript served via CloudFront/S3 for performance
* **Databases**: Aurora PostgreSQL (multi-AZ with read replicas, KMS encryption) and DynamoDB for carts
* **Messaging**: Amazon EventBridge and SQS with DLQs for asynchronous decoupling
* **Security**: AWS Secrets Manager, IAM least-privilege task roles, mTLS internal communication

## Rationale
Containerized microservices on AWS Fargate with multi-region Aurora PostgreSQL and read replicas ensure sub-2s performance and 99.95% uptime. Private VPC segmentation, mTLS, and AWS KMS encryption natively satisfy strict GDPR/CCPA compliance and OWASP security controls.