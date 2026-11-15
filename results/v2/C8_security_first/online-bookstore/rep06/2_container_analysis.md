## Overview
- Scaled-down Amazon-style e-commerce platform for purchasing physical and electronic books with recommendations and reviews.
- Designed to handle 1M MAU globally while maintaining strict security, GDPR/CCPA compliance, and high availability.

## Key Elements
- Shoppers, Vendors, and Admins
- Single Page Application (React, AWS S3, CloudFront)
- API Gateway / AWS ALB with AWS WAF
- AWS Lambda@Edge (Localization Service)
- ECS Fargate Microservices: Catalogue, Checkout & Cart, Recommendation, Vendor Portal, Review & Rating
- Databases: Amazon OpenSearch, PostgreSQL, Redis, Amazon DynamoDB
- Integration & Messaging: Amazon SQS, Amazon EventBridge/SNS, Payment Gateway, Third-Party Shipping APIs

## Relationships
- Shoppers to SPA via HTTPS/REST
- SPA to API Gateway via HTTPS/REST
- API Gateway to ECS Fargate containers via gRPC and HTTPS
- Containers to Databases via internal VPC connections
- Checkout Container to Payment Gateway and Shipping APIs via Amazon SQS async queues

## Technology Stack
- Frontend: React hosted on AWS S3 and CloudFront for edge performance
- Compute: AWS ECS Fargate for scalable microservices
- Databases: PostgreSQL for transactions, OpenSearch for search, Redis for recommendations, DynamoDB for reviews
- Messaging: Amazon SQS and EventBridge for asynchronous decoupling
- Security: AWS Cognito (OAuth2/OIDC), AWS Secrets Manager, AWS KMS, AWS WAF

## Rationale
- Decoupling core containers via SQS and EventBridge prevents cascading failures and ensures 99.95% uptime for checkouts.
- AWS edge caching and Fargate auto-scaling meet the strict 2-second performance SLA under a 1M MAU load.