## Overview
The Online Bookstore is a globally scaled, Amazon-style e-commerce platform designed to provide secure book catalog browsing, purchasing, and personalized recommendations. It guarantees high availability and sub-2-second performance across three AWS regions to serve 1 million monthly active users.

## Key Elements
- React Single-Page Application (SPA)
- Amazon API Gateway (Edge Request Router, Auth & Authorizer, Rate Limiter, GraphQL Proxy)
- Backend Microservices (Catalog, Order & Checkout, Recommendation on AWS ECS Fargate)
- Data Stores (Amazon RDS PostgreSQL, DynamoDB, ElastiCache Redis, OpenSearch)
- External Systems (Stripe, FedEx/UPS, Avalara, Auth0/AWS Cognito, SendGrid)

## Relationships
- React SPA -> Amazon API Gateway: Sends HTTPS/REST and GraphQL requests
- Amazon API Gateway -> ECS Microservices: Routes internal calls via gRPC over AWS App Mesh with TLS
- ECS Microservices -> Amazon RDS / DynamoDB / ElastiCache: Reads and writes domain data
- External Integrations: Communicates with Stripe for payments and Avalara for tax calculation

## Technology Stack
- **Frontend**: React (hosted on AWS S3, distributed via Amazon CloudFront)
- **API Ingress**: Amazon API Gateway, AWS Lambda (Custom Authorizer), AWS AppSync / API Gateway
- **Compute**: Node.js, Spring Boot, Python FastAPI deployed on AWS ECS (Fargate)
- **Data & Caching**: Amazon RDS PostgreSQL, Amazon DynamoDB, Amazon ElastiCache (Redis), Amazon OpenSearch
- **Infrastructure & Security**: AWS App Mesh, AWS CDK/Terraform, AWS X-Ray, CloudWatch

## Rationale
This architecture uses serverless edge routing and containerized microservices on AWS to easily scale past 1 million users while maintaining strict OWASP security and GDPR compliance. Region-distributed deployment guarantees 99.95% uptime and fast global performance.