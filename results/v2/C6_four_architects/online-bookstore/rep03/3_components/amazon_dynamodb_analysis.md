## Overview
The Online Bookstore is a scaled-down e-commerce platform for purchasing physical and electronic books, featuring reviews and recommendations. It utilizes a microservices architecture deployed across multiple AWS regions to ensure high scalability and availability.

## Key Elements
- **Users**: Customer, Store Administrator
- **External Systems**: AWS CloudFront/Route 53, Stripe, PayPal, UPS, FedEx, Avalara, AWS SES/SNS, AWS Personalize, AWS Fraud Detector
- **Containers**: React SPA, Amazon API Gateway, Spring Boot Catalog & Search Service, Node.js Order & Checkout Service, .NET Core Payment & Currency Service, Python Recommendation & Review Service, Python Data Privacy & User Service, .NET Core Admin & Content Management Service, Python Async Worker Service, Amazon RDS (PostgreSQL), Amazon DynamoDB, Amazon ElastiCache (Redis), Amazon OpenSearch, Amazon EventBridge & SQS
- **DynamoDB Components**: Request Router, Storage Nodes (RocksDB), Streams Processor, Global Tables Replicator, TTL Background Cleaner, Request Authenticator (AWS IAM), Partition Metadata Catalog

## Relationships
- React SPA -> Amazon CloudFront: Delivers static frontend assets [HTTPS]
- React SPA -> Amazon API Gateway: Sends user actions and API requests [HTTPS]
- Order & Checkout Service -> Request Router (DynamoDB): Manages shopping carts and order data [AWS SDK / HTTPS / SigV4]
- Storage Nodes -> Streams Processor: Triggers change data capture events [Internal RPC]
- Streams Processor -> Amazon EventBridge & SQS: Publishes asynchronous domain events [Internal AWS RPC]

## Technology Stack
- **Cloud Provider**: AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for multi-region global availability
- **Frontend**: React, Amazon S3, Amazon CloudFront for low-latency delivery
- **Backend Services**: Spring Boot, Node.js, .NET Core, and Python for domain microservices
- **Databases & Caching**: Amazon RDS (PostgreSQL), Amazon DynamoDB (NoSQL), Amazon ElastiCache (Redis)
- **Search & Messaging**: Amazon OpenSearch, Amazon EventBridge, Amazon SQS

## Rationale
This architecture leverages managed AWS services to easily scale and handle 1 million MAU with low latency. Multi-region deployments and AWS Global Tables ensure high availability and compliance with global retail standards.