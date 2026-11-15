## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform designed to sell physical and electronic books with integrated reviews and recommendations. It delivers high scalability, multi-region availability, and compliance with retail and data privacy regulations.

## Key Elements
- **Users**: Customer, Store Administrator
- **Client**: Single Page App (SPA) built with React/TypeScript
- **Edge**: Amazon CloudFront / S3, Amazon API Gateway (REST/GraphQL)
- **Services (Containers)**: Catalog Service (Go), Order & Checkout Service (Node.js/Express), Recommendation Service (Python/FastAPI)
- **Data & Messaging**: Amazon DynamoDB, Amazon Aurora PostgreSQL, Amazon ElastiCache (Redis), Amazon SQS / SNS / EventBridge
- **External Systems**: Payment Gateway, Shipping Provider APIs, Email/Notification Service, Tax Calculation Service, Identity Provider (IdP)

## Relationships
- **Customer/Admin to SPA**: HTTPS via Amazon CloudFront
- **SPA to API Gateway**: HTTPS / GraphQL / REST
- **API Gateway to Core Services**: gRPC / HTTPS over internal VPC networks
- **Core Services to Data/Messaging**: Internal AWS VPC protocols (TCP/Redis/PostgreSQL/DynamoDB protocols)
- **Services to External Systems**: HTTPS webhooks and APIs (Payment, Shipping, Email, Tax, IdP)

## Technology Stack
- **Frontend**: React and TypeScript hosted on Amazon CloudFront and S3 for fast client-side performance.
- **Compute**: Amazon ECS with AWS Fargate for serverless container orchestration ensuring auto-scaling.
- **Databases**: Amazon DynamoDB for catalogue search speed, Amazon Aurora PostgreSQL for ACID-compliant transactions, and Amazon ElastiCache (Redis) for real-time recommendations.
- **Integration**: Amazon API Gateway, SQS, SNS, and EventBridge for asynchronous event-driven workflows and API routing.
- **Cloud Provider**: AWS across `us-east-1`, `eu-west-1`, and `ap-southeast-1` regions.

## Rationale
This architecture leverages managed AWS services and containerization via ECS Fargate to effortlessly scale to 1M MAU while maintaining 99.95% uptime. Multi-region deployment, Aurora Multi-AZ replicas, and decoupled event-driven services via SQS/EventBridge guarantee low-latency performance, high availability, and secure processing.