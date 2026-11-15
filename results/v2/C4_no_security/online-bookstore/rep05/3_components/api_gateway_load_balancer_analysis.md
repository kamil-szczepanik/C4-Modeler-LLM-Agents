## Overview
An Amazon-style e-commerce online bookstore for physical and electronic books handling 1M MAU. It features a scalable microservices architecture deployed across multiple global AWS regions.

## Key Elements
- **Users**: Customer (Shopper), Book Author/Publisher, Store Administrator
- **External Systems**: Payment Gateway, Shipping Provider APIs, Identity Provider, Notification System, Tax Calculation Service
- **Client Container**: Single Page Application (React, TypeScript, Amazon CloudFront, S3)
- **Edge & Gateway Containers**: API Gateway & Load Balancer (AWS API Gateway, ALB, AWS WAF, Amazon Route 53)
- **Backend Microservices (Amazon ECS on Fargate)**: Catalog & Search Service, Checkout & Order Service, Recommendation Service, Data Privacy Service, Localization Service
- **Data & Messaging Stores**: Amazon Aurora (PostgreSQL), Amazon DynamoDB, Amazon OpenSearch, Amazon SQS, Amazon SNS

## Relationships
- **Single Page Application -> API Gateway & Load Balancer**: Sends secure client requests and real-time streams via HTTPS/REST and WebSockets
- **API Gateway & Load Balancer -> Catalog & Search Service**: Routes catalog search queries via gRPC/REST
- **API Gateway & Load Balancer -> Checkout & Order Service**: Routes secure checkout and order processing via gRPC/REST
- **API Gateway & Load Balancer -> Recommendation Service**: Routes recommendation requests via gRPC/REST

## Technology Stack
- **Cloud Infrastructure**: Amazon Web Services (AWS) across `us-east-1`, `eu-west-1`, and `ap-southeast-1` for global scale
- **Frontend**: React and TypeScript hosted on Amazon S3 and distributed via Amazon CloudFront
- **API & Routing**: AWS API Gateway, Application Load Balancer (ALB), and Amazon Route 53 for latency-based DNS routing
- **Compute**: Amazon ECS on Fargate for containerized microservices
- **Databases & Search**: Amazon Aurora (PostgreSQL) for relational data, Amazon DynamoDB for session caching, and Amazon OpenSearch for book search indexing
- **Messaging**: Amazon SQS and Amazon SNS with Dead Letter Queues for asynchronous event processing

## Rationale
This multi-region AWS serverless container architecture ensures 99.95% uptime and sub-2-second page loads globally for 1M MAU. Microservices isolation combined with robust data encryption and IAM policies guarantees compliance with GDPR, CCPA, and OWASP Top-10 security requirements.