## Overview
- Scalable, resilient, and GDPR-compliant online bookstore supporting physical/electronic book purchases, reviews, and personalized recommendations.
- Built on a multi-region AWS cloud footprint (us-east-1, eu-west-1, ap-southeast-1) designed to handle 1M MAU with 99.95% uptime.

## Key Elements
- React Single-Page Application (SPA) hosted on AWS CloudFront / S3
- AWS API Gateway
- Core E-Commerce Service, Recommendation Engine, Audit & Compliance Service, and Integration Service (Node.js/Python on Amazon ECS with Fargate)
- Search & Analytics Service (Amazon OpenSearch Service)
- Amazon Aurora PostgreSQL, Amazon DynamoDB, and Amazon ElastiCache (Redis)
- Amazon EventBridge, Amazon SQS/SNS, and AWS Lambda
- External Systems: Payment Gateway, Third-Party Shipping API, Notification Service, Currency Exchange Rate API

## Relationships
- SPA interacts with API Gateway via HTTPS/REST
- API Gateway routes traffic to Core E-Commerce, Audit Service, and Search & Analytics via HTTPS/REST or gRPC
- Core E-Commerce reads/writes transactional data to Aurora PostgreSQL, sessions to DynamoDB, and cache to ElastiCache (Redis) via TLS
- Core E-Commerce publishes events via Amazon EventBridge and SQS to trigger the Integration Service
- Integration Service calls external Payment Gateway and Shipping APIs via HTTPS/REST

## Technology Stack
- AWS CloudFront / S3 & CloudFront Functions: Global content delivery and edge logic for low latency
- Node.js (TypeScript) & Python: Core backend services and recommendation engine on AWS ECS Fargate
- Amazon Aurora PostgreSQL & DynamoDB: Relational ACID compliance and NoSQL cart storage
- Amazon OpenSearch Service: Dedicated keyword search and review indexing
- Amazon ElastiCache (Redis): Distributed session caching and hot data performance
- Amazon EventBridge & SQS: Decoupled asynchronous event-driven messaging

## Rationale
- Containerized microservices on ECS Fargate with ElastiCache and OpenSearch ensure sub-2s page loads and high scalability for 1M MAU.
- Decoupled event routing via EventBridge and SQS combined with dedicated integration services guarantees 99.95% availability despite third-party API dependencies.