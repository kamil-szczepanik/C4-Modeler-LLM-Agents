## Overview
An Amazon-style e-commerce platform built for high scalability, global reach, and compliance. It enables users to browse, purchase physical and electronic books, manage shopping carts, leave reviews, and receive personalized recommendations.

## Key Elements
* Users: Customers, Inventory Managers, Customer Support Representatives
* Frontend: Single-Page Application (SPA)
* Entry & Security: Amazon API Gateway, AWS Cognito, AWS WAF
* Core Containers: Catalog & Search Service, Order & Checkout Service, Recommendation Service, Localization Service, Review Moderation Container
* Data & Messaging: Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon ElastiCache (Redis), Amazon SQS/SNS
* External Systems: Payment Gateway, Third-Party Shipping APIs, Notification Service, Publisher Partner Systems

## Relationships
* Customer browser to SPA via HTTPS (Amazon CloudFront)
* SPA to API Gateway via REST/GraphQL over HTTPS
* API Gateway to Core Services via gRPC over HTTP/2 and JWT validation
* Core Services to Data Stores via TCP/TLS
* Order & Checkout Service to Payment Gateway and Shipping APIs via HTTPS
* Services to Async Messaging via AWS SQS/SNS protocols

## Technology Stack
* Frontend: React/TypeScript hosted on AWS S3 and distributed via Amazon CloudFront for performance.
* Compute Runtime: Amazon ECS on AWS Fargate for serverless container management across regions.
* Backend Languages: Node.js/Express (Catalog, Localization), Java/Spring Boot (Order & Checkout), Python/FastAPI (Recommendation).
* Databases: Amazon Aurora PostgreSQL (multi-AZ/Global) for transactional data, Amazon DynamoDB for cart/sessions.
* Infrastructure & Security: Terraform/CDK, AWS Secrets Manager, AWS KMS, AWS Inspector, AWS WAF.

## Rationale
This architecture uses serverless containers and multi-region replication to guarantee high availability and sub-2-second page loads globally. Decoupling core microservices with async messaging ensures critical checkout workflows remain functional during traffic surges.