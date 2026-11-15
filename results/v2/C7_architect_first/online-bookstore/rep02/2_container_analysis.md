## Overview
- E-commerce online bookstore for buying physical and electronic books with recommendations and reviews.
- Deployed on AWS across us-east-1, eu-west-1, and ap-southeast-1 to handle 1M MAU with 99.95% uptime.

## Key Elements
- Single Page Application (React.js, AWS S3, CloudFront)
- API Gateway (AWS API Gateway, AWS Cognito JWT validation)
- Core E-Commerce Container (Node.js/TypeScript)
- Recommendation & Review Container (Python, FastAPI)
- Tax & Currency Container (Node.js)
- Databases (Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon ElastiCache Redis)
- Event Bus & Integration (Amazon SQS/SNS, third-party shipping and tax/currency APIs)

## Relationships
- SPA to API Gateway: HTTPS / WSS
- API Gateway to Fargate Containers: Internal VPC Application Load Balancers (gRPC / HTTPS)
- Services to Databases: PostgreSQL wire protocol, DynamoDB API, Redis protocol
- Asynchronous Events: Amazon SQS / SNS

## Technology Stack
- React.js / S3 / CloudFront: High-performance frontend delivery for <2s page load times
- AWS API Gateway & Cognito: Scalable entry point with secure JWT validation
- Amazon ECS with AWS Fargate: Consistent container orchestration across multiple regions
- Amazon Aurora PostgreSQL & DynamoDB: Transactional and low-latency storage with global replication and geo-fencing
- Amazon ElastiCache Redis: Local caching for recommendations to protect performance

## Rationale
- Multi-region Fargate deployment ensures 99.95% availability and scalability for 1M MAU while meeting strict GDPR/CCPA data residency rules.
- Isolated microservices support specialized domains like recommendations and multi-currency taxation without compromising page performance.