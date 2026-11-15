## Overview
The Online Bookstore is a scaled-down e-commerce platform built on AWS for selling physical and electronic books, supporting 1 million monthly active users across multiple global regions. It provides catalog browsing, secure checkout, reviews, and personalized recommendations while ensuring strict compliance with GDPR, CCPA, and OWASP security standards.

## Key Elements
* **Users**: Customer, Site Administrator
* **Frontend**: Single Page App (React / TypeScript) hosted on AWS S3 & CloudFront
* **Gateway**: AWS API Gateway
* **Microservices**: Catalog & Search, Order & Checkout, Recommendation, Content Management / Moderation, Notification
* **Data Stores**: AWS Aurora PostgreSQL, AWS DynamoDB
* **Integration Services**: AWS SQS, AWS EventBridge, AWS App Mesh, AWS Secrets Manager, AWS KMS
* **External Systems**: Third-Party Shipping Partner, Payment Gateway, Tax & Currency Service, Third-Party Identity Provider, Notification Service

## Relationships
* **Customer to SPA**: HTTPS over TLS 1.3
* **SPA to API Gateway**: HTTPS/JSON REST APIs
* **API Gateway to Microservices**: gRPC over mTLS via AWS App Mesh
* **Microservices to Data Stores**: TCP with AWS KMS encryption at rest
* **Order & Checkout to Payment Gateway**: HTTPS REST API
* **Order & Checkout to Shipping Partner**: HTTPS API

## Technology Stack
* **Frontend**: React, TypeScript (For responsive user interface)
* **Backend Runtime**: Spring Boot for Java (Catalog), Node.js with TypeScript (Order, Notification), FastAPI with Python (Recommendations)
* **Search & Compute**: AWS OpenSearch (Sub-2s keyword search), AWS ECS Fargate (Container hosting)
* **Messaging & Events**: AWS SQS, AWS EventBridge / MSK Kafka (Asynchronous decoupling)
* **Security & Infrastructure**: AWS IAM, AWS Secrets Manager, AWS WAF, AWS KMS (Compliance and secrets injection)

## Rationale
This multi-region AWS microservices architecture isolates PCI-DSS and GDPR data scopes while ensuring 99.95% availability and sub-2-second page loads. Decoupled containers using gRPC over mTLS and asynchronous SQS messaging guarantee scalability for 1M MAU without performance degradation.