## Overview
- Online Bookstore is a scaled-down e-commerce platform for purchasing physical and electronic books with recommendations and reviews.
- The architecture ensures secure, compliant, and scalable operations across global regions using AWS.

## Key Elements
- Customers and Store Administrators (Actors)
- Single Page Application (React, TypeScript, Amazon CloudFront, Amazon S3)
- API Gateway (Amazon API Gateway)
- User Privacy & Compliance Service (AWS ECS Fargate, Python, FastAPI)
  - Compliance API Controller
  - Data Extraction Engine
  - Anonymization & Purging Worker
  - Compliance Event Publisher / Notification Dispatcher
- Catalog & Search Service, Checkout & Order Service, Recommendation Service (AWS ECS Fargate)
- Data Stores (Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon S3 Object Lock WORM bucket)
- Messaging & Integration (Amazon SQS, AWS SES, AWS KMS, AWS Secrets Manager)

## Relationships
- Customer -> Single Page Application: Browses catalog and manages privacy settings [HTTPS]
- Single Page Application -> API Gateway: Sends REST requests and receives responses [HTTPS, JWT]
- API Gateway -> User Privacy & Compliance Service: Routes privacy requests [mTLS, AWS IAM]
- Data Extraction Engine -> Amazon S3: Stores encrypted data exports with 15-minute presigned URLs [HTTPS, AWS KMS]
- Anonymization & Purging Worker -> Aurora PostgreSQL & DynamoDB: Executes purging and anonymization [SSL/TLS]
- Compliance Event Publisher -> Amazon SQS: Publishes domain events for asynchronous workflows [AMQP/SQS Protocol]

## Technology Stack
- Frontend: React, TypeScript hosted on Amazon S3 with Amazon CloudFront CDN
- Backend Compute: AWS ECS Fargate running Spring Boot, Node.js/Express, and Python/FastAPI
- Databases: Amazon Aurora PostgreSQL and Amazon DynamoDB for transactional and NoSQL data
- Messaging & Storage: Amazon SQS, Amazon S3 with WORM object lock, and AWS SES for notifications
- Security & Operations: AWS KMS, AWS Secrets Manager, Amazon CloudWatch, and IAM for compliance and auditing

## Rationale
- The AWS-native, microservices-based architecture provides 99.95% availability and scales seamlessly to support 1 million MAU.
- Strict isolation, encryption, and automated event-driven workflows guarantee GDPR and CCPA compliance without impacting core storefront performance.