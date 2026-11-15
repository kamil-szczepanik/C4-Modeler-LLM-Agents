## Overview
The Online Bookstore is a globally scaled e-commerce platform for physical and electronic books, supporting browsing, secure checkout, reviews, and personalized recommendations. It operates across multiple AWS regions while adhering to GDPR, CCPA, and multi-currency constraints.

## Key Elements
- React Single-Page Application (SPA) hosted on AWS S3 with CloudFront CDN
- AWS API Gateway for secure API management
- Core E-Commerce Service, Recommendation Engine, Audit & Compliance Service, and Integration Service running on Amazon ECS Fargate
- Amazon Aurora PostgreSQL for relational data and Amazon DynamoDB for NoSQL storage
- Amazon ElastiCache (Redis) for caching
- Amazon OpenSearch Service for catalogue search and analytics
- Amazon EventBridge for asynchronous event routing
- Amazon SQS / SNS and AWS Lambda for messaging and serverless processing

## Relationships
- React SPA -> AWS API Gateway: RESTful API requests [HTTPS/JSON]
- AWS API Gateway -> ECS Fargate Containers: Internal routing [HTTP/gRPC]
- Core E-Commerce Service -> Amazon Aurora PostgreSQL: Transaction persistence [SQL/TCP]
- Core E-Commerce Service -> Amazon EventBridge: Publishes domain events [AWS SDK / HTTPS]
- Amazon EventBridge -> Amazon SQS/SNS & AWS Lambda: Asynchronous event delivery [AWS Internal / HTTPS]

## Technology Stack
- React: Provides a responsive user interface on the SPA
- Amazon ECS Fargate: Container orchestration for microservices without server management
- Amazon Aurora PostgreSQL: Relational database ensuring ACID compliance for orders and users
- Amazon OpenSearch Service: Powers fast catalogue keyword searches
- Amazon EventBridge: Fully managed event bus enabling decoupled microservice architecture

## Rationale
This AWS-native, serverless, and containerized microservices architecture guarantees the required 1 M MAU scalability and 99.95% uptime. Decoupled asynchronous messaging via EventBridge ensures high performance even under high load while meeting strict regulatory and security standards.