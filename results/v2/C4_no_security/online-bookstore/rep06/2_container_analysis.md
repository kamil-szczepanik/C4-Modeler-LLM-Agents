## Overview
- Scaled-down Amazon-style global e-commerce platform for physical and electronic books.
- Designed for 1M MAU with high availability, multi-currency support, and strict regulatory compliance.

## Key Elements
- **Users:** Casual Shoppers, Book Enthusiasts, Store Administrators, Customer Support.
- **Frontend Container:** Single Page Application (React) served via Amazon S3 and Amazon CloudFront.
- **API Gateway:** Amazon API Gateway providing REST/GraphQL entry points, rate limiting, and JWT validation.
- **Backend Containers:** Catalog & Search (Spring Boot/OpenSearch), Order & Checkout (Spring Boot), Recommendation, Localization & Tax, Content & Review (Node.js/Amazon DocumentDB), and Admin Back-Office.
- **Data & Messaging:** Amazon Aurora PostgreSQL (Multi-AZ), Amazon SQS, Amazon SNS, and Amazon EventBridge.
- **External Systems:** Payment Gateway, Third-Party Shipping Provider, Tax & Currency Provider.

## Relationships
- Shoppers interact with the SPA via HTTPS.
- SPA calls Amazon API Gateway using HTTPS/REST/GraphQL.
- API Gateway routes internal traffic to backend containers using synchronous gRPC (intra-region VPC links).
- Backend services communicate asynchronously via Amazon SQS, SNS, and EventBridge.
- Order & Checkout container integrates with third-party shipping and payment APIs over HTTPS.

## Technology Stack
- **Frontend:** React, Amazon CloudFront, Amazon S3.
- **API & Routing:** Amazon API Gateway, gRPC for internal service-to-service communication.
- **Backend Services:** Spring Boot, Node.js/Express.
- **Databases & Search:** Amazon Aurora PostgreSQL, Amazon OpenSearch, Amazon DocumentDB.
- **Messaging & Events:** Amazon SQS, Amazon SNS, Amazon EventBridge.
- **Infrastructure & DevOps:** AWS ECS/EKS, Amazon CodePipeline, AWS X-Ray, Amazon CloudWatch, AWS CloudTrail.

## Rationale
- Container isolation protects checkout transactional integrity and maintains 99.95% uptime during peak loads.
- Decoupled ML recommendations and localization services prevent resource starvation, ensuring page loads remain under 2 seconds.