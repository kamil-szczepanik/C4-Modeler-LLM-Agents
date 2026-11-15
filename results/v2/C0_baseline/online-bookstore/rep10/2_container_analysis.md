## Overview
- Scalable, high-availability online bookstore built on AWS serving 1M MAU across multi-regions.
- Delivers secure e-commerce capabilities including catalogue browsing, cart management, checkout, reviews, and recommendations.

## Key Elements
- **Shopper, Author/Publisher, Administrator**: External human users interacting with the platform.
- **Single Page Application (SPA)**: React/TypeScript frontend hosted on Amazon S3 and CloudFront.
- **API Gateway**: AWS API Gateway acting as the single secure entry point.
- **Catalog & Search Container**: Spring Boot (Java) service on Amazon ECS Fargate.
- **Checkout & Order Container**: Spring Boot (Java) service on Amazon ECS Fargate.
- **Recommendation Service**: Python (FastAPI) service on Amazon ECS Fargate.
- **Shipping & Payment Integration Worker**: AWS Lambda and Amazon SQS background workers.
- **Data Stores**: Amazon Aurora PostgreSQL and Amazon DynamoDB.
- **External Systems**: Payment Gateway, Third-Party Shipping API, Tax & Compliance Service.

## Relationships
- Shopper uses HTTPS/REST to access SPA on Amazon S3/CloudFront.
- SPA communicates via HTTPS/REST and gRPC through AWS API Gateway.
- API Gateway routes synchronously via REST to Catalog & Checkout containers, and gRPC to Recommendation Service.
- Checkout & Order Container uses AWS SQS to communicate with Shipping & Payment Integration Worker.
- Checkout Container calls Tax & Compliance Service via HTTPS over AWS PrivateLink.
- Services persist state to Amazon Aurora PostgreSQL and Amazon DynamoDB using AWS KMS encryption.

## Technology Stack
- **Frontend Hosting**: Amazon S3 + CloudFront CDN for global <2s page load performance.
- **API Routing**: AWS API Gateway for rate limiting and JWT validation.
- **Compute**: Amazon ECS Fargate for container orchestration and AWS Lambda for asynchronous tasks.
- **Databases**: Amazon Aurora PostgreSQL for transactional data and Amazon DynamoDB for recommendations.
- **Messaging**: Amazon SQS with Dead Letter Queues for asynchronous checkout processing.
- **Security**: AWS Cognito for OIDC/OAuth2, AWS Secrets Manager for credentials, and AWS KMS for data at rest.

## Rationale
- Microservices containerization on ECS Fargate enables independent scaling of read-heavy catalog searches from resource-sensitive checkout flows.
- Strict isolation of payment and shipping processing via SQS/Lambda workers ensures fault tolerance and compliance with security standards.