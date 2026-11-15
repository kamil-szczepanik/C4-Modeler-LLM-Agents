## Overview
The Online Bookstore is a scaled-down e-commerce system built on AWS to support physical and electronic book sales, recommendations, and reviews. It handles 1 million monthly active users while ensuring GDPR compliance, multi-currency support, and 99.95% uptime.

## Key Elements
* Customer and Administrator (Users)
* Payment Gateway, Shipping Provider APIs, Email Service, Identity Provider, Tax Calculation Service (External Systems)
* Single-Page App, API Gateway, Catalog Service, Order & Checkout Service, Recommendation Service, Email Service (Containers)
* Amazon RDS, Amazon OpenSearch, Amazon DynamoDB, Amazon ElastiCache (Data Stores)
* Request Router, Partition Router, Storage Node, Replication Manager, Streams Processor, Global Secondary Index (GSI) Manager (Amazon DynamoDB Components)

## Relationships
* Catalog Service -> Amazon DynamoDB: Reads and writes customer reviews and ratings [DynamoDB API]
* Catalog Service -> GSI Manager: Queries book reviews and ratings sorted by date or score [DynamoDB API]
* Single-Page App -> API Gateway: Routes user requests [HTTPS]
* API Gateway -> Catalog Service, Order Service, Recommendation Service: Invokes backend containers [gRPC / REST]

## Technology Stack
* AWS (us-east-1, eu-west-1, ap-southeast-1): Target cloud provider for multi-region resilience
* React, AWS S3, CloudFront: Powers the frontend Single-Page App for fast global delivery (<2s on 3G)
* Node.js, NestJS, Amazon ECS/Fargate: Container runtime for scalable microservices
* Amazon RDS (PostgreSQL): Relational storage for transactional data
* Amazon OpenSearch: Powers keyword catalogue search
* Amazon DynamoDB: NoSQL storage with GSI Manager for high-throughput reviews and ratings

## Rationale
This AWS-native, containerized microservices architecture leverages managed services like ECS, DynamoDB, and OpenSearch to easily scale to 1 million MAU. Decoupled services and multi-AZ replication guarantee 99.95% availability while meeting strict OWASP security and GDPR compliance mandates.